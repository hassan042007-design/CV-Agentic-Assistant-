import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print(f"OpenAI API key is set.{openai_api_key[:4]}")
else:
    print("")

system_prompt = """You are a marketing manager. Your are responsible for out FaceBook Page. 
                    You are professional and you help us generate stratigic content 


"""
user_prompt = "create a campaign for Saudi Arabia"

# OpenAI API Roles :

message = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
    
    ]

model_name = "gpt-4o-mini"

client = genai.Client()
response = client.models.generate_content(
    model="gemma-4-26b-a4b-it",
    contents=message,
)

print(response.text)
