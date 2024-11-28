# Text Generation
This Python program generates text using the Hugging Face Inference API and the pre-trained GPT-2 model. It interacts with the API to produce text outputs based on user-provided prompts. It includes features for token validation, input validation, and error handling to ensure smooth functionality.
## Features
- **Token Validation**: Ensures the Hugging Face API token is valid before making requests.
- **Text Generation**: Accepts user prompts and generates text using the GPT-2 model via the Hugging Face API.
- **Input Validation**: Restricts input to alphabetic characters and spaces to avoid unexpected errors.
- **Whitespace Normalization**: Cleans up the generated text by removing unnecessary spaces.
## Prerequisites
1. **Hugging Face API Token**: Obtain an API token from [Hugging Face](https://huggingface.co/)
2. **Dependencies**: Install required Python packages using the command:
   
   ```
   pip install requests python-dotenv
   ```
## Setup Instructions
1. **Clone or download** the repository.
2. **Create a** `.env` **file**: Place the Hugging Face API token in a `.env` file in the project root:

   ```
   API_TOKEN=your_huggingface_api_token
   ```
3. **Run the Script**: Execute the script using Python:

   ```
   python text_generation.py
   ```
## How to Use
1. Launch the program by running the script.
2. Enter a text prompt when prompted. The tool will send the prompt to the GPT-2 model via the Hugging Face API and display the generated text.
3. Type `exit` to quit the program at any time.
## Code Overview
### Key Components
1. `load_dotenv()`: Loads the API token from the `.env` file.
2. `get_headers()`: Generates the required headers for API requests, including the authorization token.
3. `normalize_whitespace()`: Removes extra spaces from the generated text.
4. `validate_token()`: Verifies the API token by making a test request to the API.
5. `generate_text(input_text)`: Sends a user-provided prompt to the API and processes the response.
6. `main()`: The main function that manages user interactions, input validation, and text generation.
### Sample Execution Flow
1. User launches the program.
2. The script validates the API token. If invalid, the program terminates with an error message.
3. The user is prompted to enter a text prompt.
4. The program sends the input to the Hugging Face API and retrieves the generated text.
5. The processed text is displayed alongside the user’s input.
### Example
```
Welcome to the Text Generation Tool!
Type 'exit' to quit the program.


Token validation successful. Ready to proceed.

Enter a prompt for text generation: Life is a box of chocolates

Input Text: Life is a box of chocolates
Generated Text: Life is a box of chocolates with a frosted apple and chocolate bar, a dark-colored cupcake, and a cupcake made with frosting. You've got one meal filled with something else—a dessert, doodle, or a banana.

Enter a prompt for text generation: exit

Goodbye!
```
## Error Handling
- **Token Issues**: Prints a detailed error message and terminates if the token is invalid.
- **API Errors**: Displays the error message from the API response if the request fails.
- **Input Validation**: Rejects prompts containing non-alphabetic characters.
## Notes
- Ensure your Hugging Face API token has the required permissions to access the GPT-2 model.
