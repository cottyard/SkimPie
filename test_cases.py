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

case7 = """
(define factorial (lambda (n)
    (if (= n 1)
        1
        (* n (factorial (- n 1))))))
(factorial 6)
"""

# this is the normal-order Y combinator
# (define Y (lambda (f) (lambda (x) (f (x x))))(lambda (x) (f (x x))))

case8 = """
(define Y (lambda (f)
  ((lambda (x)
     (f (lambda (y) ((x x) y))))
   (lambda (x)
     (f (lambda (y) ((x x) y)))))))

(define fac-to-be (lambda (f)
  (lambda (n)
    (if (= n 1)
        1
        (* n (f (- n 1)))))))

((Y fac-to-be) 5)
"""

case9 = """
(define TRUE
  (lambda (x)
    (lambda (y) x)))

(define FALSE
  (lambda (x)
    (lambda (y) y)))

(define (IF cond when-true when-false)
  ((cond when-true) when-false))

(cons (IF TRUE 1 2) (cons (IF FALSE 1 2) (quote ())))
"""

import re

def all_cases():
    items = sorted(globals().items(), key=lambda item: item[0])
    return [item for item in items if re.match(r'case\d*', item[0])]