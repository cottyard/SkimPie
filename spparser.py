# data

class Int:
    def __init__(self, exp):
        self.value = int(exp)

    def __str__(self):
        return str(self.value)

def is_int(exp):
    try:
        int(exp)
        return True
    except (ValueError, TypeError):
        return False

class Symbol:
    def __init__(self, exp):
        self.value = exp

    def __str__(self):
        return self.value

# expressions

def is_if(exp):
    return exp[0] == 'if'

class If:
    def __init__(self, exp):
        self.cond = parse_exp(exp[1])
        self.when_true = parse_exp(exp[2])
        self.when_false = parse_exp(exp[3])

    def __str__(self):
        return 'if (%s) then (%s) else (%s)' % (
            str(self.cond), str(self.when_true), str(self.when_false))

class Application:
    def __init__(self, exp):
        self.proc = parse_exp(exp[0])
        self.args = list(map(parse_exp, exp[1:]))

    def __str__(self):
        return '(%s)(%s)' % (
            str(self.proc), ', '.join(list(map(str, self.args))))

def parse_atom(exp):
    if is_int(exp):
        return Int(exp)
    else:
        return Symbol(exp)

def parse_exp(exp):
    if not isinstance(exp, list):
        return parse_atom(exp)
    elif is_if(exp):
        return If(exp)
    else:
        return Application(exp)

def parse_to_exp(tokens):
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

def parse(tokens):
    return parse_exp(parse_to_exp(tokens))