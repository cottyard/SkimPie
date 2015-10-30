def primitive_add(args):
    result = 0
    for a in args:
        result += a
    return result

def primitive_multiply(args):
    result = 1
    for a in args:
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

built_ins = {
    '+': primitive_add,
    '*': primitive_multiply,
    '==': primitive_equal,
    '<=': primitive_less_than
}

class Environment:
    def __init__(self, dict, parent=None):
        self.env = dict
        self.parent = parent

    def lookup(self, symbol):
        return self.env[symbol] if symbol in self.env else self.parent.lookup(symbol)

global_env = Environment(built_ins)
