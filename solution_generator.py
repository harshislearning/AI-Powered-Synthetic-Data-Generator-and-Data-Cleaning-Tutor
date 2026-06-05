import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_cleaning_solution(
    profile,
    language,
    issues
):

    prompt = f"""
You are a Senior Data Cleaning Expert.

Dataset Information:

{profile}

Issues Found:

{issues}

Generate a COMPLETE step-by-step data cleaning solution.

Requirements:

1. Use {language}
2. Add comments for every step.
3. Handle missing values.
4. Handle duplicates.
5. Handle case inconsistencies.
6. Handle extra spaces.
7. Mention typo detection strategy.
8. Save final dataset as:

cleaned_dataset.csv

Return ONLY executable code.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=1500
        )

        return response.choices[0].message.content

    except Exception as e:

        import traceback
        return traceback.format_exc()