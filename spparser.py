def parse(tokens):
    def parse_exp():
        nonlocal head
        if tokens[head] == ')':
            raise SyntaxError('unexpected )')

        if tokens[head] == '(':
            head += 1
            exp = []
            while tokens[head] != ')':
                exp.append(parse_exp())
            head += 1
            return exp
        else:
            head += 1
            return tokens[head - 1]

    head = 0
    return parse_exp()


class SyntaxError(Exception):
    pass
