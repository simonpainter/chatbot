# Chatbot

A Python-based chatbot that answers questions about the content of a JSON file using the ChatGPT API.

## Description

The Chatbot is a command-line interface (CLI) tool that allows users to ask questions about the content of a JSON file. It utilizes the ChatGPT API to process the user's input, extract relevant information from the JSON data, and provide appropriate responses. The chatbot aims to provide a convenient way to retrieve specific information from a structured JSON file.

## Features

- CLI-based interface for easy interaction
- Integration with the ChatGPT API for natural language processing
- Parsing and querying JSON data to provide relevant answers
- Handling of edge cases and error scenarios
- Extensible architecture for future enhancements

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/simonpainter/chatbot.git
   ```

2. Navigate to the project directory:
   ```
   cd chatbot
   ```

3. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Obtain an API key from OpenAI and set the `OPENAI_API_KEY` environment variable with your API key.

## Usage

1. Prepare your JSON file containing the data you want to query. Place the file in the project directory and name it `data.json`.

2. Run the chatbot:
   ```
   python chatbot.py
   ```

3. Enter your questions or queries when prompted. The chatbot will process your input and provide relevant answers based on the content of the JSON file.

4. Type `quit` or `exit` to terminate the chatbot.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the existing code style and include appropriate tests.

## License

This project is licensed under the [MIT License](LICENSE).