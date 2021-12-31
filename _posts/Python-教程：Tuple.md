---
title: 如何学习编程，以 python 为例：数据的抽象
date: 2021-07-04 13:16:09
tags:
---

很多时候我们希望表示结构化的数据，比如我们想表示一个分数，那么它包含一个分母和一个分子。这时，基础数据类型是不足以表示这样的概念的。但是没关系，一个分数可以用两个整数表示。

这里用了一些 python 的语法糖，但是其他语言中都有类似的概念。

现在我们用两个整数的复合表示分数

```python
(3, 5) # represents 3/5
(6, 2) # represents 6/2 i.e. 3
```

对分数进行取值，取分母和分子。

```python
numerator, denominator = (3, 5)
# numerator = 3
# denominator = 5
```

python 并不自带分数计算方法，不过没有关系，因为python 提供了整数运算方法，通过组合组合已有的运算，我们可以定义分数运算

```python
def frac_add(a, b):
  numer_a, denom_a = a
  numer_b, denom_b = b
  numer_new = numer_a * denom_b + numer_b * denom_a
  denom_new = denom_a * denom_b
  return (numer_new, denom_new)
```

```python
def frac_mul(a, b):
  numer_a, denom_a = a
  numer_b, denom_b = b
  numer_new = numer_a * numer_b
  denom_new = denom_a * denom_b
  return (numer_new, denom_new)
```

```python
a = (3, 5)
b = (2, 4)

frac_mul(a, b) # (6, 20)
```

## 数据复合的抽象

现在我们已经学过怎么复合简单的数据了。现在我们在数据复合的基础上进行抽象。

我们现在希望定义一个二维坐标上的点。和之前类似，我们可以用tuple表示

```python

```

而且我可以轻易切换笛卡尔坐标和极坐标。我们只需要重新定义一组新的取值函数即可。

并且现在我们可以完全忘记我们是怎么定义的向量的了。我们可以用极坐标表示，也可以用笛卡尔坐标表示。但是他们完全不影响我们的使用。

这就是抽象的好处。

构造函数和取值函数看起来非常简单，但是他们其实非常有用。比如如果你想把分子和分母的位置调换一下，那么你只需要修改取值函数的定义

```python
def mul_frac(num1, num2):
     new_numer = get_numer(num1) * get_numer(num2)
     new_denom = get_denom(num1) * get_nuner(num2)
     return make_frac(new_numer, new_denom)
```

这样太麻烦了，所以我们希望自动生成取值函数。

这里是为了接下来面向对象编程作准备。