import os

import slack

from zds_slack.slacky import (
    CustomSlackBot,
)


slack_token = os.environ["SLACK_API_TOKEN"]