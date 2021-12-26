---
title: 如何学习编程，以python为例：信任和递归
date: 2021-07-11 20:20:37
tags:
---

这里介绍一些编程中解决问题的思路。

一个计算机程序可能看起来很神奇，但是请记住，这没有什么可神奇的。所有计算机程序都是把一个复杂问题不断变小，直到能用基本操作解决。

接下来我将用几个例子展示这个观点。



之前，我们介绍了怎么利用函数来 “签订契约”，现在我们介绍 “信任契约“ 带来的魔法。



之前，我们可以很容易描述一些层级性的事物。

比如根据人名生成有关体重的健康建议。

我们先通过人名在数据库中获取体重和身高，然后又根据身高体重计算 BMI，最后通过 BMI 生成 BMI category 和 建议。

我们可以认为有这样一张图，表示各种函数的层级

```
generate_report_by_name

===== based upon =====

get_weight_by_name
get_height_by_name
check_BMI_category_by_weight_height
get_suggestion_by_BMI_category
```



```
check_BMI_category_by_weight_height

===== based upon =====

check_BMI_category_by_BMI
find_BMI
```



现在我们来做一些层级性不是那么明显的事

观察下面几个函数

```python
def pow_2(value):
  return value * value

def pow_3(value):
	return value * value * value

def pow_4(value):
  return find_abs(find_pow_3(value))
```



1. 



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



开根号的算法

首先是怎么对一个数开根号。我们可以用二分法

```python
def sqrt(number : float) -> float:
  def sqrt_()
```



斐波那契数列

