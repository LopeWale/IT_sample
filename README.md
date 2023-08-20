## Emmanuel Akinwale
# System Error Analysis Python Program

## Objective
This project aims to develop a Python program that utilizes agents and tools to effectively analyze system errors, generate solution guidance, and improve troubleshooting processes.

## Agents and Tools

### 1. Get Operating System Agent (OperatingSystemAgent.py)
- Retrieves the operating system name.
- Prints and returns the message "The operating system is: [operating system name]".

### 2. Run System Diagnostic Agent (RunSystemDiagnosticAgent.py)
- Runs system diagnostics.
- Writes the output to "system_dialog.log".
- Prints and returns the message "The system diagnostic output has been written to the system_dialog.log file."

### 3. Error Analysis Agent (ErrorAnalysisAgent.py)
- Analyzes the error output using the OpenAI API.
- Reads the content of "system_diagnostic.log", "system_event_log.log", and user-uploaded error log files.
- Analyzes the combined content using the OpenAI API.
- Appends analysis results to "AI_Analysis.log".
- Prints the message "The error output has been analyzed using the OpenAI API, and the results have been appended to the AI_Analysis.log file."

### 4. Create Solution Guidance Tool (SolutionGuidanceTool.py)
- Creates a solution guidance log file if an error is found.
- Prints the message "A solution guidance log file has been created with a summary of the problem and a few basic troubleshooting instructions."
- If no errors are found, prints the message "If no errors were found, the program has finished running."

### 5. Log Writer Tool (LogWriterTool.py)
- Defines methods to write logs to specified files.

## Chain of Execution

1. Get Operating System Agent retrieves the operating system name.
2. Run System Diagnostic Agent runs system diagnostics and writes the output to "system_dialog.log".
3. Error Analysis Agent analyzes the error output using the OpenAI API, considering "system_diagnostic.log", "system_event_log.log", and user-uploaded logs.
4. Analysis results are appended to "AI_Analysis.log".
5. If an error is found, Create Solution Guidance Tool creates a solution guidance log file.
6. Appropriate messages are printed as described in the objective.

## Usage

1. Run the `Main.py` script to execute the program.
2. Select options to execute individual modules or automatically run all modules.
3. The program follows a sequence of agent execution as described above.

---

This program streamlines the analysis of system errors, the generation of solution guidance, and enhances troubleshooting by utilizing a combination of agents and tools.
