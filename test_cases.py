case_basic_ops = ("""
(+ (- 0 12)
   (* 2 2 2)
   (/ 7 2)
   (mod 7 2))
""", 0.5)

case_if = ("""
(if (<= 5 6) (+ 7 8) (+ 9 10))
""", 15)

case_list = ("""
(cons 4 (list (car (cdr (quote (1 2 3))))))
""", [4, '2'])

case_function = ("""
(define inc
    (lambda (x) (+ x 1)))
(inc 1)
""", 2)

case_higher_level_function = ("""
((lambda (f) (f 1))(lambda (x) (+ x 6)))
""", 7)

case_recursion = ("""
(define factorial (lambda (n)
    (if (= n 1)
        1
        (* n (factorial (- n 1))))))
(factorial 6)
""", 720)

# this is the normal-order Y combinator
# (define Y (lambda (f) (lambda (x) (f (x x))))(lambda (x) (f (x x))))

case_Y_combinator = ("""
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
""", 120)

case_lambda_calculus_conditional = ("""
(define TRUE
  (lambda (x)
    (lambda (y) x)))

(define FALSE
  (lambda (x)
    (lambda (y) y)))

(define (IF cond when-true when-false)
  ((cond when-true) when-false))

(cons (IF TRUE 1 2) (cons (IF FALSE 1 2) (quote ())))
""", [1, 2])

case_quote_abbreviation = ("""
(cons '4 '(1 2 3))
""", ['4', '1', '2', '3'])

case_set_and_closure = ("""
(define (Constructor)
  (define n 0)

  (define (inc)
    (set! n (+ n 1)))

  (define (read) n)

  (lambda (method-name)
    (if (eq? method-name 'inc)
        inc
    (if (eq? method-name 'read)
        read
    '()))))

(define obj (Constructor))

((obj 'inc))
((obj 'inc))
((obj 'read))
""", 2)


import re


def all_cases():
    items = sorted(globals().items(), key=lambda item: item[0])
    return [item for item in items if re.match(r'case', item[0])]