# Online Basic Racket Interpreter (Backend Repo)

> About

- Backend: Flask
- This is a basic Racket Interpreter built in 2 days for fun without looking at any Racket Interpreter source code, just from playing around with DrRacket.
- This repo contains the source code for the React frontend and Flask backend of the my Online Basic Racket Interpreter website source code.

> API Specification

- url: `https://something.com`
- body: `{ input: string, show_steps: boolean }`

> Features

- basic operations  
  ex: `(+ 2 3)`
- builtin functions  
  ex: `(gcd 12 18)`
- builtin constants  
  ex: `pi`
- console output  
  ex: `(printf 5)`
- custom functions  
  ex: `(define (add_two a b) (+ a b))`
- custom constants  
  ex: `(define x 10)`

> Data Types Supported

- numeric
- boolean

> Builtin Functions

`'cond', 'else', 'true', 'false', '=', '>', '<', '>= ', '<=', 'add1', 'sub1', '+', '-', '*', '/', '%', 'expt', 'sqr', 'sqrt', 'floor', 'ceiling', 'round', 'abs', 'max', 'min', 'gcd', 'lcm', 'sin', 'cos', 'tan', 'log', 'printf'`

> Builtin Constants

`'pi', 'e'`

> Specification

- Only numeric and boolean types are supported.
- Console output must be made by using the `'printf'` function.
- The `'cond'` conditionals can be written with both `()` and `[]` notation.
- There cannot be any duplicate definition names or parameter names that are already defined as definition names.
- There can be numeric or boolean values in a `'cond'` without an operation block `()`.

> Sample Code Blocks

### Add Two

```scheme
(define x 10)
(define y (* 2 3))

(define (add_two a b)
  (+ a b))

(printf (add_two x y))
```

### Factorial (Basic Recursion)

```scheme
(define (factorial n)
  (cond [(= n 1) 1]
        [else (* n (factorial (sub1 n)))]))

(printf (factorial 10))
```

### Factorial (Accumulative Recursion)

```scheme
(define (factorial n acc)
  (cond [(= n 1) acc]
        [else (factorial (sub1 n) (* n acc))]))

(printf (factorial 10 1))
```

### Nested Conditional

```scheme
(printf (cond [(cond [(> 2 1) true]
                     [else false]) 1]
              [else 2]))
```

---
