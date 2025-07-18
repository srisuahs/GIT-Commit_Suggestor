# suggest.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")  # e.g., "openrouter/auto"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def suggest_commit_message(pr_description):
    print("Generating commit message...\n")

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are an expert developer. Suggest a clean and meaningful Git commit message based on the PR description."
            },
            {
                "role": "user",
                "content": pr_description
            }
        ],
        "max_tokens": 10,  # ✅ Safe for free credits
        "temperature": 0.7
    }

    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=data)
        print(f"📨 OpenRouter Response: {response.status_code}")
        response.raise_for_status()

        json_response = response.json()
        print("✅ OpenRouter API Response:", json_response)

        return json_response["choices"][0]["message"]["content"]

    except Exception as e:
        print("❌ OpenRouter API Error:", str(e))
        return "⚠️ Failed to generate commit message from OpenRouter."
