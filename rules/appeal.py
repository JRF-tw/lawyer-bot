from datetime import datetime
from .rule import Rule

class AppealRule(Rule):
    def match_expr(self):
        return (r'我.*申訴.*')

    def run(self, message, **kwargs):
        return '若你想申訴檢察官或法官，請參考此網頁資訊：\nhttps://www.jrf.org.tw/keywords/1\n台中請致電 04-23292371 ，其他地區請致電 02-25421958 。\n打電話之前，請先參考網頁資訊喔！'
