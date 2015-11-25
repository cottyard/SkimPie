import apply

# data


class Int:
    def __init__(self, literal):
        self.value = int(literal)

    def __str__(self):
        return str(self.value)

    def eval(self, env):
        return self.value


class Float:
    def __init__(self, literal):
        self.value = float(literal)

    def __str__(self):
        return str(self.value)

    def eval(self, env):
        return self.value


class Symbol:
    def __init__(self, literal):
        self.value = literal

    def __str__(self):
        return "'%s'" % self.value

    def eval(self, env):
        return env.lookup(self.value)


class List:
    def __init__(self, s_exp):
        self.s_exp = s_exp

    def __str__(self):
        return str(self.s_exp)

    def eval(self, env):
        return self.s_exp


# expressions

class Assignment:
    def __init__(self, symbol, value_exp):
        self.identifier = symbol.value
        self.value_exp = value_exp

    def __str__(self):
        return "%s := %s" % (str(self.identifier), str(self.value_exp))

    def eval(self, env):
        env.find_env(self.identifier)[self.identifier] = self.value_exp.eval(env)
        return None


class Program:
    def __init__(self, expressions):
        self.exps = expressions

    def __str__(self):
        return '\n'.join([str(e) for e in self.exps])

    def eval(self, env):
        v = None
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
        if apply.force(self.cond.eval(env)):
            return self.when_true.eval(env)
        else:
            return self.when_false.eval(env)


class Application:
    def __init__(self, proc_to_be, arg_exps):
        self.proc_to_be = proc_to_be
        self.arg_exps = arg_exps

    def __str__(self):
        return '(%s)(%s)' % (
            str(self.proc_to_be), ', '.join(list(map(str, self.arg_exps))))

    def eval(self, env):
        procedure = apply.force(self.proc_to_be.eval(env))
        return apply.apply(procedure, self.arg_exps, env)


class Define:
    def __init__(self, name, value):
        self.name = name.value
        self.value = value

    def __str__(self):
        return '%s = (%s)' % (self.name, str(self.value))

    def eval(self, env):
        env.set(self.name, self.value.eval(env))
        return None


class DefineProc:
    def __init__(self, name, params, body):
        self.name = name.value
        self.params = params
        self.body = body

    def __str__(self):
        return '%s = <proc object>' % self.name

    def eval(self, env):
        env.set(self.name, apply.Procedure(self.params, self.body, env))
        return None


class Lambda:
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def __str__(self):
        return '<lambda object>'

    def eval(self, env):
        return apply.Procedure(self.params, [self.body], env)
