import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

def generate_text(input_text):
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}  

    payload = {
        "inputs": input_text,
        "parameters": {
            "max_new_tokens": 50,
            "num_return_sequences": 1,
            "temperature": 0.8
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        generated_text = response.json()[0]['generated_text']
        print("Input:", input_text)
        print("Generated Text:", generated_text)
    else:
        print("Error:", response.json())


generate_text("Life is a box of")
