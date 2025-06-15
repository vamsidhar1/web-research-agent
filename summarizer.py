# summarizer.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following:\n\n{text[:2000]}"}
        ],
        max_tokens=200,
        temperature=0.7,
    )
    return response.choices[0].message["content"].strip()
