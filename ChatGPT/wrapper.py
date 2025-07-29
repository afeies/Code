from openai import OpenAI
import os

class ChatGPT:
    def __init__(self, api_key=None, model='gpt-3.5-turbo'):
        self.client = OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
        self.model = model
        self.messages = []
    
    def chat(self, message):
        self.messages.append({'role': 'user', 'content': message})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        
        reply = response.choices[0].message.content
        self.messages.append({'role': 'assistant', 'content': reply})
        return reply
    
    def clear(self):
        self.messages = []

if __name__ == '__main__':
    chatgpt = ChatGPT()
    
    print(chatgpt.chat('Hello!'))
    print(chatgpt.chat("What's my name?"))
    
    chatgpt.clear()
    print(chatgpt.chat('Tell me a joke'))