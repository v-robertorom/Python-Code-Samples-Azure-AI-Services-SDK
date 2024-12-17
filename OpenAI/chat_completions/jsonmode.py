import os
from openai import AzureOpenAI
import time
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-05-01-preview"
)

start_time = time.time()

response = client.chat.completions.create(
    model="gpt-4o",
    stream=True,
    response_format={"type": "json_object"},
    messages=[
        {"role": "user", "content": "Say this is a test and return the response in a JSON format!"}
    ]
)

# Initialize a list to store the full response content
full_response = []

# Stream the response
for chunk in response:
    # Check if 'choices' exists and is not empty
    if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
        # Check if 'delta' and 'content' exist
        if hasattr(chunk.choices[0], 'delta') and hasattr(chunk.choices[0].delta, 'content'):
            content = chunk.choices[0].delta.content
            if content:  # Ensure content is not None
                # Print each chunk content
                print(content)
                # Append the chunk content to the full response list
                full_response.append(content)

# After the stream is complete, print the full response
print("\nFull response:")
print(''.join(full_response))  # Join the chunks into a full response