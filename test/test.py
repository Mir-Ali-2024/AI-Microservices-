import requests
import json

def make_post_request(api_url, custom_header, json_body):
    headers = {'Custom-Header': custom_header, 'Content-Type': 'application/json'}
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(json_body))
        if response.status_code == 200:
            print("Request successful!")
            print("Response:")
            print(response.json())
        else:
            print("Request failed with status code:", response.status_code)
            print("Response:")
            print(response.text)
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
api_url = 'https://example.com/api/endpoint'
custom_header = 'CustomHeaderValue'
json_body = {'key1': 'value1', 'key2': 'value2'}

make_post_request(api_url, custom_header, json_body)
