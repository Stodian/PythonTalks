import json
import requests

def lambda_handler(event, context):
    # Replace with your smart lock API endpoint and key
    smart_lock_api_url = "https://api.smartlockprovider.com/lock"
    api_key = "YOUR_API_KEY"
    
    # Make the API request to lock the door
    response = requests.post(
        smart_lock_api_url,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"command": "lock"}
    )
    
    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': json.dumps('Door locked successfully!')
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': json.dumps('Failed to lock the door.')
        }
