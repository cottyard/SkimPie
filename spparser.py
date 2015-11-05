from representation import *
from spexception import *

def is_int(exp):
    try:
        int(exp)
        return True
    except (ValueError, TypeError):
        return False

def is_float(exp):
    try:
        float(exp)
        return True
    except (ValueError, TypeError):
        return False

def is_if(exp):
    return exp[0] == 'if'

def is_quote(exp):
    return exp[0] == 'quote'

def is_define(exp):
    return exp[0] == 'define' and not isinstance(exp[1], list)

def is_defineproc(exp):
    return exp[0] == 'define' and isinstance(exp[1], list)

def is_lambda(exp):
    return exp[0] == 'lambda'

def parse_atom(exp):
    if is_int(exp):
        return Int(exp)
    elif is_float(exp):
        return Float(exp)
    else:
        return Symbol(exp)

def parse_exp(exp):
    if not isinstance(exp, list):
        return parse_atom(exp)
    elif is_if(exp):
        return If(parse_exp(exp[1]), parse_exp(exp[2]), parse_exp(exp[3]))
    elif is_quote(exp):
        return List(exp[1])
    elif is_define(exp):
        return Define(parse_exp(exp[1]), parse_exp(exp[2]))
    elif is_defineproc(exp):
        symbols = list(map(Symbol, exp[1]))
        return DefineProc(symbols[0], symbols[1:], list(map(parse_exp, exp[2:])))
    elif is_lambda(exp):
        return Lambda(list(map(parse_exp, exp[1])), parse_exp(exp[2]))
    else:
        return Application(parse_exp(exp[0]), list(map(parse_exp, exp[1:])))

def read_one_exp(tokens, head=0):
    def read_next_exp():
        nonlocal head
        if tokens[head] == ')':
            raise PieSyntaxError('unexpected )', tokens, head)

        if tokens[head] == '\'':
            head += 1
            return ['quote', read_next_exp()]

        if tokens[head] == '(':
            head += 1
            exp = []
            while head < len(tokens) and tokens[head] != ')':
                exp.append(read_next_exp())
            if head >= len(tokens):
                raise PieSyntaxError('expecting )', tokens, head)
            head += 1
            return exp
        else:
            head += 1
            return tokens[head - 1]

    return read_next_exp(), head

def parse_program(tokens):
    head = 0
    parsed_exps = []
    while head < len(tokens):
        exp, head = read_one_exp(tokens, head)
        parsed_exps.append(parse_exp(exp))
    return Program(parsed_exps)