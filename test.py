import sptokenizer
import spparser
import environment
import test_cases

for case, source in test_cases.all_cases():
    tokens = sptokenizer.tokenize(source)
    #print(tokens)
    program = spparser.parse_program(tokens)
    #print('parsed:', program)
    print(case)
    print('evaluated to:', program.eval(environment.global_env))
