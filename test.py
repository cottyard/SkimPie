import sptokenizer
import spparser
from environment import Environment, built_ins
import test_cases
import apply

for case_name, case in test_cases.all_cases():
    source, expected_value = case

    tokens = sptokenizer.tokenize(source)
    program = spparser.parse_program(tokens)
    actual_value = apply.force(program.eval(Environment(built_ins)))

    if expected_value != actual_value:
        print(case_name, 'failed with a returned value of', actual_value)

print('done')