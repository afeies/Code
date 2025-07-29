from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",   # nano does not support web search
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?"
)

print(response.output_text)