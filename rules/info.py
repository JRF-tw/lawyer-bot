from datetime import datetime
from .rule import Rule

class TimeRule(Rule):
    def match_expr(self):
        return (r'現在.*(時間|幾點|日期)', r'今天.*(幾[月號]|第幾天)')

    def run(self, bot, message, **kwargs):
        now = datetime.now()
        return '齁齁，現在的時間是 {:%Y/%m/%d %H:%M}。'.format(now, term, days)
