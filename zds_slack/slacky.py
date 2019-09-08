from zds_slack import *


class CustomSlackBot():
    """
    Custom Slack Bot.
    """

    def __init__(
        self,
        slack_token,
        path_to_responses='responses',
    ):
        """
        Initializes a custom Slack bot.

        Args:
            slack_token (str) : security token to grant the bot access to the 
                workspace. You can find it under 
                [slack api](https://api.slack.com/apps/) inside the 
                <kbd> Install App </kbd> > ``Bot User OAuth Access Token``.
        """

        self.slack_token = slack_token

        self.RTMClient = slack.RTMClient(token=slack_token)

        # self.send_scheduled_msg()

    def start(self):
        """
        Starts the Client.
        """

        self.RTMClient.start()

    def send_scheduled_msg(self):
        """
        Sends a scheduled message.
        """

        import datetime

        now = datetime.datetime.now().timestamp()
        schedule_time = now + 10
        
        self.RTMClient.chat_scheduleMessage(
            channel='CN1JTR2Q7',
            text='Hora do Bolo! :tada:',
            post_at=schedule_time,
        )

    @slack.RTMClient.run_on(event='message')
    def answer_message(**payload):
        """
        Answers a message sent to the channel.
        """

        path_to_responses = 'responses'
        msgs_handler = MsgsHandler(subfolder=path_to_responses)
        msgs_dict = msgs_handler.msgs_dict

        data = payload['data']
        web_client = payload['web_client']
        rtm_client = payload['rtm_client']
        channel_id = data['channel']
        thread_ts = data['ts']
        text = data['text'].lower()

        if all (key in data for key in ('text', 'user')):

            user = data['user']

            if 'novat' in data['text']:

                response_message = msgs_dict['novat'].replace(
                    'user', 
                    user,
                )

            elif 'cafe' in data['text']:

                response_message = msgs_dict['cafe']

            elif 'cotacoes' in data['text']:

                cotacoes = 100

                response_message = msgs_dict['cotacoes'].replace(
                    'cotacoes', 
                    str(cotacoes),
                )

            elif 'senha' in data['text']:

                response_message = msgs_dict['senha']

            else:

                response_message = msgs_dict['else']

            post_message(
                web_client=web_client,
                channel=channel_id if 'senha' not in text else user,
                text=response_message,
            )

    @slack.RTMClient.run_on(event='message')
    def send_scheduled_message(**payload):
        """
        Envia uma mensagem         
        """

        path_to_responses = 'scheduled'
        msgs_handler = MsgsHandler(subfolder=path_to_responses)
        msgs_dict = msgs_handler.msgs_dict

        data = payload['data']
        web_client = payload['web_client']
        rtm_client = payload['rtm_client']
        channel_id = data['channel']
        thread_ts = data['ts']
        text = data['text'].lower()

        response_message = msgs_dict['bolo']

        now = datetime.datetime.now().timestamp()
        scheduled_time = now + 15

        if all (key in data for key in ('text', 'user')):

            user = data['user']

            if 'senha' in text:

                web_client.chat_scheduleMessage(
                    channel=channel_id,
                    post_at=scheduled_time,
                    text=response_message,
                )


def post_message(
    web_client,
    channel,
    text,
):
    """
    POSTs a message with the Slack Client.
    """

    web_client.chat_postMessage(
        channel=channel,
        text=text,
    )


class MsgsHandler():
    """
    Manages the *response messages*.
    """

    def __init__(
        self,
        subfolder,  
    ):
        """
        Initialization.
        """

        self.path_to_msgs = 'data/msgs'
        self.subfolder = subfolder
        self.complete_path_to_msgs = os.path.join(
            self.path_to_msgs,
            self.subfolder,
        )

        self.files = [
            [dirpath, dirnames, filenames]
            for dirpath, dirnames, filenames 
            in os.walk(self.complete_path_to_msgs)
        ]

    @property
    def msgs_dict(self):
        """
        Puts the messages into a dictionary.
        """

        msgs_dict = {}
        for msg_file in self.files[0][2]:

            path_to_msg_file = os.path.join(
                self.complete_path_to_msgs, 
                msg_file
            )
            msg_file_name_without_ext = os.path.splitext(msg_file)[0]
            with open(path_to_msg_file, 'r') as f:
                msgs_dict[msg_file_name_without_ext] = f.read()

        return msgs_dict