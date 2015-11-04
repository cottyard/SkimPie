class PieException(Exception):
    pass


class PieSyntaxError(PieException):
    def __init__(self, msg, tokens, head):
        source = ' '.join(tokens)
        loc = sum((len(t) for t in tokens[:head])) + head
        loc_str = ' ' * loc + '~'
        self._message = '%s\n%s\n%s\n' % (msg, source, loc_str)

    def __str__(self):
        return self._message


class PieUnresolvedSymbolError(PieException):
    pass