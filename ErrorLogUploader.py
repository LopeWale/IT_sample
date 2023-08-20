import os

class ErrorLogUploader:
    def __init__(self, diagnostic_log_path='system_diagnostic.log'):
        self.diagnostic_log_path = diagnostic_log_path

    def check_for_errors(self):
        if os.path.exists(self.diagnostic_log_path):
            with open(self.diagnostic_log_path, 'r') as file:
                content = file.read()
                # Check for specific error patterns; customize as needed
                if 'ERROR' not in content:
                    return self.prompt_for_log_upload()
                else:
                    print("Errors found in system diagnostics.")
                    return None
        else:
            print(f"{self.diagnostic_log_path} not found.")
            return None

    def prompt_for_log_upload(self):
        print("No errors found in system diagnostics. Would you like to upload an error log file? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            log_path = input("Please enter the path to the error log file: ").strip()
            if os.path.exists(log_path):
                print(f"Error log file {log_path} uploaded successfully.")
                return log_path
            else:
                print("File not found. Please check the path and try again.")
                return None
        else:
            print("No log file uploaded.")
            return None
