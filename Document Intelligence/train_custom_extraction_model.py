from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
import os
from dotenv import load_dotenv
load_dotenv()

endpoint = "https://<my-custom-subdomain>.cognitiveservices.azure.com/"
credential = AzureKeyCredential(os.getenv("api_key"))
document_intelligence_client = DocumentIntelligenceClient(endpoint, credential)