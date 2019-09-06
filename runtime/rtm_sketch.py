import os

import slack


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    """
    Says hello to user.
    """

    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']

    if (
        'text' in data.keys() and 
        'Hello' in data['text']
    ):

        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",
            thread_ts=thread_ts,
        )


# Runtime

# slack_token = os.environ["SLACK_API_TOKEN"]
slack_token = 'xoxb-749639846231-747790262928-sokP07h7DCpbtYq6NS6WeI0T'

rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()