import requests
import json
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv
load_dotenv()


## https://learn.microsoft.com/en-us/rest/api/azure/
## https://learn.microsoft.com/en-us/rest/api/aiservices/accountmanagement/rai-policies/create-or-update?view=rest-aiservices-accountmanagement-2024-06-01-preview&tabs=HTTP
 
region = "eastus"
token_credential = DefaultAzureCredential()
subscriptionId = os.getenv("SUBSCRIPTION-ID")
resourceGroupName = os.getenv("RESOURCE-GROUP-NAME")
accountName = os.getenv("ACCOUNT-NAME")
 
token = token_credential.get_token('https://management.azure.com/.default')
headers = {'Authorization': 'Bearer ' + token.token}
 
url = f"https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/raiPolicies?api-version=2024-06-01-preview"
 
response = requests.get(url, headers=headers)
 
data = json.loads(response.text)
 
print(json.dumps(data, indent=4))