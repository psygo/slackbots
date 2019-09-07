from zds_slack import *


class CustomSlackBot():
    """
    Custom Slack Bot.
    """

    def __init__(
        self,
        slack_token,
    ):
        """
        Initializes a custom Slack bot.
        """

        self.slack_token = slack_token

        self.RTMClient = slack.RTMClient(token=slack_token)

    def start(self):
        """
        Starts the Client.
        """

        self.RTMClient.start()

    @slack.RTMClient.run_on(event='message')
    def say_hello(**payload):
        """
        Says hello to an user.
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
                # thread_ts=thread_ts,
            )