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

built_ins = {
    '+': primitive_add,
    '-': primitive_substract,
    '*': primitive_multiply,
    '=': primitive_equal,
    '<=': primitive_less_than,
    'cons': primitive_cons,
    'car': primitive_car,
    'cdr': primitive_cdr,
    'list': primitive_list,
    'begin': primitive_begin
}

class UnresolvedSymbolError(BaseException):
    pass

class Environment:
    def __init__(self, dict, parent=None):
        self.env = dict
        self.parent = parent

    def lookup(self, symbol):
        if symbol in self.env:
            return self.env[symbol]
        else:
            if self.parent is None:
                raise UnresolvedSymbolError(symbol)
            return self.parent.lookup(symbol)

    def set(self, name, value):
        self.env[name] = value

    def nested(self):
        return Environment({}, self)

    def __str__(self):
        return str(self.env)

global_env = Environment(built_ins)
