---
title: prolog 的优越性及其边界
date: 2021-12-26 02:14:29
tags:
---

> 前置知识：
> 
> 皮亚诺算术
> 
> 整数的定义
> 
> Prolog 语法
> 
> 可选：
> 
> 可数集
> 
> unification 

Prolog 使用了 `unification` 算法。

## Unification 算法的语义

实际上这个算法的语义是 :

- 在 toplevel 查找表达式的定义。

- 如果 toplevel 可以找到可能匹配的定义，查看定义。

- 定义由

- 依次求值 and conjunction。根据 conjunction 找可能匹配的，variable。求值内部的 expresion。找到下一个 conjunction，把已有的 expression 带入。

```haskell
eval (Clause pre vars defs) (env : envs) = 
    |get-pre env 
```

之后依次顺序尝试匹配 and 连接的 predicate。

prolog 既有 declaretive 语义也同时也有 imperative 语义。

因此在写程序的时候需要保证流按偏序生成，这样可以保证覆盖所有的可能解。

值得注意的是 prolog 和逻辑不等价。

prolog 的语义是：寻找搜索空间中的所有可能解。

之后我会讨论一下 prolog 使用的 unification 算法。

关系型编程的好处是合理处理的关系可以反向计算。

这有点像之前我们做过的 haskell 的 reasoning about programs。在 reasoning 中，我们有时需要定义一个关系，代表某函数的参数及其结果符合某某关系。例如：

正是因为关系是双向的，而函数是单向的，所以 prolog 可以反向运算。

但请注意，反向运算是有边界的。

prolog 有一个很好的特性：他可以反向计算

下面我用一个例子展示 prolog 操作数学 object

```prolog
nat(n).
nat(s(N)) :-
    nat(N).
```

这段语句定义了一个链。这就是所有自然数的定义。

```prolog
three :- nat(s(s(s(n)))).
five :- nat(s(s(s(s(s(n)))))).
```

三和五都是整数。

```prolog
add_n(n, Y, Y).
add_n(s(X), Y, R) :-
    add_n(X, s(Y), R).
```

这里定义 naive 的加法。

如果我们只关注加法的正向计算，那么我们可以说这个算法是正确的。

```prolog
add_n(s(s(s(n))), s(s(n)), R).
```

但是我现在遇到一个问题，给定任一想要的输出，这个程序保证在有限的时间内输出这个输出。但是这个程序不保证结束。

例如在输出`add_n(X, Y, R)`的时候，这个定义只能输出：

```prolog
X = n, Y = Z = n;
X = n, Y = Z = s(n);
X = n, Y = Z = s(s(n));
```

它的求值方法是

看一个表达式。如果这个表达式中没有变量：

1. 我们可以理解为内部的 conjunction，之后每次经过一个 conjunction，都会过滤一些值。

找包括关系的

如果我们能把定义改为

```prolog
add_n(s(X), Y, R) :-
    nat(R),
    add_n(X, s(Y), R).
```

prolog 语言的一种定义我附在这里，我实在懒得搞这个了

```scheme
;;; source http://community.schemewiki.org/?sicp-ex-4.78


;;; Exercise 4.78
(load "ch4-ambeval.scm")

(define input-prompt ";;; Query input:")
(define output-prompt ";;; Query results:")

(define (qeval query frame succeed fail)
  ((analyze query) frame succeed fail))

;;; predicates
(define (and? query) (tagged-list? query 'and))
(define (or? query) (tagged-list? query 'or))
(define (not? query) (tagged-list? query 'not))
(define (lisp-value? query) (tagged-list? query 'lisp-value))

(define (analyze query)

  (cond ((and? query) (analyze-and (contents query)))
        ((or? query) (analyze-or (contents query)))
        ((lisp-value? query) (analyze-lisp-value (contents query)))
        ((not? query) (analyze-not (contents query)))
        (else (analyze-simple query))))

(define (analyze-lisp-value call)
  (lambda (frame succeed fail)
    (if (execute
         (instantiate
          call
          frame
          (lambda (v f)
            (error "Unknown pat var -- LISP-VALUE" v))))
        (succeed frame fail)
        (fail))))

(define (analyze-not operands)
  (lambda (frame succeed fail)
    ((analyze (negated-query operands))
     frame
     (lambda (ext fail2)
       (fail))
     (lambda () (succeed frame fail)))))

(define (analyze-or disjuncts)
  (lambda (frame succeed fail)
    (define (try)
      ((analyze (car disjuncts))
       frame
       succeed
       (lambda ()
         ((analyze-or (cdr disjuncts))
          frame succeed fail))))

    (if (empty-disjunction? disjuncts)
        (succeed frame fail)
        (try))))

(define (analyze-and conjuncts)
  (lambda (frame succeed fail)
    (define (try)
      ((analyze (car conjuncts))
       frame
       (lambda (ext fail2)
         ((analyze-and (cdr conjuncts))
          ext succeed fail2))
       fail))

    (if (empty-conjunction? conjuncts)
        (succeed frame fail)
        (try))))

;;; rewritten
(define (rule-body rule)
  (if (null? (cddr rule))
      #f
      (caddr rule)))

(define (analyze-simple query)
  (lambda (frame succeed fail)
    (define (try-assertion assertions)
      (if (stream-null? assertions)
          (try-rule (fetch-rules query frame))
          (let ((ext (pattern-match query (stream-car assertions) frame))
                (fail2 (lambda () (try-assertion (stream-cdr assertions)))))
            (if (succeeded? ext)
                (succeed ext fail2)
                (fail2)))))

    (define (try-rule rules)
      (if (stream-null? rules)
          (fail)
          (let* ((clean-rule (rename-variables-in (stream-car rules)))
                 (ext (unify-match query (conclusion clean-rule) frame))
                 (fail2 (lambda () (try-rule (stream-cdr rules)))))
            (if (succeeded? ext)
                (if (rule-body clean-rule)
                    (qeval (rule-body clean-rule)
                           ext
                           succeed fail2)
                    (succeed ext fail2))
                (fail2)))))

    (try-assertion (fetch-assertions query frame))
    ))

(define (driver-loop)
  (define (internal-loop try-again)
    (prompt-for-input input-prompt)
    (let ((q (query-syntax-process (read))))
      (cond
       ;; ((eq? q '#!eof) 'goodbye!)
       ((eq? q 'try-again) (try-again))
       ((assertion-to-be-added? q)
        (add-rule-or-assertion! (add-assertion-body q))
        (newline)
        (display "Assertion added to assertions base.")
        (driver-loop))
       (else (newline)
             (display ";;; Starting a new problem ")
             (qeval q
                    '()  ; an empty frame
                    ;; ambeval success
                    (lambda (val next-alternative)
                      (announce-output output-prompt)
                      (user-print
                       (instantiate q
                                    val
                                    (lambda (v f)
                                      (contract-question-mark v))))
                      (internal-loop next-alternative))
                    ;; ambeval failure
                    (lambda ()
                      (announce-output
                       ";;; There are no more values of")
                      (user-print q)
                      (driver-loop)))))))
  (internal-loop
   (lambda ()
     (newline)
     (display ";;; There is no current problem")
     (driver-loop))))

;;;;;;;;;;;;;;;;;;;;;;
        test
;;;;;;;;;;;;;;;;;;;;;;

;;; Query input:
(big-shot ?p ?q)

;;; Starting a new problem
;;; Query results:
(big-shot (Aull DeWitt) administration)

;;; Query input:
try-again

;;; Query results:
(big-shot (Cratchet Robert) accounting)

;;; Query input:
try-again

;;; Query results:
(big-shot (Scrooge Eben) accounting)

;;; Query input:
try-again

;;; Query results:
(big-shot (Scrooge Eben) accounting)


;;; Query input:
(reverse (1 2 3) ?x)

;;; Starting a new problem
;;; Query results:
(reverse (1 2 3) (3 2 1))


;;; Query input:
(and (replace ?p2 ?p1)
            (salary ?p1 ?s1)
            (salary ?p2 ?s2)
            (lisp-value > ?s2 ?s1))

;;; Starting a new problem
;;; Query results:
(and (replace (Hacker Alyssa P) (Fect Cy D)) (salary (Fect Cy D) 35000) (salary (Hacker Alyssa P) 40000) (lisp-value > 40000 35000))

;;; Query input:
try-again

;;; Query results:
(and (replace (Warbucks Oliver) (Aull DeWitt)) (salary (Aull DeWitt) 25000) (salary (Warbucks Oliver) 150000) (lisp-value > 150000 25000))

;;; Query input:
try-again

;;; There are no more values of
(and (replace (? p2) (? p1)) (salary (? p1) (? s1)) (salary (? p2) (? s2)) (lisp-value > (? s2) (? s1)))
```