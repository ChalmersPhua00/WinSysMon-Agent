from mcp.server.fastmcp import FastMCP
import sys
import os
import subprocess
import io
import contextlib

# Add current directory to path to ensure we can import local modules
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
# Import local modules
from Process import list_processes as list_processes_module
from Filesystem import search_filesystem as search_filesystem_module
from Filesystem import find_large_files as find_large_files_module
from Filesystem import disk_usage as disk_usage_module
from Filesystem import list_directory as list_directory_module
from Filesystem import read_file as read_file_module
from Filesystem import file_metadata as file_metadata_module
from Networking import get_network_adapters as get_network_adapters_module
from Networking import get_active_connections as get_active_connections_module
from Networking import get_listening_ports as get_listening_ports_module
from Networking import get_routing_table as get_routing_table_module
from Networking import ping_host as ping_host_module
from Networking import trace_route as trace_route_module
from Networking import get_dns_info as get_dns_info_module
from Networking import get_network_statistics as get_network_statistics_module
from Networking import get_wifi_profiles as get_wifi_profiles_module
from Performance import get_cpu_usage as get_cpu_usage_module
from Performance import get_ram_usage as get_ram_usage_module
from Performance import get_disk_io as get_disk_io_module
from Performance import get_network_io as get_network_io_module
from Performance import get_system_performance as get_system_performance_module
from Performance import get_top_processes_by_cpu as get_top_processes_by_cpu_module
from Performance import get_top_processes_by_mem as get_top_processes_by_mem_module
from Performance import get_performance_counters as get_performance_counters_module
from Performance import monitor_real_time as monitor_real_time_module
from Services import list_services as list_services_module
from Services import get_service_details as get_service_details_module
from Services import get_service_status as get_service_status_module
from Services import find_service as find_service_module
from Services import get_running_services as get_running_services_module
from Services import get_startup_services as get_startup_services_module
from Registry import read_registry_key as read_registry_key_module
from Registry import read_registry_value as read_registry_value_module
from Registry import search_registry_keys as search_registry_keys_module
from Registry import list_registry_subkeys as list_registry_subkeys_module
from Registry import get_startup_programs_registry as get_startup_programs_registry_module
from Registry import get_installed_programs_registry as get_installed_programs_registry_module
from Registry import get_system_info_registry as get_system_info_registry_module
from System import get_system_overview as get_system_overview_module
from System import get_hardware_info as get_hardware_info_module
from System import get_os_info as get_os_info_module
from System import get_environment_vars as get_environment_vars_module
from System import get_installed_software as get_installed_software_module
from System import get_system_uptime_info as get_system_uptime_info_module
from System import get_user_info as get_user_info_module
from System import get_system_paths as get_system_paths_module
# Initialize FastMCP server
mcp = FastMCP("WinSysMon")

def capture_stdout(func, *args, **kwargs):
    """Helper to capture print output from existing functions"""
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        func(*args, **kwargs)
    return f.getvalue()

@mcp.tool()
def list_processes() -> str:
    """Lists current running processes."""
    return capture_stdout(list_processes_module.list_processes)

@mcp.tool()
def search_filesystem(pattern: str, path: str, recursive: bool) -> str:
    """Searches for files matching a pattern."""
    return capture_stdout(search_filesystem_module.search_filesystem, pattern, path, recursive)

@mcp.tool()
def find_large_files(path: str, size_threshold_mb: int) -> str:
    """Finds files larger than the specified threshold in MB."""
    return capture_stdout(find_large_files_module.find_large_files, path, size_threshold_mb)

@mcp.tool()
def disk_usage() -> str:
    """Retrieves disk usage information."""
    return capture_stdout(disk_usage_module.disk_usage)

@mcp.tool()
def list_directory(path: str, recursive: bool) -> str:
    """Lists directory contents."""
    return capture_stdout(list_directory_module.list_directory, path, recursive)

@mcp.tool()
def read_file(path: str) -> str:
    """Reads the content of a file."""
    return capture_stdout(read_file_module.read_file, path)

@mcp.tool()
def file_metadata(path: str) -> str:
    """Retrieves file metadata."""
    return capture_stdout(file_metadata_module.file_metadata, path)

@mcp.tool()
def get_network_adapters() -> str:
    """Retrieves network adapter information and IP configuration."""
    return capture_stdout(get_network_adapters_module.get_network_adapters)

@mcp.tool()
def get_active_connections(protocol: str) -> str:
    """Retrieves active network connections. Protocol can be 'tcp', 'udp', or 'all'."""
    return capture_stdout(get_active_connections_module.get_active_connections, protocol)

@mcp.tool()
def get_listening_ports(protocol: str) -> str:
    """Retrieves listening ports. Protocol can be 'tcp', 'udp', or 'all'."""
    return capture_stdout(get_listening_ports_module.get_listening_ports, protocol)

@mcp.tool()
def get_routing_table() -> str:
    """Retrieves the IPv4 routing table."""
    return capture_stdout(get_routing_table_module.get_routing_table)

@mcp.tool()
def ping_host(host: str, count: int) -> str:
    """Pings a host. Host: a domain name (eg. "google.com") or an IP address (eg. "8.8.8.8) | count: number of ping requests to the target."""
    return capture_stdout(ping_host_module.ping_host, host, count)

@mcp.tool()
def trace_route(host: str) -> str:
    """Traces the route to a host."""
    return capture_stdout(trace_route_module.trace_route, host)

@mcp.tool()
def get_dns_info() -> str:
    """Retrieves DNS servers and cache information."""
    return capture_stdout(get_dns_info_module.get_dns_info)

@mcp.tool()
def get_network_statistics() -> str:
    """Retrieves network adapter and protocol statistics."""
    return capture_stdout(get_network_statistics_module.get_network_statistics)

@mcp.tool()
def get_wifi_profiles() -> str:
    """Retrieves saved WiFi profiles."""
    return capture_stdout(get_wifi_profiles_module.get_wifi_profiles)

@mcp.tool()
def get_cpu_usage(duration: int) -> str:
    """Retrieves CPU usage statistics."""
    return capture_stdout(get_cpu_usage_module.get_cpu_usage, duration)

@mcp.tool()
def get_ram_usage() -> str:
    """Retrieves RAM usage statistics."""
    return capture_stdout(get_ram_usage_module.get_ram_usage)

@mcp.tool()
def get_disk_io() -> str:
    """Retrieves disk I/O statistics."""
    return capture_stdout(get_disk_io_module.get_disk_io)

@mcp.tool()
def get_network_io() -> str:
    """Retrieves network I/O statistics."""
    return capture_stdout(get_network_io_module.get_network_io)

@mcp.tool()
def get_system_performance() -> str:
    """Retrieves overall system performance metrics."""
    return capture_stdout(get_system_performance_module.get_system_performance)

@mcp.tool()
def get_top_processes_by_cpu(count: int) -> str:
    """Retrieves top processes by CPU usage."""
    return capture_stdout(get_top_processes_by_cpu_module.get_top_processes_by_cpu, count)

@mcp.tool()
def get_top_processes_by_mem(count: int) -> str:
    """Retrieves top processes by memory usage."""
    return capture_stdout(get_top_processes_by_mem_module.get_top_processes_by_mem, count)

@mcp.tool()
def get_performance_counters(counter_name: str) -> str:
    """Retrieves specific performance counters or lists categories."""
    return capture_stdout(get_performance_counters_module.get_performance_counters, counter_name)

@mcp.tool()
def monitor_real_time(duration: int, interval: int) -> str:
    """Monitors real-time performance metrics."""
    return capture_stdout(monitor_real_time_module.monitor_real_time, duration, interval)

@mcp.tool()
def list_services(status_filter: str, startup_type_filter: str, limit: int) -> str:
    """Lists Windows services with filtering. status_filter allowed values : running, stopped, paused, all. startup_type_filter allowed values : manual, auto, disabled, all."""
    return capture_stdout(list_services_module.list_services, status_filter, startup_type_filter, limit)

@mcp.tool()
def get_service_details(service_name: str) -> str:
    """Retrieves detailed information about a specific service."""
    return capture_stdout(get_service_details_module.get_service_details, service_name)

@mcp.tool()
def get_service_status(service_name: str) -> str:
    """Retrieves the current status of a specific service."""
    return capture_stdout(get_service_status_module.get_service_status, service_name)

@mcp.tool()
def find_service(search_term: str) -> str:
    """Searches for services by name or display name."""
    return capture_stdout(find_service_module.find_service, search_term)

@mcp.tool()
def get_running_services(limit: int) -> str:
    """Retrieves a list of currently running services."""
    return capture_stdout(get_running_services_module.get_running_services, limit)

@mcp.tool()
def get_startup_services(limit: int) -> str:
    """Retrieves services configured to start automatically."""
    return capture_stdout(get_startup_services_module.get_startup_services, limit)

@mcp.tool()
def read_registry_key(key_path: str) -> str:
    """Reads all values and properties of a specific registry key."""
    return capture_stdout(read_registry_key_module.read_registry_key, key_path)

@mcp.tool()
def read_registry_value(key_path: str, value_name: str) -> str:
    """Reads a specific value from a registry key."""
    return capture_stdout(read_registry_value_module.read_registry_value, key_path, value_name)

@mcp.tool()
def search_registry_keys(search_term: str, hive: str) -> str:
    """Searches for registry keys matching a term."""
    return capture_stdout(search_registry_keys_module.search_registry_keys, search_term, hive)

@mcp.tool()
def list_registry_subkeys(key_path: str, max_depth: int) -> str:
    """Lists subkeys of a registry key up to a specified depth."""
    return capture_stdout(list_registry_subkeys_module.list_registry_subkeys, key_path, max_depth)

@mcp.tool()
def get_startup_programs_registry() -> str:
    """Retrieves startup programs defined in the registry."""
    return capture_stdout(get_startup_programs_registry_module.get_startup_programs_registry)

@mcp.tool()
def get_installed_programs_registry() -> str:
    """Retrieves installed programs listed in the registry."""
    return capture_stdout(get_installed_programs_registry_module.get_installed_programs_registry)

@mcp.tool()
def get_system_info_registry() -> str:
    """Retrieves system information (OS version, CPU, etc.) from the registry."""
    return capture_stdout(get_system_info_registry_module.get_system_info_registry)

@mcp.tool()
def get_system_overview() -> str:
    """Retrieves a high-level overview of the system (Hostname, OS, CPU, RAM, Uptime)."""
    return capture_stdout(get_system_overview_module.get_system_overview)

@mcp.tool()
def get_hardware_info(category: str) -> str:
    """Retrieves detailed hardware information. Category can be 'cpu', 'memory', 'disk', 'network', or 'all'."""
    return capture_stdout(get_hardware_info_module.get_hardware_info, category)

@mcp.tool()
def get_os_info() -> str:
    """Retrieves detailed Operating System information and recent hotfixes."""
    return capture_stdout(get_os_info_module.get_os_info)

@mcp.tool()
def get_environment_vars() -> str:
    """Retrieves environment variables."""
    return capture_stdout(get_environment_vars_module.get_environment_vars)

@mcp.tool()
def get_installed_software() -> str:
    """Retrieves a list of installed software via WMI."""
    return capture_stdout(get_installed_software_module.get_installed_software)

@mcp.tool()
def get_system_uptime_info() -> str:
    """Retrieves system uptime and last boot time information."""
    return capture_stdout(get_system_uptime_info_module.get_system_uptime_info)

@mcp.tool()
def get_user_info() -> str:
    """Retrieves information about local user accounts and the current user."""
    return capture_stdout(get_user_info_module.get_user_info)

@mcp.tool()
def get_system_paths() -> str:
    """Retrieves important system paths and the PATH environment variable."""
    return capture_stdout(get_system_paths_module.get_system_paths)

if __name__ == "__main__":
    mcp.run()