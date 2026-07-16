import os
from dotenv import load_dotenv


load_dotenv()

# Get the Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


if not GROQ_API_KEY:
    raise ValueError(
        "❌ GROQ_API_KEY not found! Please create a .env file and add your API key."
    )