import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/gpt2"

def get_headers():
    # Returns the headers required for the Hugging Face API request.
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

def normalize_whitespace(text):
    # Normalizes spaces in the text by replacing multiple spaces with a single space
    return ' '.join(text.split())

def validate_token():
    # Validates the Hugging Face API token by making a test request.
    # If invalid, prints the error and terminates the program.
    headers = get_headers()
    try:
        # Use a minimal, non-empty placeholder for "inputs"
        payload = {"inputs": "test"}

        # Make a test request
        response = requests.post(API_URL, headers=headers, json=payload)

        # Check if the response body is JSON
        try:
            response_json = response.json()
        except ValueError:
            print("\nError during token validation: Unexpected response format.")
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Content: {response.text}")
            exit(1)

        # Handle invalid token or other errors
        if response.status_code != 200:
            print(f"\nError: {response_json}")  # Display token error
            exit(1)

        print("\nToken validation successful. Ready to proceed.\n")
    except requests.RequestException as e:
        print(f"\nError during token validation: {e}")
        exit(1)

def generate_text(input_text):
    # Sends input to Hugging Face API, processes the generated text, and prints both input and output together.
    headers = get_headers()
    payload = {
        "inputs": input_text,
        "parameters": {
            "max_new_tokens": 50,
            "num_return_sequences": 1,
            "temperature": 0.8
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            generated_text = response.json()[0]['generated_text']
            # Normalize whitespace in the output text
            normalized_output = normalize_whitespace(generated_text)
            print(f"\nInput Text: {input_text}\nGenerated Text: {normalized_output}\n")
        else:
            json_response = response.json()
            print(f"\nError: {json_response}\n")
    except requests.RequestException as e:
        print(f"\nError during the API request: {e}\n")



def main():
    # Main function to handle user input
    print("Welcome to the Text Generation Tool!")
    print("Type 'exit' to quit the program.\n")
    # Validate token before allowing user interaction
    validate_token()
    while True:
        # Read input from the user
        user_input = input("Enter a prompt for text generation: ").strip()
        # Exit condition
        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break
        # Validate input: Check for non-letter characters except spaces
        if not all(char.isalpha() or char.isspace() for char in user_input):
            print("\nError: Input must not contain non-letter characters. Please try again.\n")
            continue
        generate_text(user_input)

# Run the main function
if __name__ == "__main__":
    main()