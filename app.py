import os
from bottle import request, route, run

VERIFY_TOKEN = os.environ.get('JRF_VERIFY_TOKEN')

@route('/hooks/messenger')
def messenger_hook():
    if request.query.get('hub.verify_token' == VERIFY_TOKEN):
        return request.query.get('hub.challenge')
    else:
        return 'Procedure illegal'

if __name__ = '__main__':
    run(host='localhost', port=6000)
