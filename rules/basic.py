from .rule import Rule

class HelloRule(Rule):
    def match_expr(self):
        return (r'(H(i|ello)|安安|[你妳]好|哈囉|嗨)',)

    def run(self, message, **kwargs):
        return '嗨，我是黑熊莉絲 ʕ •ᴥ•ʔ'

class FallbackRule(Rule):
    def match(self, message):
        return self.run(message)

    def run(self, message, **kwargs):
        return '我不太清楚你說什麼哦～\n如果不知道要問些什麼，可以問我「你可以做什麼？」'

class HelpRule(Rule):
    def match_expr(self):
        return (r'[你妳](能|可以|會).*([做幹]|幫.*)(什麼|嘛|啥)',)

    def run(self, message, **kwargs):
        return '''我是司改會的小夥伴黑熊莉絲～

你可以問我問題，我會盡力的從司改會的網站找資料，只要說「我要問」、「我想問」就可以了！
當然像是案件申訴、捐款資訊，我也都略知一二哦！

一起打造人民信賴的司法！ ʕ •ᴥ•ʔ'''
