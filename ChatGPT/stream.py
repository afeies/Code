from openai import OpenAI
client = OpenAI()

stream = client.responses.create(
    model="gpt-4.1-nano",
    input=[
        {
            "role": "user",
            "content": "Say 'double bubble bath' ten times fast.",
        },
    ],
    stream=True,
)

for event in stream:
    # print(event)
    if hasattr(event, "delta"):
        print(event.delta)
    print()