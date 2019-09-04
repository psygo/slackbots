import os

import slackclient as slack


# slack_token = os.environ["SLACK_API_TOKEN"]
slack_token = 'xoxb-749639846231-747790262928-bJDd2KiPU5yxxyYVgactPCUo'

client = slack.SlackClient(token=slack_token)

# Check the Connection:
is_connected = client.rtm_connect(with_team_state=False)
print('Are we connected? ', is_connected)

response = client.chat_postMessage(
    channel='#random',
    text='Hello World!',
)

assert response['ok']
assert response['message']['test'] == 'Hello World!'