from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano",
    input=[
        {"role": "user", "content": "what teams are playing in this image?"},
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4iExM5slhUuWNIa8pIDa_4wCS2O84fwnPnQ&s"
                }
            ]
        }
    ]
)

print(response.output_text)