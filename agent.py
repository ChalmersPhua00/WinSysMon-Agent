import asyncio
import os
import json
from openai import AsyncOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Define how to run your server
server_params = StdioServerParameters(
    command=r"c:\Users\chalm\Documents\WinSysMon\winsysmon_venv\Scripts\python.exe",
    args=[r"c:\Users\chalm\Documents\WinSysMon\mcp_server.py"],
    env=os.environ.copy()
)

async def run_agent():
    # Connect to the server via stdio
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            mcp_tools = await session.list_tools()
            print(f"Connected to {len(mcp_tools.tools)} tools")

            # Convert MCP tools to OpenAI format
            openai_tools = []
            for tool in mcp_tools.tools:
                openai_tools.append({
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.inputSchema
                    }
                })

            # Initialize OpenAI (Assumes OPENAI_API_KEY is in environment variables)
            client = AsyncOpenAI()

            # Initialize chat history with a system prompt
            messages = [{"role": "system", "content": "You are a helpful Windows System Monitor assistant. You can use tools to check system status. When you identify an issue, use the navigation tools to open the relevant Settings page or System Tool to guide the user to the fix."}]

            print("\n-------------------------------------------------------")
            print("\n-------------------------------------------------------")
            print("\n _    _ _       _____           ___  ___ ")
            print("\n| |  | (_)     /  ___|          |  \/  | ")
            print("\n| |  | |_ _ __ \ `--. _   _ ___ | .  . | ___  _ __ ")
            print("\n| |/\| | | '_ \ `--. \ | | / __|| |\/| |/ _ \| '_ \ ")
            print("\n\  /\  / | | | /\__/ / |_| \__ \| |  | | (_) | | | | ")
            print("\n \/  \/|_|_| |_\____/ \__, |___/\_|  |_/\___/|_| |_| ")
            print("\n                       __/ | ")
            print("\n                      |___/ ")
            print("\n-------------------------------------------------------")
            print("\n---------------- (Type 'quit' to exit) ----------------")

            while True:
                # --- MEMORY MANAGEMENT (MemGPT-Lite) ---
                # If history exceeds 20 messages, summarize the older half to save tokens.
                if len(messages) > 20:
                    # 1. Preserve System Prompt (index 0)
                    sys_prompt = messages[0]
                    # 2. Identify messages to summarize (skip system prompt, keep last 5 for context)
                    # We summarize everything between the start and the last 5 messages.
                    to_summarize = messages[1:-5]
                    recent_history = messages[-5:]
                    # 3. Convert complex message objects to a simple string for the summarizer
                    history_text = ""
                    for msg in to_summarize:
                        if isinstance(msg, dict):
                            role = msg.get("role")
                            content = msg.get("content")
                        else:
                            continue
                        history_text += f"{role}: {content}\n"
                    # 4. Ask GPT-4o to compress this history
                    messages = [sys_prompt]
                    if history_text.strip():
                        summary_response = await client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "system", "content": "Summarize the following conversation history concisely. Retain key technical details."},
                                {"role": "user", "content": history_text}
                            ]
                        )
                        summary = summary_response.choices[0].message.content
                        messages.append({"role": "system", "content": f"PREVIOUS CONVERSATION SUMMARY: {summary}"})
                    messages += recent_history
                # ---------------------------------------

                # Get user query
                query = await asyncio.to_thread(input, "\nUser: ")
                if query.lower() in ["quit"]:
                    break
                messages.append({"role": "user", "content": query})

                # Loop to handle multiple tool steps (Agentic Loop)
                while True:
                    # Call OpenAI with tools
                    response = await client.chat.completions.create(
                        model="gpt-4o",
                        messages=messages,
                        tools=openai_tools,
                    )

                    # Process tool calls
                    response_msg = response.choices[0].message
                    messages.append(response_msg)
                    if response_msg.tool_calls:
                        for tool_call in response_msg.tool_calls:
                            func_name = tool_call.function.name
                            func_args = json.loads(tool_call.function.arguments)
                            print(f"Invoking tool: {func_name} with {func_args}")
                            # Execute tool via MCP
                            result = await session.call_tool(func_name, arguments=func_args)
                            tool_output = result.content[0].text
                            messages.append({
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": tool_output
                            })
                    else:
                        print(f"\nAgent: {response_msg.content}")
                        break

if __name__ == "__main__":
    asyncio.run(run_agent())