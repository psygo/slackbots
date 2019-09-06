import os

import slack


# slack_token = os.environ["SLACK_API_TOKEN"]
slack_token = 'xoxb-749639846231-747790262928-lcxHzucYkHidgt8JprSVNt7v'

client = slack.WebClient(token=slack_token)

client.chat_postMessage(
  channel="#random",
  text="Hugo viado."
)