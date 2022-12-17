# Example 2: Adds user input.

from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Create Assistant service object.
authenticator = IAMAuthenticator('HvqisECsNQkJaxZHI6g2nvE12y97iOGPAqO7v5sWdkzG') # replace with API key
assistant = AssistantV2(
    version = '2021-11-27',
    authenticator = authenticator
)
assistant.set_service_url('https://api.us-east.assistant.watson.cloud.ibm.com/instances/7100bdb5-2ea0-4626-9a32-e44f8fabf720') # replace with service instance URL
assistant_id = '49c310ef-cb26-4b4a-a66f-1ce40ec7892a' # replace with environment ID

# Initialize with empty value to start the conversation.
message_input = {
    'message_type:': 'text',
    'text': ''
    }

# Main input/output loop
while message_input['text'] != 'quit' or message_input['text'] != 'exit':

    # Send message to assistant.
    result = assistant.message_stateless(
        assistant_id,
        input = message_input
    ).get_result()


    # Print responses from actions, if any. Supports only text responses.
    if result['output']['generic']:
        for response in result['output']['generic']:
            if response['response_type'] == 'text':
                print(response['text'])

    # Prompt for the next round of input unless skip_user_input is True.
    if not result['context']['global']['system'].get('skip_user_input', False):
        user_input = input('>> ')
        message_input = {
            'text': user_input
        }