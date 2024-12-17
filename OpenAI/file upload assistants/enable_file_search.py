from openai import AzureOpenAI
import os
from dotenv import load_dotenv
load_dotenv()


client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-05-01-preview",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

assistant = client.beta.assistants.create(
  name="Financial Analyst Assistant",
  instructions="You are an expert financial analyst. Use your knowledge base to answer questions about audited financial statements.",
  model="gpt-4o",
  tools=[{"type": "file_search"}],
)