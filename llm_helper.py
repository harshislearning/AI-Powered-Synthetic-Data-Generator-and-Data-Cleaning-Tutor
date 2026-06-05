import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_domain_context(domain):

    prompt = f"""
    Give short realistic context for dataset domain: {domain}

    Example:

    Students dataset contains:
    names, emails, marks, attendance, departments

    Keep response short.
    """

    try:

        response = client.chat.completions.create(
            model="qwen/qwen3-32b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=100
        )

        return response.choices[0].message.content

    except Exception:

        return "General synthetic dataset"