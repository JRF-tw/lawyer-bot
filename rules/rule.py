import re

'''
Base class for bot rules.
'''
class Rule(object):
    '''
    Check if a rule applies and `run()` the rule; return `None` otherwise.
    '''
    def match(self, message):
        for expr in self.match_expr():
            m = re.search(expr, message.text)
            if m:
                return self.run(message, **m.groupdict())
        return None

    '''
    Return a set of regular expression rules. In default implementation of
    `match()`, the returning value will be used to determine whether the rule
    applies, while extract `run()` arguments from named groups.
    '''
    def match_expr(self):
        raise NotImplementedError

    '''
    Executes the rule.
    '''
    def run(self, message, **kwargs):
        pass
