from transformers import pipeline
# from langchain_huggingface import HuggingFacePipeline
# from langchain.prompts import PromptTemplate
import torch

print(torch.cuda.is_available())

model = pipeline(task="summarization", model="facebook/bart-large-cnn")
response = model("text to summarize")
print(response)