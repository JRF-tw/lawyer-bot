from .rule import Rule

class HelloRule(Rule):
    def match_expr(self):
        return (r'(H(i|ello)|安安|[你妳]好|哈囉|嗨)',)

    def run(self, message, **kwargs):
        return '安安，我是黑熊莉絲。'

class FallbackRule(Rule):
    def match(self, message):
        return self.run(message)

    def run(self, message, **kwargs):
        return '我不太清楚你說什麼哦～\n如果不知道要問些什麼，可以問我「你可以做什麼？」'

class HelpRule(Rule):
    def match_expr(self):
        return (r'[你妳](能|可以|會).*([做幹]|幫.*)(什麼|嘛|啥)',)

    def run(self, message, **kwargs):
        return '你可以問我司法問題，你可以說「我要問……」，我就會找文章給你參考喔！\n你也可以說「我要申訴……」，我會跟你說申訴的資訊；\n你也可以支持我們，只要說「我要捐款……」，我會告訴你怎贊助我們喔！'
