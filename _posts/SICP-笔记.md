---
title: SICP 笔记
date: 2021-04-05 20:52:11
tags:
---



Understanding a language :

- The primitives
- The ways of combinations
- The ways of abstractions



The key to understand complicated things is to not look at the detail. 



You have the name of sprites, you have the power over it.

如果你能对一个事物命名，你就可以掌控它。感觉有点语言哲学的感觉。唯名论的感觉。



Iteration vs linear recursion

```scheme
(define (+ x y)
  if (= x 0)
  	 y
  	 (+ (pred x) (succ y)))

;; Iteration
;; (+ 2 5)
;; (+ 1 6)
;; (+ 0 7)
;; 7
;; O(x) time O(1) space


(define (+ x y)
  if (= x 0)
     y
  	 (succ (+ (pred x) y)))

;; Linear Recursion
;; (succ (+ 2 4))
;; (succ (succ (+ 1 4)))
;; (succ (succ (succ (+ 0 4))))
;; (succ (succ (succ 4)))
;; (succ (succ 5))
;; (succ 6)
;; 7
;; O(x) time O(x) space
```





学习编程就是学习编程语言里有用的模式，比如如何从数列中挑出最大的元素。如果不会这些模式，写程序会很痛苦。（抽象）

计算机科学是非常唯名论的学科，他鼓励忘记符号背后的意义。感觉有点像抽象代数的感觉，把一类计算全部看作某某算子。



data abstraction

(denominator fraction) 

(numerator fraction)

而不是 (car fraction) (cdr fraction)

延迟作出具体实现的决定

计算机科学最重要的一点就是在你做出实现之前，你可以假设你已经有了一个实现

之后再根据需要做决定



如果认为你可以在开始编程之前设计好所有东西，那往往是不对的



在计算机编程中为某个事情找到意义往往比实现它更难



数据的抽象其实是一种和实现者的契约。比如分数的抽象需要保证以下性质

x = (make-fraction n d)

(numerator x) / (denominator x) = n / d

实际上这些契约定义了什么是 rational number，而具体实现并不确定什么是 rational number，他们只是符合定义的某种实现



再比如如何定义 pair

pair 其实是符合以下公理的东西

(car (cons a b)) = a

(cdr (cons a b)) = b

这样定义的 cons car cdr 组成了 pair



循环是一种特殊的递归，它的效率更好

允许我们进行递归的性质是 闭包 。比如

```
(num + num) -> num -- 连加利用了 + 封闭的的性质
(cdr list) -> list -- map 利用了 cdr 是封闭运算的性质，所以可以递归
data Tree a = Node a Tree Tree | Nil   -- 利用了树是自相似的，所以可以遍历

```



两种构建抽象的方式

自顶向下

```
					a
					|
	------------------
	|       |        |
-----   -----    ------
|   |   |   |    |    |
   ----
   |  |
```



分层dls

```
----------------------
| language of 组合图像|
----------------------
          |
-----------------------
| language of 构建图像 |
-----------------------
				  |
-----------------------
| language of 点和向量 |
-----------------------
```



sicp 推荐使用 分层 dls 但是我觉得各有优势，自顶向下适合完成特定任务，分层dls 提供了更好的扩展性，支持随意组合。

数学是一种分层 dls，感觉一些上古软件也有分层 dls 的感觉，比如说 vim。

感觉挺多库的设计都使用了两种策略，比如 机器学习库 使用了 分层 dls 表示各种数据（矩阵 auto-grad 卷积)，但是在特定算法上使用了 自顶向下 ，比如人脸识别 分成 特征提取 和 分类器。



为什么积分比微分更难：

因为微分是把一个大问题转换程一些小问题，而积分是反过来。（但是问题是，很多小问题有相似的模式，所以不容易转换回去）
$$
\frac{d(uv)}{dt} = v\frac{du}{dt} + u\frac{dv}{dt}
$$
左边是一个大问题，右边是小问题

但是转换回去不容易，我们很难看出来 第二项含有 第一项某个部分的微分，第一项含有第二项某个部分的微分，而且两边微分的部分恰好是另一边不微分的部分🤷‍♀️



非常好解释 quote 的方式：

A: say your name

B: Sussana

A: say your name

C: your name

符号不仅代表其所代表的，也代表其本身



函数式数据结构 

名称 对应 值 比如 

```scheme
(define list-a '(1 2 3))	

(define list-b (cdr list-a))
```



非函数式数据结构

名称对应指针 （值储存的位置）

```scheme
(define list-a '(1 2 3))

(set! list-a (cdr list-a))
```





名称由量词创造

```
(lambda food (cook food)) ;; procedure that cooks food

```



这个我也没想好怎么解释





编程中很多的问题是 同一性 造成的

比如说

```scheme
(define a (cons 1 2))

(define b (cons a a))

(set-car! b (cons 3 4))
;; a = [1, 2]
;; b = [[3, 4], [1, 2]]

(set-car! a 5)
;; a = [5, 2]
;; b = [[3, 4], [5, 2]]

(set-car! (cdr b) 6)
;; a = [6, 2]
;; b = [[3, 4], [6, 2]]
```

在修改 a 的时候，b 变了

但是修改 b 的时候 a 却没有变

之后再次修改 b 的时候，a 缺又变了



我们可以禁止任何变化的发生。因为这种互相影响的变化（b 变化时 a 也变化） 是很多复杂系统的 bug 的来源。但是 同时，我们需要这样一种可以变化的结构，因为如果不允许改变。那么很多数据结构是没办法高效、方便地实现的，比如哈希表和队列。



但是如果我这样

```scheme
(define a (cons 1 2))

(define b (cons 
           	(cons (car a) (cdr a))
           	(cons (car a) (cdr a))))

(set-car! b (cons 3 4))
;; a = [1, 2]
;; b = [[3, 4], [1, 2]]

(set-car! a 5)
;; a = [5, 2]
;; b = [[3, 4], [1, 2]]

(set-car! (cdr b) 6)
;; a = [5, 2]
;; b = [[3, 4], [6, 2]]
```

这次 a 和 b 的变化互相不影响对方。



这里展示出，变量对应的是 储存 值的容器。值 和 变量 是 不同的。

但是在

