---
title: 如何学习编程，以python为例：递归
date: 2021-07-11 20:20:37
tags:
---

这里介绍一些编程中解决问题的思路。

一个计算机程序可能看起来很神奇，但是请记住，这没有什么可神奇的。所有计算机程序都是把一个复杂问题不断变小，直到能用基本操作解决。

接下来我将用几个例子展示这个观点。

之前我们学过怎么处理简单的过程抽象：把过程组织到函数里。

比如计算一个数的绝对值：

```python
def find_abs(value):
  if value >= 0:
    return value
  else:
    return - value
```

通过小的函数我们可以构建一些大的函数

```python
def find_pow_3(value):
	return value * value * value

def find_pow_3_then_abs(value):
  return find_abs(find_pow_3(value))
```



我们可以很容易描述一些顺序性的事物。

顺序性的事物：

如果想要煮泡面：

1. 烧水
2. 放面条
3. 放调料



但是有些时候我们没办法把解决方案完全描述出来

比如我们介绍了怎么求平方，怎么求三次方，怎么求四次方，但是如果想求五次方，我是不是还要定义另一个函数呢。我当然可以，但是观察之前我们定义的各种求次方的函数，我们发现很多地方是重复的。

似乎三次方只是在二次方的基础上多乘了一次自己，而二次方则是自己乘一次方，一次方是自己乘一，而任何数的零次方都是1。

那么我们可以归纳，(n + 1) 次方是在 n 次方的基础上多乘一次自己，任何数的0次方是1

```python
def pow(x, n):
  if n < 0:
    raise Exeption("Doesn't support")
  if n == 0:
    return 1
  return x * pow(x, n - 1)
```

这样做的好处有

1. 我们少定义了很多函数
2. 我们可以应对更多的用户输入，很多时候我们是不知道用户需要什么的

比如如果我们需要计算一个复数的n次根，那么任意次方就是必须的，而不是可选的。



另外，我们还可以用稍微更快一点算法

```python
def pow(x, n):
	if n % 2 == 0: # 是2的倍数
   	temp = pow(x, n / 2)
    return temp * temp
  
  temp = pow(x, (n - 1) / 2)
  return temp * temp * x
```

理论上，这是最快的算法



首先是怎么对一个数开根号。我们可以用二分法

```python
def sqrt(number : float) -> float:
  def sqrt_()
```

