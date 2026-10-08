import os
import anthropic

client = anthropic.Anthropic(
api_key=os.getenv("ANTHROPIC_API_KEY")
)

async def ask_claude(prompt):
response = client.messages.create(
model="claude-sonnet-4",
max_tokens=500,
messages=[
{
"role": "user",
"content": prompt
}
]
)

return response.content[0].text