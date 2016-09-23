#!/usr/bin/env python3
import facebook
import hmac
import io
import os
import rules
from bottle import Bottle, request, route, run, abort

# Config
VERIFY_TOKEN = os.environ.get('JRF_VERIFY_TOKEN')
APP_SECRET = os.environ.get('JRF_APP_SECRET')

# Variables
app = Bottle()
rules = [
    rules.TimeRule(),
    rules.HelpRule(),
    rules.SearchRule(),
    rules.TeachDialogRule(),
    rules.DialogRule(),
    rules.HelloRule(),
    rules.FallbackRule(),
]

@app.route('/hooks/messenger')
def verification_hook():
    if request.query.get('hub.verify_token') == VERIFY_TOKEN:
        return request.query.get('hub.challenge')
    else:
        return abort(400, 'Token illegal')

@app.post('/hooks/messenger')
def messenger_hook():
    if not check_signature:
        return abort(400, 'Invalid request')

    messages = []
    try:
        for entry_dict in request.json['entry']:
            for message_dict in entry_dict['messaging']:
                message = facebook.parse_message(message_dict)
                messages.append(message)
    except KeyError:
        pass

    for message in filter(messages, None):
        for rule in rules:
            text = rule.match(message)
            if text:
                facebook.send_message(message.sender, text)
            break

def check_signature():
    signature = request.get_header('X-Hub-Signature')
    if not signature.startswith('sha1='):
        return False

    # Read and encode non-ASCII string
    buf = io.BytesIO()
    with io.TextIOWrapper(request.body, newline='') as reader:
        c = reader.read(1)
        value = ord(c)
        if value > 127:
            buf.write(r'\u{:04x}'.format(value).encode())
        else:
            buf.write(c.encode())

    # Hash it
    h = hmac.new(APP_SECRET.encode(), buf, 'sha1').hexdigest().lower()
    return hmac.compare_digest(h, signature[4:])

if __name__ == '__main__':
    app.run()
