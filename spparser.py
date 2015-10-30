from representation import *

def is_int(exp):
    try:
        int(exp)
        return True
    except (ValueError, TypeError):
        return False

def is_if(exp):
    return exp[0] == 'if'

def is_quote(exp):
    return exp[0] == 'quote'

def is_define(exp):
    return exp[0] == 'define'

def is_lambda(exp):
    return exp[0] == 'lambda'

def parse_atom(exp):
    if is_int(exp):
        return Int(exp)
    else:
        return Symbol(exp)

def parse_exp(exp):
    if not isinstance(exp, list):
        return parse_atom(exp)
    elif is_if(exp):
        return If(parse_exp(exp[1]), parse_exp(exp[2]), parse_exp(exp[3]))
    elif is_quote(exp):
        return Quote(exp[1])
    elif is_define(exp):
        return Define(parse_exp(exp[1]), parse_exp(exp[2]))
    elif is_lambda(exp):
        return Lambda(list(map(parse_exp, exp[1])), parse_exp(exp[2]))
    else:
        return Application(parse_exp(exp[0]), list(map(parse_exp, exp[1:])))

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