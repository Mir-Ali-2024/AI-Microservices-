from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
BASE_URL = 'https://tt-azureopenai-poc.openai.azure.com'

@app.route('/chat/single_response/<deployment_id>', methods=['POST'])
def chat(deployment_id):
    received_body = request.json  # Assuming the body is in JSON format
    
    # Validate the received message format
    if not validate_message_format(received_body):
        transform_payload(received_body)

    # Validate the prompt
    if not prompt_defense(received_body):
        return 'Invalid prompt detected', 400
    
    # Construct the API endpoint URL using the deployment ID
    api_endpoint = f'{BASE_URL}/openai/deployments/{deployment_id}/chat/completions'
    
    # Extract query parameters from the request URL
    api_params = request.args.to_dict()
    print(api_params)
    # Append query parameters to the endpoint URL
    if api_params:
        api_endpoint += '?' + '&'.join([f'{key}={value}' for key, value in api_params.items()])
    
    try:
        response = requests.post(api_endpoint, json=received_body)
        print(response.status_code)
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return 'Failed to send body to API endpoint', response.status_code
    except Exception as e:
        return f'Error occurred: {str(e)}', 500


def prompt_defense(received_body):
    # Placeholder for prompt defense logic
    return True

"""
    Validates if a message adheres to the expected format.
    Returns True if the format is correct, False otherwise.
    """
def validate_message_format(message):
    
    if not isinstance(message, dict):
        return False
    if "role" not in message or "content" not in message:
        return False
    if not isinstance(message["role"], str) or not isinstance(message["content"], str):
        return False
    return True

"""
If the senders payload is not correclty formated it puts it into the correct format
"""
def transform_payload(received_body):
    # Transform the received payload to the required format
    transformed_payload = {
        "messages": [
            {
                "role": "user",
                "content": received_body["prompt"]  # Assuming the prompt is stored under the key "prompt"
            }
        ]
    }
    return transformed_payload



if __name__ == '__main__':
    app.run(debug=True)
