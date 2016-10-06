#!/usr/bin/env python
import os
import sys

def help():
    print("""
dbtool.py - Database utility

Commands:
    list    List all dialogues.
    help    Show this message.

Project homepage:
    https://github.com/jrf-tw/lawyer-bot
    """)

def show_matches():
    from models import Match

    # Define column width
    keyword_width, answer_width = 10, 40
    full_width = (keyword_width + answer_width + 7)

    # Print column header
    print('-' * full_width)
    print('|', 'keyword'.ljust(keyword_width), '|', 'answer'.ljust(answer_width), '|', sep=' ')
    print('-' * full_width)

    # List all matches
    matches = list(Match.select().order_by(Match.keyword, Match.id))
    for match in matches:
        print('|', str(match.keyword)[:keyword_width // 2].ljust(keyword_width // 2, '　'),
              '|', str(match.answer)[:answer_width // 2].replace('\n', '↵').ljust(answer_width // 2, '　'), '|', sep=' ')

    # Print footer and total
    print('-' * full_width)
    print()
    print('{} dialogues.'.format(len(matches)))

if __name__ == '__main__':
    method = (sys.argv[1] if len(sys.argv) > 1 else '').lower()
    if method == 'list':
        show_matches()
    else:
        help()
