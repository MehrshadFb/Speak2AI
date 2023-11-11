import openai
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

configure()
openai.api_key = os.getenv('API_KEY_OPENAI')

def ask_computer(prompt):
    configure()
    try:
        if not prompt:
            return "Prompt is empty."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=256
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"An error occurred: {str(e)}"

