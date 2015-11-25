def apply(proc, args, env):
    if isinstance(proc, Procedure):
        args = [delay(arg, env) for arg in args]
    else:
        args = [force(arg.eval(env)) for arg in args]
    return proc(args)


class Procedure:
    def __init__(self, params, body, env):
        self.params = params
        self.body = body
        self.env = env

    def __repr__(self):
        return "<proc object>"

    def __call__(self, args):
        env = self.env.nested()

        for symbol, value in zip(self.params, args):
            env.set(symbol.value, value)

        for expression in self.body[:-1]:
            expression.eval(env)

        return self.body[-1].eval(env)


def force(obj):
    if isinstance(obj, Thunk):
        return force(obj.get_value())
    else:
        return obj


def delay(exp, env):
    return Thunk(exp, env)


class Thunk:
    def __init__(self, exp, env):
        self.exp = exp
        self.env = env
        self.evaluated = False
        self.value = None

    def get_value(self):
        if not self.evaluated:
            self.value = self.exp.eval(self.env)
            self.evaluated = True
            self.exp = None
            self.env = None
        return self.value
