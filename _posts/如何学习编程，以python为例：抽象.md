---
title: 如何学习编程，以python为例：函数抽象与契约
date: 2021-07-11 22:29:01
tags:
---

之前我们已经学习过基本元素和基本操作了。

> 前置知识，python 基本元素和操作，函数定义，作用域
> 
> 作用域是个十分重要的概念，但是这里没有讲；我在学习数学的过程中，很多困惑都是作用域不清晰造成的，再一次证明了程序是比数学更好的语言（狗头）

现在我们通过一个计算 BMI 指数的例子介绍函数的作用。

我希望计算 小红和小明的 BMI 指数。

我需要怎么做呢？

```python
weight_xiaohong = 50
height_xiaohong = 160

weight_xiaoming = 60
height_xiaoming = 165

BMI_xiaohong = weight_xiaohong / (height_xiaohong * height_xiaohong)
BMI_xiaoming = weight_xiaoming / (height_xiaoming * height_xiaoming)
```

## 函数作为公共模版

我们可以看到

```python
weight / (height * height)
```

这个公式反复出现，那我们不妨定义一个公共的模版来表示这样的计算。

```python
def find_BMI(weight, height):
  return weight / (height * height)
```

怎么理解函数呢，我们目前可以理解函数其实就是文本替代。我们可以认为

`find_BMI(weight, height)` 在数学上等价于 `weight / (height * height)`， 每次看到 `find_BMI` 我们只需在脑中想象它变成了具体的算式即可。

那么定义函数有什么好处呢

第一个好处是，每次需要 BMI 指数的时候我们可以少打很多字。

第二个好处是，我们更不容易出错，而且函数名也提供了更多的信息给读者，让读者明白这个程序在做什么。

只定义一个函数不是很有趣，那么不如我们增加一个新的需求：判断BMI指数是否健康。

那么我们可以这样定义

```python
def check_BMI_category_by_BMI(BMI):
  if BMI < 18.5:
    return "underweight"
  elif BMI < 25:
    return "normal weight"
  elif BMI < 29:
    return "over weight"
  else:
    return "obesity"
```

似乎这个函数也很简单。

## 函数的复合

有了这两个函数之后好玩的事情发生了，我们几乎免费获得了根据体重和身高判断是否超重的函数。这个函数是是前面两个函数的复合。

那么这是第三个好处，我们可以从更高的角度看问题，而不用总是关注底层的BMI公式是怎么算的。事实上从现在开始我已经可以忘记 BMI 公式的计算方式了。

```python
def check_BMI_category_by_weight_height(weight, height):
  return check_BMI_category_by_BMI(find_BMI(weight, height))
```

## 函数作为接口

那么第四个好处是函数为我们提供了一种合作的方式。

比如，有人写了另外两个函数

```python
get_height_by_name
get_weight_by_name
```

这两个函数通过人名，返回这个人的身高和体重。

这个函数背后有可能是一个很大的数据库，这个函数负责在这个数据库中查找这些信息然后返回；也有可能是一堆非常复杂的逻辑，比如发邮件给叫这个名字的人，然后根据收到的邮件智能分析数据。至于具体怎么实现，我们并不关心，我们只要知道这个东西存在就行了。

一个函数就是一个契约，你告诉它一个输入，它保证会告诉你结果。在计算机科学中，我们管这样的契约叫接口。计算机科学就是建立在这样的契约之上的，高层的操作并不需要知道底层实现具体是怎么样的。这种合作方式极为高效，在短短几十年间，计算机科学已经发展成为了这个星球上几乎是覆盖最广的科学，我很难想到有什么科学不需要计算机参与。

为什么叫接口是因为我们不关心内部的逻辑是怎么样的，我们只关心我们给它什么输入，我们会得到什么输出。

那么现在，我们可以根据人名来判断这个人是否超重了！

```python
def check_BMI_category_by_name(name):
  weight = get_weight_by_name(name)
  height = get_height_by_name(name)
  return check_BMI_category_by_weight_height(weight, height)
```

注意到我们并没有自己实现所有的逻辑，相反，别人替我们实现好了很大一部分。

## 为别人提供接口

现在我们定义了很多函数了，但是客户可能不愿意知道所有的细节（我们定义了什么辅助函数），那么不如我们定义一个主函数，只给用户提供他想要的信息。

```python
def generate_report_by_name(name):
  weight = get_weight_by_name(name)
  height = get_height_by_name(name)
  BMI_category = (weight, height)
  suggestions = get_suggestion_by_BMI_category(BMI_category)
  report = f"{name}, weight : {weight}, height : {height}, your BMI category is {BMI_category}, we would suggest you {suggestions}"
  return report
```

注意到这里的 suggestions 也是由别人定义好的函数生成的。

对于一般用户，他们只需要输入名字，然后调用这个函数，就能得到一份有关体重的健康报告，然而对于高级用户，他们则可以使用我们定义的其他辅助函数重新组合做一些高级操作。
