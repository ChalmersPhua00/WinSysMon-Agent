@echo off
setlocal

REM Change directory to the script's location
cd /d "%~dp0"
echo "Starting up..."
REM Check if winsysmon_venv exists, if not create it
if not exist "winsysmon_venv" (
    python -m venv winsysmon_venv
)
REM Activate the environment
call winsysmon_venv\Scripts\activate
REM Upgrade pip
python -m pip install --upgrade pip --quiet
REM Install/Update dependencies
if exist "requirements.txt" (pip install -r requirements.txt --quiet)
REM Check for OpenAI Key
if "%OPENAI_API_KEY%"=="" (
    set /p OPENAI_API_KEY="Please enter your OpenAI API Key: "
)
python agent.py
pause