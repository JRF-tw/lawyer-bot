import json
import os
import random
import peewee as p
from .rule import Rule

SUPERVISORS = []
DIALOGUES = {}
DATABASE = p.SqliteDatabase('bot.db')

class User(p.Model):
    user_id = p.CharField(max_length=64, unique=True)
    is_admin = p.BooleanField(default=False)

class Match(p.Model):
    keyword = p.CharField(max_length=32)
    answer = p.TextField()
    class Meta:
        database = DATABASE

DATABASE.connect()
User.create_table(fail_silently=True)
for user in User.select().where(User.is_admin == True):
    SUPERVISORS.append(user.user_id)

Match.create_table(fail_silently=True)
for match in Match.select():
    answers = DIALOGUES.get(match.keyword, [])
    answers.append(match.answer)
    DIALOGUES[match.keyword] = answers

class TeachDialogRule(Rule):
    def match_expr(self):
        return (r'我(如果|若|一旦)?(說|講|提到)\s*「?(?P<keyword>.+?)」?，?\s*你就?要?(說|講|大喊)\s*「?(?P<answer>.+?)」?\s*$',)

    def run(self, message, keyword, answer, **kwargs):
        if message.sender not in SUPERVISORS:
            print('User', message.sender, 'triggered training but rejected')
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
