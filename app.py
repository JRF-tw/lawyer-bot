#!/usr/bin/env python3
import os
from bottle import Bottle, request, route, run

# Config
VERIFY_TOKEN = os.environ.get('JRF_VERIFY_TOKEN')

# Variables
app = Bottle()

@app.route('/hooks/messenger')
def messenger_hook():
    if request.query.get('hub.verify_token' == VERIFY_TOKEN):
        return request.query.get('hub.challenge')
    else:
        return 'Procedure illegal'

if __name__ = '__main__':
    app.run()
