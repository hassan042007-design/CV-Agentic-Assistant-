import os
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader

load_dotenv(override=True)

# Load API key
groq_api_key = os.getenv("Groq_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found! Check your .env file.")
else:
    print(f"Groq API key loaded: {groq_api_key[:4]}...")

# Create client
client = Groq(api_key=groq_api_key)


# Print the response
# print(response.choices[0].message.content)

reader = PdfReader("My CV.pdf") 
cv_teaxt = ""
for page in reader.pages:  
    cv_teaxt += page.extract_text() + "\n"

# Define prompts
system_prompt = f"""You are assisstant. You are responsible to reply to questions about my career. 
You have my cv here:\n {cv_teaxt} . use it to reply."""

user_prompt = ""

#Call the API
while True:
    user_prompt = input("What is your question ? \n ")
    if user_prompt == "exit":
        print("Exiting the program.")
        break
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # free & powerful
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt}
        ]
    )
    reply_from_ai = response.choices[0].message.content
    print(reply_from_ai)
