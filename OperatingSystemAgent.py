import platform
import subprocess

class OperatingSystemAgent:
    def __init__(self):
        self.os_name = platform.system()
        print(f"Operating System Detected: {self.os_name}")

    def run_diagnostics(self):
        command = self._get_diagnostic_command()
        if command:
            result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
            output = result.stdout.decode('utf-8')
            print("System diagnostics completed.")
            return self.os_name, output
        else:
            print("Unsupported OS.")
            return None, None

    def _get_diagnostic_command(self):
        if self.os_name == "Windows":
            return "systeminfo"
        elif self.os_name == "Linux":
            return "uname -a"
        elif self.os_name == "Darwin":  # macOS
            return "system_profiler SPSoftwareDataType"
        elif self.os_name in ["FreeBSD", "OpenBSD", "NetBSD"]:
            return "uname -a"
        elif self.os_name == "SunOS":  # Solaris
            return "uname -a"
        else:
            return None


