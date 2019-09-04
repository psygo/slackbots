# Initial Configurations

## Setting Up a New Workspace

You can create a new `Workspace` by going to `Window > Sign in to another Workspace` and then using the `...` on the top-righthand corner to find the respective option.

## Creating a New App

In order to make a bot, first you need to get an API token for it. Go to [api.slack.com/apps](https://api.slack.com/apps).

Add a `Bot` type of app.

Once that's done, add it to your Workspace by going to `Basic Information`. Notice that you can see your credentials there too.

## Setting Up the Python Workspace

```bash
pipenv install slackclient

pipenv shell
```

## Setting Up the Bot

The token is **not** the `Verification Token` on the `App Credentials` section.

It's actually the `Bot User OAuth Access Token` under the `OAuth & Permissions` section.

## Useful Links

Slack's Github page seems *extremely outdated*. [This medium tutorial](https://medium.com/alex-attia-blog/build-a-first-simple-slack-bot-with-python-5392ef359835) is *way* better.