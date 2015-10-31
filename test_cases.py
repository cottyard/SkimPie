case1 = """
  (+ (* 1 1)
     (* 2 2 2)
     (* 3 3 3)
     (* 4 4))
"""

case2 = """
(if (= 1 2) 3 4)
"""

case3 = """
(if (<= 5 6) (+ 7 8) (+ 9 10))
"""

case4 = """
(cons 4 (list (car (cdr (quote (1 2 3))))))
"""

case5 = """
(define inc
    (lambda (x) (+ x 1)))
(inc 1)
"""

case6 = """
((lambda (f) (f 1))(lambda (x) (+ x 6)))
"""

# case7 = """
# (define factorial (lambda (n)
#     (if (= n 1)
#         1
#         (factorial (- n 1)))))
# (factorial 6)
# """

import re

def all_cases():
    items = sorted(globals().items(), key=lambda item: item[0])
    return [item for item in items if re.match(r'case\d*', item[0])]