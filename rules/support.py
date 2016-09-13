from datetime import datetime
from .rule import Rule

class SupportRule(Rule):
    def match_expr(self):
        return (r'我想.*(參與|志工|義務).*')

    def run(self, message, **kwargs):
        return '歡迎你一起來參與司法改革！\n如果您是律師，歡迎報名義務律師，參與專案：\nhttps://jrf.neticrm.tw/civicrm/profile/create?gid=34&reset=1\n如果您想參與志工，也可以填寫志工表單：\nhttps://jrf.neticrm.tw/civicrm/profile/create?gid=11&reset=1\n歡迎你加入司改會！'
