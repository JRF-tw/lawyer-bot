import json
import logging
import os
import random
from .rule import Rule
from models import User, Match, create_tables

DIALOGUES = {}
logger = logging.getLogger('bot')

for match in Match.select():
    answers = DIALOGUES.get(match.keyword, [])
    answers.append(match.answer)
    DIALOGUES[match.keyword] = answers

class TeachDialogRule(Rule):
    def __init__(self):
        super().__init__()
        self.supervisors = [user.user_id for user in User.select().where(User.is_admin == True)]

    def match_expr(self):
        return (r'我(如果|若|一旦)?(說|講|提到)\s*「?(?P<keyword>.+?)」?，?\s*你就?要?(說|講|大喊)\s*「?(?P<answer>.+?)」?\s*$',)

    def run(self, message, keyword, answer, **kwargs):
        if message.sender not in SUPERVISORS:
            logger.warning('User %s triggered training but rejected', message.sender)
            return None

        if keyword in DIALOGUES:
            DIALOGUES[keyword].append(answer)
        else:
            DIALOGUES[keyword] = [answer]

        match = Match(keyword=keyword, answer=answer)
        match.save()
        print(keyword, answer)

        return random.choice((
            '好的～',
            '（筆記）',
            '學會了這句，我就可以去選總統了！',
        ))

class DialogRule(Rule):
    def match(self, message):
        for keyword in DIALOGUES.keys():
            if keyword in message.text:
                return self.run(message, keyword=keyword)
        return None

    def run(self, message, keyword, **kwargs):
        return random.choice(DIALOGUES[keyword])
