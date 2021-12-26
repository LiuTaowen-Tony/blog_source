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

实际上这个算法的语义是 :

寻找 toplevel 定义，根据 toplevel 定义生成一个流。

之后依次顺序尝试匹配 and 连接的 predicate。



prolog 既有 declaretive 语义也同时也有 imperative 语义。



因此在写程序的时候需要保证流按偏序生成，这样可以保证覆盖所有的可能解。



值得注意的是 prolog 和逻辑不等价。



prolog 的语义是：寻找搜索空间中的所有可能解。



之后我会讨论一下 prolog 使用的 unification 算法。



关系型编程的好处是合理处理的关系可以反向计算。



这有点像之前我们做过的 haskell 的 reasoning about programs。在 reasoning 中，我们有时需要定义一个关系，代表某函数的参数及其结果符合某某关系。例如：

```
fun-max
```

暂时没想到好的例子



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