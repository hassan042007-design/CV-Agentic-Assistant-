import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(override=True)

# ✅ Make sure this matches EXACTLY what's in your .env file
gemini_api_key = os.getenv("GEMINI_API_KEY")

# ✅ Always check if key loaded correctly
if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY not found! Check your .env file.")
else:
    print(f"✅ API key loaded: {gemini_api_key[:4]}...")

system_prompt = """You are a marketing manager. You are responsible for our Facebook Page. 
You are professional and you help us generate strategic content."""

user_prompt = "create a campaign for Saudi Arabia"

client = genai.Client(api_key=gemini_api_key)

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
        ),
        contents=[
            types.Content(
                role="user",
                parts=[types.Part(text=user_prompt)]
            )
        ]
    )
    print(response.text)

except Exception as e:
    print(f"❌ Error: {e}")