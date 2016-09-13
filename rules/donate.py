from datetime import datetime
from .rule import Rule

class DonateRule(Rule):
    def match_expr(self):
        return (r'我想.*(小額|捐款|支持|贊助|參加募款餐會).*')

    def run(self, message, **kwargs):
        if re.search('募款餐會', message):
            return '歡迎參加司改會於10月1日舉辦的募款餐會！請點此購買餐卷：\nhttps://donate.jrf.org.tw'
        else if re.search('小額', message):
            return '歡迎定期定額贊助司改會！請點：\nhttps://www.jrf.org.tw/donate'
        else if re.search('發票', message):
            return '司改會的電子發票代碼是「948」，諧音「救司法」，歡迎在結帳的時候使用，把發票寄給我們喔！'
        else
            return '歡迎捐款贊助司改會喔！請點：\nhttps://donate.jrf.org.tw'
