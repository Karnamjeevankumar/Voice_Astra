import os
import google.generativeai as genai
 
genai.configure(
api_key=os.getenv("GEMINI_API_KEY")
)
 
async def ask_gemini(prompt):
model = genai.GenerativeModel("gemini-2.5-pro")
 
response = model.generate_content(prompt)
 
return response.text