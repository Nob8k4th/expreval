class LexError(Exception):
    pass
class Lexer:
    def tokenize(self, text):
        if '>=' in text:
            raise IndexError('bad token')
        return text.replace('(',' ( ').replace(')',' ) ').split()
