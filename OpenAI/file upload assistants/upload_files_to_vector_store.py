import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the AzureOpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-05-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Ensure folder_path is an absolute path
folder_path = os.path.join(os.getcwd(), "test3")

# Collect all file paths in the 'test' folder
file_paths = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, filename))]

# Print full file paths for debugging
print("Full file paths:")
for path in file_paths:
    print(path)

# Open the file streams for uploading
file_streams = [open(path, "rb") for path in file_paths]

# Already uploaded files
files_id= ["assistant-y51N7OusxFGfeT9SkyT2bMUv","assistant-mMAwx7mtKFQr2HivykXJ27Fg","assistant-iepWFF5HXCLYIoRdFrgubedk","assistant-tln2lVhssHKNfHKfjYGWSsru","assistant-ppc7rY96hcTskaY20Jlz1zPs"]

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id='vs_l47wTYZccDGajLknpBIzAtxH', files=file_streams
    )

# Print the status and the file counts of the batch to see the result of this operation.
print(f"Batch status: {file_batch.status}")
print(f"Files processed: {file_batch.file_counts}")