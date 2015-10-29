source_1 = """
(+ 1 2)
"""

source_2 = """
(+ 3 (* 5 6))
"""

source_3 = """
  (+ (* 1 1)
     (* 2 2)
     (* 3 3)
     (* 4 4))
"""

sources = [source_1, source_2, source_3]

import sptokenizer
import spparser
import evaluator

for s in sources:
    s = sptokenizer.tokenize(s)
    print('tokenized', s)
    s = spparser.parse(s)
    print('parsed', s)
    s = evaluator.evaluate(s, {})
    print('evaluated', s)
