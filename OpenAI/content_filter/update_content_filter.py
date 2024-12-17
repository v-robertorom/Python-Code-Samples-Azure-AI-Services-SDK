import requests
import json
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv
load_dotenv()


## https://learn.microsoft.com/en-us/rest/api/azure/
## https://learn.microsoft.com/en-us/rest/api/aiservices/accountmanagement/rai-policies/create-or-update?view=rest-aiservices-accountmanagement-2024-06-01-preview&tabs=HTTP

region = os.getenv("REGION")
token_credential = DefaultAzureCredential()
subscriptionId = os.getenv("SUBSCRIPTION-ID")
resourceGroupName = os.getenv("RESOURCE-GROUP-NAME")
accountName = os.getenv("ACCOUNT-NAME")
raiPolicyName = os.getenv("RAI-POLICY-NAME")
api_version = os.getenv("API-VERSION")

# Get the token
token = token_credential.get_token('https://management.azure.com/.default')
headers = {
    'Authorization': 'Bearer ' + token.token,
    'Content-Type': 'application/json'
}

# URL for the RAI policy
url = f"https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/raiPolicies/{raiPolicyName}?api-version={api_version}"

# Fetch the existing policy
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Original Policy:")
    print(json.dumps(data, indent=4))

    # Enable all filters in the contentFilters list
    for filter_item in data["properties"]["contentFilters"]:
        filter_item["enabled"] = True
        filter_item["blocking"] = True  # Set this to True if you want to enforce blocking
        filter_item["severityThreshold"] = "Medium"  # Adjust as necessary

    # Prepare the body for the PUT request
    body = {
        "properties": {
            "type": data["properties"]["type"],
            "mode": data["properties"]["mode"],
            "basePolicyName": data["properties"]["basePolicyName"],
            "contentFilters": data["properties"]["contentFilters"]
        }
    }

    # Send the updated policy back to the server
    put_response = requests.put(url, headers=headers, json=body)

    if put_response.status_code == 200 or put_response.status_code == 201:
        updated_data = put_response.json()
        print("Updated Policy:")
        print(json.dumps(updated_data, indent=4))
    else:
        print(f"Error updating policy: {put_response.status_code} - {put_response.text}")
else:
    print(f"Error fetching policy: {response.status_code} - {response.text}")