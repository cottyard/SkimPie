import sptokenizer
import spparser
import environment
import traceback

prompt = 'pie > '


def read_input():
    print(prompt, end="", flush=True)

    indent = 0
    unmatched_left = 0
    lines = []

    while True:
        line = input(' ' * indent)
        lines.append(line)
        for c in line:
            if c == '(':
                unmatched_left += 1
            elif c == ')':
                unmatched_left -= 1
        if unmatched_left <= 0:
            return '\n'.join(lines)

        indent = len(prompt)


def repl():
    while True:
        source = read_input()
        try:
            tokens = sptokenizer.tokenize(source)
            ast = spparser.parse_program(tokens)
            value = ast.eval(environment.global_env)
        except Exception:
            print(traceback.format_exc())
        else:
            if value is not None:
                print(value)

repl()
