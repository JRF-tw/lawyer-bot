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
    from terminaltables import SingleTable

    # Initialize table data
    data = [['keyword', 'answer']]

    # List all matches
    matches = list(Match.select().order_by(Match.keyword, Match.id))
    for match in matches:
        data.append([str(match.keyword), str(match.answer).replace('\n', '↵')[:30]])

    # Create and print table
    table = SingleTable(data)
    table.title = '{} dialogues'.format(len(matches))
    print(table.table)

if __name__ == '__main__':
    method = (sys.argv[1] if len(sys.argv) > 1 else '').lower()
    if method == 'list':
        show_matches()
    else:
        help()
