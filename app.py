#!/usr/bin/env python3
import codecs
import facebook
import hmac
import io
import json
import logging
import os
import rules
from bottle import Bottle, request, route, run, abort

# Config
VERIFY_TOKEN = os.environ.get('JRF_VERIFY_TOKEN')
APP_SECRET = os.environ.get('JRF_APP_SECRET')

# Variables
app = Bottle()
logger = logging.getLogger('bot')
rules = [
    rules.TimeRule(),
    rules.HelpRule(),
    rules.SearchRule(),
    rules.TeachDialogRule(),
    rules.DialogRule(),
    rules.HelloRule(),
    rules.FallbackRule(),
]

# Configure logger
log_path = os.path.join(os.environ.get('LOGDIR', '.'), 'jrf_bot.log')
logging.basicConfig(filename=log_path, level=logging.DEBUG)

@app.route('/hooks/messenger')
def verification_hook():
    if request.query.get('hub.verify_token') == VERIFY_TOKEN:
        return request.query.get('hub.challenge')
    else:
        return abort(400, 'Token illegal')

@app.post('/hooks/messenger')
def messenger_hook():
    try:
        reader = codecs.getreader('utf-8')
        entity = json.load(reader(request.body))
    except json.JSONDecodeError:
        logger.warning('Malformed JSON received')
        logger.debug(request.body.read().decode('latin1'))
        return  # Malformed JSON

    if not check_signature():
        pass #return abort(400, 'Invalid request')

    messages = []
    for entry_dict in entity['entry']:
        for message_dict in entry_dict['messaging']:
            message = facebook.parse_message(message_dict)
            messages.append(message)
            logger.debug(str(message))

    for message in filter(None, messages):
        for rule in rules:
            text = rule.match(message)
            if text:
                facebook.send_message(message.sender, text)
                break

def check_signature():
    signature = request.get_header('X-Hub-Signature')
    logger.debug('Signature [%s]', signature)
    if not signature.startswith('sha1='):
        logger.warning('Signature method invalid')
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
    h = hmac.new(APP_SECRET.encode(), buf.getbuffer(), 'sha1').hexdigest().lower()
    logger.debug('Calculated signature [%s]', h)
    return hmac.compare_digest(h, signature[4:])

if __name__ == '__main__':
    app.run()
