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

class Application:
    def __init__(self, proc, args):
        self.proc = proc
        self.args = args

    def __str__(self):
        return '(%s)(%s)' % (
            str(self.proc), ', '.join(list(map(str, self.args))))

    def eval(self, env):
        return self.proc.eval(env)([a.eval(env) for a in self.args])