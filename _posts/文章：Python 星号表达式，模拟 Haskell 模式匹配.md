---
title: 文章：Python 星号表达式，模拟 Haskell 模式匹配
date: 2020-10-18 00:06:51
tags:
---

# Python 的星号表达式，模拟 Haskell 模式匹配

简略写写 星号表达式 的语法。

首先是星号可以表示变长参数。

```python
def add_first_two(a,b,*args,key1,key2,**kwargs):
    try:
        print(key1)
        print(key2)
    except:
        pass
    finally:
        print(**kwargs)
        return a + b
```

之后是星号表达式的解包。

星号表达式在赋值语句左边和右边的含义是不同的。

左边表示匹配参数

```python
tpl = (1,2,3,4)

head,*belly,tail = tpl
head  # 1
belly # (2,3)
tail  # 4

((a,*b),*c) = ["Python","JavaScript","Haskell"]
a # 'P'
b # ['y','t','h','o','n']
c # ["JavaScript","Haskell"]
```

右边表示参数展开。

```python
tpl = (1,2,3,4)
lst = [*tpl] # [1,2,3,4]

long_lst = [*tpl,*lst] # [1,2,3,4,1,2,3,4]

dct = dict(a=1,b=2,c=3)
dct_to_lst = [*dct] #'a' 'b' 'c'

long_dct = {**dct,"d"=4} # dict(a=1,b=2,c=3,d=4)

print(*tpl)
#1 2 3 4

print(tpl)
#(1,2,3,4)
```

最近在学 Haskell，里面的模式匹配很优雅。

在 Haskell 中我们可以使用这样的语句

```haskell
sum :: [Int] -> Int
sum [] = 0
sum (n:ns) = n + sum(ns)

sum [1,2,3,4,5]
-- 15
```

在python中我们也可以使用类似的

```python
def sum(lst):
    n,*ns = lst
    if ns is None:
        return n
    else:
        return n + sum(ns)
```

这样写是为了和上面  Haskell 的 sum 函数输入格式匹配，都是 `list`。

如果不要求使用 `list` 作为输入的话，我们可以利用 python 的变长参数写的更优雅一点。

```python
def sum(n,*ns):
    if ns is None:
        return n
    else:
        return n + sum(*ns)
```

这样看起来 Python 利用星号表达式也可以在一定程度上模拟 Haskell 的引以为傲的模式匹配了。Python 可以模拟一维的模式匹配，几乎没有损失。

但是对于高于一维的模式匹配，Python 就会有点力不从心。

```haskell
addVector (x1, y1) (x2, y2)
	= (x1 + x2, y1 + y2)
	
addVector (1, 2), (3, 4)
-- (4, 6)
```

对于上面这种，我们可以用 dummy variable 来获取参数。

```python
def addVector(vx,vy):
    (x1,y1),(x2,y2) = vx,vy
    return (x1 + x2, y1 + y2)
```

```python
def addVector(vector_x,vector_y):
    (x,*xs), (y,*ys) = vector_x, vector_y
    return (x+y,addVector(xs,ys))
```

可惜这样的话，我们在输入函数参数的时候就没有提示了。

有点类似于海象运算符，但是这里是作用于函数的输入，海象运算符用不了。
