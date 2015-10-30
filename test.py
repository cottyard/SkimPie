s1 = """
  (+ (* 1 1)
     (* 2 2 2)
     (* 3 3 3)
     (* 4 4))
"""

s2 = """
(if (== 1 2) 3 4)
"""

s3 = """
(if (<= 5 6) (+ 7 8) (+ 9 10))
"""

sources = [s1, s2, s3]

import sptokenizer
import spparser
import evaluator

for s in sources:
    s = sptokenizer.tokenize(s)
    s = spparser.parse(s)
    print('parsed', s)
    #s = evaluator.evaluate(s, {})
    #print('evaluated', s)
