import os
from openai import AzureOpenAI
client = AzureOpenAI(
    api_key=,  
    api_version=,
    azure_endpoint = 
    )

raw_response = client.chat.completions.with_raw_response.create(
    model="gpt-4", # model = "deployment_name".
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": "How are you?"}
    ]
)

chat_completion = raw_response.parse()
response_headers = raw_response.headers
