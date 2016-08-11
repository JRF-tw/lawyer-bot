import json
import os
import random
from .rule import Rule

DIALOGUES = {}
try:
    with open('dialog.json', 'r') as f:
        DIALOGUES.update(json.load(f))
except IOError:
    pass

class TeachDialogRule(Rule):
    def match_expr(self):
        return (r'我(如果|若|一旦)?(說|講|提到)\s*「?(?P<keyword>.+?)」?，?\s*你就?要?(說|講|大喊)\s*「?(?P<answer>.+?)」?\s*$',)

    def run(self, bot, message, keyword, answer, **kwargs):
        if keyword in DIALOGUES:
            DIALOGUES[keyword].append(answer)
        else:
            DIALOGUES[keyword] = [answer]

        try:
            with open('dialog.json', 'w') as f:
                json.dump(DIALOGUES, f, ensure_ascii=False, indent='\t')
        except IOError:
            pass
        finally:
            print(keyword, answer)

        return random.choice((
            '好的～',
            '（筆記）',
            '學會了這句，我就可以去選總統了！',
        ))

class DialogRule(Rule):
    def match(self, bot, message):
        for keyword in DIALOGUES.keys():
            if keyword in message.text:
                return self.run(bot, message, keyword=keyword)
        return None

    def run(self, bot, message, keyword, **kwargs):
        return random.choice(DIALOGUES[keyword])
