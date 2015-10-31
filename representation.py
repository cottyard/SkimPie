# data


class Int:
    def __init__(self, literal):
        self.value = int(literal)

    def __str__(self):
        return str(self.value)

    def eval(self, env):
        return self.value


class Symbol:
    def __init__(self, literal):
        self.value = literal

    def __str__(self):
        return self.value

    def eval(self, env):
        return env.lookup(self.value)


# expressions


class Program:
    def __init__(self, expressions):
        self.exps = expressions

    def __str__(self):
        return '\n'.join([str(e) for e in self.exps])

    def eval(self, env):
        for e in self.exps:
            v = e.eval(env)
        return v


class If:
    def __init__(self, cond, when_true, when_false):
        self.cond = cond
        self.when_true = when_true
        self.when_false = when_false

    def __str__(self):
        return 'if (%s) then (%s) else (%s)' % (
            str(self.cond), str(self.when_true), str(self.when_false))

    def eval(self, env):
        if self.cond.eval(env):
            return self.when_true.eval(env)
        else:
            return self.when_false.eval(env)


class Quote:
    def __init__(self, s_exp):
        self.s_exp = s_exp

    def __str__(self):
        return str(self.s_exp)

    def eval(self, env):
        return self.s_exp


class Application:
    def __init__(self, proc_to_be, args):
        self.proc_to_be = proc_to_be
        self.args = args

    def __str__(self):
        return '(%s)(%s)' % (
            str(self.proc_to_be), ', '.join(list(map(str, self.args))))

    def eval(self, env):
        procedure = self.proc_to_be.eval(env)
        evaluated_args = [a.eval(env) for a in self.args]
        # if isinstance(self.proc_to_be, Symbol):
        #     print('applying', self.proc_to_be.value, 'to', evaluated_args)
        # else:
        #     print('applying to', evaluated_args)
        return procedure(evaluated_args)


class Define:
    def __init__(self, symbol, value):
        self.name = symbol.value
        self.value = value

    def __str__(self):
        return '%s = (%s)' % (self.name, str(self.value))

    def eval(self, env):
        env.set(self.name, self.value.eval(env))
        return None


class DefineProc:
    def __init__(self, name, params, body):
        pass

    def __str__(self):
        pass

    def eval(self, env):
        pass


class Lambda:
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def __str__(self):
        return '<lambda object>'

    def eval(self, env):
        return Procedure(self.params, [self.body], env)


# procedure


class Procedure:
    def __init__(self, params, body, env):
        self.params = params
        self.body = body
        self.env = env

    def __repr__(self):
        return "<proc object>"

    # apply
    def __call__(self, args):
        nested_env = self.env.nested()
        for symbol, value in zip(self.params, args):
            nested_env.set(symbol.value, value)
        for expression in self.body[:-1]:
            expression.eval(nested_env)
        return self.body[-1].eval(nested_env)
