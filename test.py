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

s4 = """
(cons 4 (list (car (cdr (quote (1 2 3))))))
"""

s5 = """
(define name 6)
"""

s6 = """
name
"""

s7 = """
((lambda (x) (+ x 1)) 2)
"""

s8 = """
((lambda (f) (f 1))(lambda (x) (+ x 6)))
"""

sources = [s1, s2, s3, s4, s5, s6, s7, s8]

import sptokenizer
import spparser
import environment

for s in sources:
    s = sptokenizer.tokenize(s)
    s = spparser.parse(s)
    print('parsed:', s)
    print('evaluated to:', s.eval(environment.global_env))
