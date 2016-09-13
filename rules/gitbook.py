from datetime import datetime
from .rule import Rule

class GitbookRule(Rule):
    def match_expr(self):
        return (r'我想.*(看書|電子書|閱讀).*')

    def run(self, message, **kwargs):
        return '想看司改會出的書，可以來這裡喔：\nhttps://www.gitbook.com/@jrf-tw'
