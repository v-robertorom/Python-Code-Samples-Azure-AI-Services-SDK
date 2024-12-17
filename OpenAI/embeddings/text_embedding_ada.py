from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = AzureOpenAI(
    api_key = os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version = "2024-02-01",
    azure_endpoint = os.getenv("AZURE_OPENAI_API_KEY")
)

response = client.embeddings.create(
    input = "This will be converted to a vector",
    model="text-embedding-ada-002"
)

print(response.model_dump_json(indent=2))
