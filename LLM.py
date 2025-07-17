# Run in any client
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

server_ip = os.getenv("M416_5090x2")
api_url = f"http://{server_ip}:8000/v1/chat/completions"

model = "Qwen/Qwen2.5-VL-7B-Instruct"
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Taiwan is a"
    }
]

pload = {
    "model": model,
    "messages": messages,
    "n": 1,
    "top_k": 0,
    "seed": 42,
    "temperature": 0.0,
    "max_tokens": 16,
    "stream": False,
}

# Send the request to the server
try:
    response = requests.post(api_url, json=pload)
    response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

    generated_text = response.json()["choices"][0]["message"]["content"]

    print(f"User Prompt: {messages[-1]['content']!r}")
    print(f"Generated Text: {generated_text!r}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")