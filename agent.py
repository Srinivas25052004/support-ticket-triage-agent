import json

from groq import Groq

from config import GROQ_API_KEY
from prompts import SYSTEM_PROMPT

client = Groq(api_key=GROQ_API_KEY)


def classify_ticket(subject, body):

    user_prompt = f"""
Subject:
{subject}

Description:
{body}
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            temperature=0.2,

            response_format={"type": "json_object"},

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        result = json.loads(
            response.choices[0].message.content
        )

        return {

            "category": result.get("category", "General"),
            "urgency": result.get("urgency", "Low"),
            "team": result.get("team", "Support Team"),
            "confidence": result.get("confidence", 80),
            "summary": result.get("summary", "No summary generated."),
            "reason": result.get("reason", "No reason generated."),
            "sentiment": result.get("sentiment", "Neutral"),
            "needs_human_review": result.get("needs_human_review", False)

        }

    except Exception as e:

        return {

            "category": "General",
            "urgency": "Low",
            "team": "Support Team",
            "confidence": 0,
            "summary": "Unable to analyze ticket.",
            "reason": str(e),
            "sentiment": "Neutral",
            "needs_human_review": True

        }