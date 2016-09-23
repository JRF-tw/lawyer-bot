import os
import requests
from datetime import datetime

PAGE_ACCESS_TOKEN = os.environ.get('JRF_PAGE_ACCESS_TOKEN')
API_BASE_URL = 'https://graph.facebook.com/v2.6'

class Message(object):
    def __init__(self, sender=None, recipient=None, timestamp=None, text=None):
        self.sender = sender
        self.recipient = recipient
        self.timestamp = timestamp
        self.text = text

    def __str__(self):
        return "Message(sender='{sender}', text='{text}')".format(**self.__dict__)

def send_message(recipient, message):
    api_url = '{}/me/messages?access_token={}'.format(API_BASE_URL, PAGE_ACCESS_TOKEN)
    entity = {}

    if type(recipient) is str:
        entity['recipient'] = { 'id': recipient }
    else:
        entity['recipient'] = recipient

    if type(message) is str:
        entity['message'] = { 'text': message }
    else:
        entity['message'] = message

    return requests.post(url=api_url, json=entity)

def parse_message(entity):
    try:
        return Message(
            sender=entity['sender']['id'],
            recipient=entity['recipient']['id'],
            timestamp=datetime.fromtimestamp(entity['timestamp'] / 1000.0),
            text=entity['message']['text'])
    except KeyError:
        return None
