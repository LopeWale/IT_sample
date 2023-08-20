import openai
from ErrorLogUploader import ErrorLogUploader  # Add the import for ErrorLogUploader


class ErrorAnalysisAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_system_errors(self):
        # Read the content of the system diagnostic log
        with open("system_diagnostic.log", "r") as file:
            diagnostic_content = file.read()

        # Read the content of the system event log
        with open("system_event_log.log", "r") as file:
            event_log_content = file.read()

        # Initialize the user's error log content as an empty string
        error_log_content = ""

        # Check if the user uploaded an error_log.log file using ErrorLogUploader
        error_log_uploader = ErrorLogUploader()
        uploaded_log_path = error_log_uploader.check_for_errors()
        if uploaded_log_path:
            with open(uploaded_log_path, "r") as file:
                error_log_content = file.read()

        # Define the system message for the specific use case
        system_message = "You are an intelligent diagnostic analyzer."

        # Call the OpenAI Chat Completion API for diagnostic content
        diagnostic_responses = self._upload_text_in_chunks(
            system_message,
            f"Analyze the following system diagnostic:\n{diagnostic_content}"
        )

        # Call the OpenAI Chat Completion API for event log content
        event_log_responses = self._upload_text_in_chunks(
            system_message,
            f"Analyze the following event log:\n{event_log_content}"
        )

        # Call the OpenAI Chat Completion API for error log content
        error_log_responses = self._upload_text_in_chunks(
            system_message,
            f"Analyze the following error log:\n{error_log_content}"
        )

        # Combine the analysis results and append to AI_Analysis.log
        combined_result = (
            self._combine_responses(diagnostic_responses) + "\n\n" +
            self._combine_responses(event_log_responses) + "\n\n" +
            self._combine_responses(error_log_responses)
        )
        with open("AI_Analysis.log", "a") as file:
            file.write("\n\n")  # Add some separation between results
            file.write(combined_result)

        print("The error output has been analyzed using the OpenAI API and the results have been appended to the AI_Analysis.log file.")

    def _upload_text_in_chunks(self, system_message, content_to_analyze):
        max_length = 4097
        chunks = self.split_text_into_chunks(content_to_analyze, max_length)
        responses = []

        for chunk in chunks:
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": chunk},
            ]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            response_content = response['choices'][0]['message']['content']
            responses.append(response_content)

        return responses

    def split_text_into_chunks(self, text, max_length):
        chunks = []
        current_chunk = ""

        for word in text.split():
            if len(current_chunk) + len(word) + 1 > max_length:
                chunks.append(current_chunk)
                current_chunk = ""

            if current_chunk:
                current_chunk += " "
            current_chunk += word

        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def _combine_responses(self, responses):
        return "\n".join(responses)

