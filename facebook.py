import os
import requests

PAGE_ACCESS_TOKEN = os.environ.get('JRF_PAGE_ACCESS_TOKEN')
API_BASE_URL = 'https://graph.facebook.com/v2.6'

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
