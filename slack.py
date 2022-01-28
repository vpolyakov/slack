import json
from urllib import request

from config import SLACK_URL


class SlackSender:
    """
    Создание объекта, который можно использовать для посылки сообщений в Слак через Slack Incoming Webhook.
    """
    def __init__(self, slack_url, username=None, channel=None, icon_emoji=None):
        """
        Initialize the instance with the Slack request URL
        :param slack_url: Slack Incoming Webhook URL
        :param username: (optional) message sender username
        :param channel: (optional) Slack channel to post to
        :param icon_emoji: (optional) customize emoji for message sender.
        """
        self.slack_url = slack_url
        self.username = username
        self.channel = channel
        self.icon_emoji = icon_emoji

    def set_user_name(self, username):
        self.username = username

    def set_channel(self, channel):
        self.channel = channel

    def set_icon_emoji(self, icon_emoji):
        self.icon_emoji = icon_emoji

    def get_user_name(self):
        return self.username

    def get_channel(self):
        return self.channel

    def get_icon_emoji(self):
        return self.icon_emoji

    def get_slack_url(self):
        return self.slack_url

    def send(self, text):
        payload = {
            "text": "{0}".format(text),
            "username": self.username,
            "channel": self.channel,
            "icon_emoji": self.icon_emoji
        }

        json_data = json.dumps(payload)
        req = request.Request(self.slack_url,
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'})
        request.urlopen(req)


if __name__ == '__main__':
    message = 'Hello, World! - тестирование слак хукера'

    slack = SlackSender(slack_url=SLACK_URL, username='Mumbai Server', channel='@vpolyakov', icon_emoji=':warning:')
    slack.send(message)
