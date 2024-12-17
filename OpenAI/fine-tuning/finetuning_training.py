# Submit fine-tuning training job

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),
  api_version = "2024-05-01-preview"  # This API version or later is required to access seed/events/checkpoint features
)

response = client.fine_tuning.jobs.create(
    training_file = "",
    validation_file = "",
    model = "gpt-35-turbo-0613", # Enter base model name. Note that in Azure OpenAI the model name contains dashes and cannot contain dot/period characters.
    seed = 105 # seed parameter controls reproducibility of the fine-tuning job. If no seed is specified one will be generated automatically.
)

job_id = response.id

# You can use the job ID to monitor the status of the fine-tuning job.
# The fine-tuning job will take some time to start and complete.

print("Job ID:", response.id)
print("Status:", response.status)
print(response.model_dump_json(indent=2))