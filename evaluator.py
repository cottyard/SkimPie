# if

def if_clause(exp):
    if exp[0] == 'if':
        return True
    return False

def eval_if(exp, env):
    if len(exp) != 4:
        raise SyntaxError

    condition = evaluate(exp[1], env)
    if condition:
        return evaluate(exp[2], env)
    else:
        return evaluate(exp[3], env)

# self evaluating

class SelfEvaluateError(BaseException):
    pass

def int_evaluator(exp):
    try:
        return int(exp)
    except (ValueError, TypeError):
        raise SelfEvaluateError

self_evaluators = [
    int_evaluator,
]

def self_evaluating(exp):
    for evaluator in self_evaluators:
        try:
            evaluator(exp)
            return True
        except SelfEvaluateError:
            pass
    return False

def self_evaluator(exp, env):
    for evaluator in self_evaluators:
        try:
            return evaluator(exp)
        except SelfEvaluateError:
            pass

# apply

def application(exp):
    return isinstance(exp, list)

def application_evaluator(exp, env):
    procedure = exp[0]
    arguments = list(map(lambda exp: evaluate(exp, env), exp[1:]))
    return apply(procedure, arguments)

def primitive_procedure(procedure):
    return procedure in primitive_procedure_implementations

def primitive_multiply(*arguments):
    result = 1
    for a in arguments:
        result *= a
    return result

def primitive_add(*arguments):
    result = 0
    for a in arguments:
        result += a
    return result

def primitive_equal(*arguments):
    a0 = arguments[0]
    for a1 in arguments[1:]:
        if not a0 == a1:
            return False
        a0 = a1
    return True

def primitive_less_than(*arguments):
    a0 = arguments[0]
    for a1 in arguments[1:]:
        if not a0 <= a1:
            return False
        a0 = a1
    return True

primitive_procedure_implementations = {
    '+': primitive_add,
    '*': primitive_multiply,
    '==': primitive_equal,
    '<=': primitive_less_than,
}

def apply_primitive(procedure, arguments):
    impl = primitive_procedure_implementations[procedure]
    return impl(*arguments)

def apply(procedure, arguments):
    #print('applying', procedure, 'to', arguments)
    if primitive_procedure(procedure):
        return apply_primitive(procedure, arguments)
    else:
        raise NotImplementedError()

# eval

evaluators = [
    (self_evaluating, self_evaluator),
    (if_clause, eval_if),
    (application, application_evaluator),
]

def evaluate(exp, env):
    #print('evaluating', exp)
    for determinator, evaluator in evaluators:
        if determinator(exp):
            return evaluator(exp, env)
