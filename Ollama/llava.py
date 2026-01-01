from openai import OpenAI
import base64

def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

image_base64 = encode_image(
    "/Users/alexfeies/Code/Code/Images3/frog.jpeg"
)

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="llava:7b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant that analyzes images in detail. Provide clear and descriptive responses."
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}"
                    }
                }
            ]
        }
    ],
    max_tokens=200
)

print(response.choices[0].message.content)