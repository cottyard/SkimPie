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


primitive_procedure_implementations = {
    '+': primitive_add,
    '*': primitive_multiply
}

def apply_primitive(procedure, arguments):
    impl = primitive_procedure_implementations[procedure]
    return impl(*arguments)

def apply(procedure, arguments):
    if primitive_procedure(procedure):
        return apply_primitive(procedure, arguments)
    else:
        raise NotImplementedError()

# eval

evaluators = [
    (self_evaluating, self_evaluator),
    (application, application_evaluator)
]

def evaluate(exp, env):
    for determinator, evaluator in evaluators:
        if determinator(exp):
            return evaluator(exp, env)
