
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("API Key Loaded:", bool(key))

client = genai.Client(api_key=key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Generate one Python interview question."
)

print("Generated Question:")
print(response.text)
