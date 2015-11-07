from spexception import *


def primitive_add(args):
    result = args[0]
    for a in args[1:]:
        result += a
    return result


def primitive_substract(args):
    result = args[0]
    for a in args[1:]:
        result -= a
    return result


def primitive_multiply(args):
    result = args[0]
    for a in args[1:]:
        result *= a
    return result


def primitive_divide(args):
    result = args[0]
    for a in args[1:]:
        result /= a
    return result


def primitive_mod(args):
    assert len(args) == 2
    n1, n2 = args
    return n1 % n2


def primitive_equal(args):
    a0 = args[0]
    for a1 in args[1:]:
        if not a0 == a1:
            return False
        a0 = a1
    return True


def primitive_less_than(args):
    a0 = args[0]
    for a1 in args[1:]:
        if not a0 <= a1:
            return False
        a0 = a1
    return True


def primitive_cons(args):
    exp, s_exp = args
    return [exp] + s_exp


def primitive_car(args):
    s_exp = args[0]
    return s_exp[0]


def primitive_cdr(args):
    s_exp = args[0]
    return s_exp[1:]


def primitive_list(args):
    return list(args)


def primitive_begin(args):
    return args[-1]


def primitive_exit(args):
    exit(0)

built_ins = {
    '+': primitive_add,
    '-': primitive_substract,
    '*': primitive_multiply,
    '/': primitive_divide,
    'mod': primitive_mod,
    '=': primitive_equal,
    'eq?': primitive_equal,
    '<=': primitive_less_than,
    'cons': primitive_cons,
    'car': primitive_car,
    'cdr': primitive_cdr,
    'list': primitive_list,
    'begin': primitive_begin,
    'exit': primitive_exit
}


class Environment:
    def __init__(self, dict, parent=None):
        self.env = dict
        self.parent = parent

    def lookup(self, symbol):
        return self.find_env(symbol)[symbol]

    def find_env(self, symbol):
        if symbol in self.env:
            return self.env
        else:
            if self.parent is None:
                raise PieUnresolvedSymbolError(symbol)
            return self.parent.find_env(symbol)

    def set(self, name, value):
        self.env[name] = value

    def nested(self):
        return Environment({}, self)

    def __str__(self):
        return str(self.env)

