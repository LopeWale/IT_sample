import subprocess
import datetime
from OperatingSystemAgent import OperatingSystemAgent

class RunSystemDiagnosticAgent:
    def __init__(self, os_agent: OperatingSystemAgent):
        self.os_name = os_agent.os_name

    def run_specific_diagnostics(self):
        command = self._get_specific_diagnostic_command()
        if command:
            result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
            output = result.stdout.decode('utf-8')
            print("Specific diagnostics completed.")
            self._write_to_file('system_diagnostic.log', output)
            return output
        else:
            print("Unsupported OS or no specific diagnostics available.")
            return None

    def get_event_logs(self):
        interval = input("Please enter the time interval for the event logs (in minutes): ")
        try:
            interval = float(interval)
        except ValueError:
            print("Invalid input. Please enter a numeric value for the minutes.")
            return None

        command = self._get_event_log_command(interval)
        if command:
            result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
            output = result.stdout.decode('utf-8')
            self._write_to_file('system_event_log.log', output)
            return output

    def _get_specific_diagnostic_command(self):
        if self.os_name == "Windows":
            return "sfc /scannow"  # Windows
        elif self.os_name == "Linux":
            return "dmesg"         # Linux
        elif self.os_name == "Darwin":
            return "diskutil verifyDisk disk0" # macOS
        elif self.os_name in ["FreeBSD", "OpenBSD", "NetBSD"]:
            return "dmesg"         # Kernel log for BSD variants
        elif self.os_name == "SunOS": # Solaris
            return "prtdiag"       # System diagnostics for Solaris
        else:
            return None

    def _get_event_log_command(self, interval):
        interval = int(interval) # Cast the interval to an integer
        if self.os_name == "Windows":
            return f'powershell -command "Get-EventLog -LogName System -EntryType Error -After ((Get-Date).AddMinutes(-{interval})) | Format-Table -Wrap"'
        elif self.os_name == "Linux":
            return f"journalctl -p err..emerg --since '{interval} minutes ago'" # Linux
        elif self.os_name == "Darwin":
            return f"log show --last {interval}m --predicate 'eventMessage CONTAINS \"error\"'" # macOS
        else:
            return None

    def _write_to_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
