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

        Args:
            slack_token (str) : security token to grant the bot access to the 
                workspace. You can find it under 
                [slack api](https://api.slack.com/apps/) inside the 
                <kbd> Install App </kbd> > ``Bot User OAuth Access Token``.
        """

        self.slack_token = slack_token

        self.RTMClient = slack.RTMClient(token=slack_token)

    def start(self):
        """
        Starts the Client.
        """

        self.RTMClient.start()

    @slack.RTMClient.run_on(event='message')
    def answer_message(**payload):
        """
        Answers a message sent to the channel.
        """

        data = payload['data']
        web_client = payload['web_client']
        rtm_client = payload['rtm_client']
        channel_id = data['channel']
        thread_ts = data['ts']

        text = data['text'].lower()

        if all (key in data for key in ('text', 'user')):

            user = data['user']

            if 'novat' in data['text']:

                response_message = f"""
                Olá <@{user}>! Bem-vindo à Zanthus! :tada:

                Sugiro que você comece por aqui:

                1. Portal de Documentação da Zanthus: 
                2. Como funciona o PDV da Zanthus?
                3. Como funciona o workflow com o Jira?
                4. Onde estão os códigos de lançamentos dos mísseis nucleares?
                """

            elif 'cafe' in data['text']:

                response_message = f"""
                Há café feito:

                1. Por Máquina.
                2. Pela Didi.
                """

            elif 'cotacoes' in data['text']:

                cotacoes = 100

                response_message = f"""
                Na maioria dos casos, a cotação acaba sendo:

                R$ {cotacoes} / PDV
                """

            # elif 'senha' in data['text']:

                # Talvez criar algum atributo para mensagens privadas?

            else:

                response_message = f"""
                Desculpe, mas eu não sei te responder! :persevere:
                """

            web_client.chat_postMessage(
                channel=channel_id,
                text=response_message,
                # thread_ts=thread_ts,
            )