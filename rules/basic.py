from .rule import Rule

class HelloRule(Rule):
    def match_expr(self):
        return (r'(H(i|ello)|安安|[你妳]好|哈囉|嗨)',)

    def run(self, message, **kwargs):
        return '嗨 {}，我是黑熊莉絲。'.format(message.from_user.username)

class FallbackRule(Rule):
    def match(self, message):
        return self.run(message)

    def run(self, message, **kwargs):
        return '我不太清楚你說什麼哦～\n如果不知道要問些什麼，可以問我「你可以做什麼？」'

class HelpRule(Rule):
    def match_expr(self):
        return (r'[你妳](能|可以|會).*([做幹]|幫.*)(什麼|嘛|啥)',)

    def run(self, message, **kwargs):
        return '你可以跟我說「我說⋯⋯你就說⋯⋯」，我就會記在我的小本本上。'
