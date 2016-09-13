from datetime import datetime
from .rule import Rule

class NewsletterRule(Rule):
    def match_expr(self):
        return (r'我想.*(電子報|訂閱).*')

    def run(self, message, **kwargs):
        return '訂閱司改會電子報請往這邊走：\nhttps://jrf.neticrm.tw/civicrm/profile/create?gid=12&reset=1'
