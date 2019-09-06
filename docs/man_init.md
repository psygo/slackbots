# Initial Configurations

## On Tutorials

There has been a lot of updates with respect to the API library, so many tutorials became outdated. It's best to stick to [the official one](https://github.com/slackapi/python-slackclient/tree/master/tutorial).

Other useful tutorials:

- [Traversy Media](https://youtu.be/nyyXTIL3Hkw)
- [Will Hieronymus's Python Slack Bot](https://youtu.be/tg1OoneCc_s)
- [Matt Makai's Full Stack Tutorial](https://youtu.be/tg1OoneCc_s)
- [Alexandre Attia's Medium Tutorial](https://medium.com/alex-attia-blog/build-a-first-simple-slack-bot-with-python-5392ef359835) (a bit outdated and not very well formatted)

[Paul Asjes's Building Slack Bots book](https://www.amazon.com/dp/B01ENNEMBW/ref=nav_timeline_asin?_encoding=UTF8&psc=1) is also another great resource, though it's written in `JavaScript`.

[SlackAPI HQ](https://github.com/slackapi) is a must-stop also.

## Setting Up a New Workspace

You can create a new `Workspace` by going to `Window > Sign in to another Workspace` and then using the `...` on the top-righthand corner to find the respective option.

## Creating a New App

In order to make a bot, first you need to get an API token for it. Go to [api.slack.com/apps](https://api.slack.com/apps).

Add a `Bot` type of app.

Once that's done, add it to your Workspace by going to `Basic Information`. Notice that you can see your credentials there too.

## Setting Up the Python Workspace

Note that you should use `python3`'s version of the library, which is way more stable. Please follow the recommendations found in [the official Github repo](https://github.com/slackapi/python-slackclient).

```bash
pipenv shell

pip3 install slackclient
```

## Setting Up the Bot

The token is **not** the `Verification Token` on the `App Credentials` section.

It's actually the `Bot User OAuth Access Token` under the ~~`OAuth & Permissions`~~ `Basic Information` section.

## Useful Links

Slack's Github page seems *extremely outdated*. [This medium tutorial](https://medium.com/alex-attia-blog/build-a-first-simple-slack-bot-with-python-5392ef359835) is *way* better.