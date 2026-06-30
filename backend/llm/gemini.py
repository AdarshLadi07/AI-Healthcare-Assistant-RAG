import google.generativeai as genai

from config.config import GEMINI_API_KEY
from backend.llm.prompts import SYSTEM_PROMPT


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(report, question):

    prompt = f"""
{SYSTEM_PROMPT}

Medical Report:

{report}

Question:

{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text