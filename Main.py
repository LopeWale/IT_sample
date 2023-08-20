import os
from dotenv import load_dotenv
from OperatingSystemAgent import OperatingSystemAgent
from RunSystemDiagnosticAgent import RunSystemDiagnosticAgent
from ErrorAnalysisAgent import ErrorAnalysisAgent
from ErrorLogUploader import ErrorLogUploader
import openai

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variables
openai_api_key = os.getenv("YOUR_OPENAI_API_KEY")

class MainApp:
    def __init__(self):
        self.error_uploader = ErrorLogUploader()
        self.os_agent = OperatingSystemAgent()
        self.diagnostic_agent = RunSystemDiagnosticAgent(self.os_agent)
        self.error_analysis_agent = ErrorAnalysisAgent(openai_api_key)

    def run(self):
        while True:
            print("Select an option:")
            print("1. Run specific diagnostics")
            print("2. Check for system errors")
            print("3. Get event logs")
            print("4. Analyze system errors using OpenAI")
            print("5. Automatically run all modules")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.diagnostic_agent.run_specific_diagnostics()
            elif choice == "2":
                self.error_uploader.check_for_errors()
            elif choice == "3":
                self.diagnostic_agent.get_event_logs()
            elif choice == "4":
                self.analyze_system_errors()
            elif choice == "5":
                self.run_all_modules()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def analyze_system_errors(self):
        # Read the content of the system diagnostic log
        with open("system_diagnostic.log", "r") as file:
            diagnostic_content = file.read()

        # Analyze the diagnostic content using the OpenAI API
        self.error_analysis_agent.analyze_system_errors()

    def run_all_modules(self):
        print("Automatically running all modules...")

        # Run specific diagnostics
        self.diagnostic_agent.run_specific_diagnostics()

        # Check for system errors
        self.error_uploader.check_for_errors()

        # Get event logs
        self.diagnostic_agent.get_event_logs()

        # Analyze system errors using OpenAI
        self.analyze_system_errors()

        print("All modules executed.")

if __name__ == "__main__":
    app = MainApp()
    app.run()






