import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

# Initialize the AzureOpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-05-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Create a vector store called "Financial Statements"
vector_store = client.beta.vector_stores.create(name="Financial Statements")
print(vector_store)