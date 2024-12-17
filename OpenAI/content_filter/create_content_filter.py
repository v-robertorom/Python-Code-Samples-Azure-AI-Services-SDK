import requests
import json
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv
load_dotenv()

# Azure configurations
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

    # Add a new content filter with all filters disabled
    new_filter = {
        "name": "NewFilterName",
        "severityThreshold": "Low",  # You can adjust this value as needed
        "blocking": False,  # Disabled
        "enabled": False,   # Disabled
        "source": "Prompt"
    }

    # Add the new filter to the existing list of content filters
    data["properties"]["contentFilters"].append(new_filter)

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
        print("Updated Policy with New Content Filter:")
        print(json.dumps(updated_data, indent=4))
    else:
        print(f"Error updating policy: {put_response.status_code} - {put_response.text}")
else:
    print(f"Error fetching policy: {response.status_code} - {response.text}")
