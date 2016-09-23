import os
import requests
from datetime import datetime

PAGE_ACCESS_TOKEN = os.environ.get('JRF_PAGE_ACCESS_TOKEN')
API_BASE_URL = 'https://graph.facebook.com/v2.6'

class Message(object):
    def __init__(self, **options):
        self.sender = options.get('sender')
        self.recipient = options.get('recipient')
        self.timestamp = options.get('timestamp')
        self.text = options.get('text')

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
        sender = entity['sender']['id']
        recipient = entity['recipient']['id']
        timestamp = datetime.fromtimestamp(entity['timestamp'])
        text = entity['message']['text']
        return Message(sender, recipient, text, timestamp)
    except KeyError:
        return None
