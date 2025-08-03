import requests
import os

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account 
API_KEY = os.environ.get("<your API key>")
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE:  manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"messages":[{"content":"","role":""}]}

response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/b897efbd-83c9-47b1-80cd-ead3b31eeafc/ai_service_stream?version=2021-05-01', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})

print("Scoring response")
try:
    print(response_scoring.json())
except ValueError:
    print(response_scoring.text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")