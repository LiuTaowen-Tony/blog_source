---
title: 文章：python 装饰器：roperty,  classmethod, staticmethod
date: 2020-09-30 13:45:39
tags:
---

# python 里的一些装饰器

> 这篇文章主要介绍 property,  classmethod, staticmethod 这三个装饰器

## 0x00 @property

### 函数调用作属性

property 这个装饰器可以把函数调用当作对象的属性

直接看例子会比较清楚

```python
class Matrix():
    def __init__(self,data):
        self._data = data
        self._r = len(data)
        self._c = len(data[0])
    
    @property
    def shape(self):
        return (self._r,self._c)
```

这里如果我们想看看 Matrix 的形状，那么我们直接执行

```python
a = Matrix([[1,2],[3,4]])
print(a.shape) #不是 a.shape()

#(2,2)
```

这样的好处是我们希望得到的是一个属性，用获得属性的方式去取的比较符合直觉

而且使用 @property 装饰器我们不用担心属性被修改

```python
a.shape = (3,4)
#AttributeError: can't set attribute
```

### 提升性能

@property 的另一个作用是延迟一些计算，让程序的性能更好

```python
    @property
    def T(self):
        try:
            return self._T
        else:
            self._T = Matrix([[self._data[i][j] for i in range(self._r)] for j in range(self._c)])
            return self._T
```

这里动态的给 Matrix Object 增加了一个 `_T` 属性，如果我们在整个程序里不需要求某个矩阵的转制，那么我们就不去求。

如果我们需要一个矩阵的转制，那么我们只在第一次使用的时候求它的转制，之后我们会把运算好的结果储存起来，方便下次调用。

三种方法对比

| `__init__`                         | `T()`                            | `@property`                        |
| ---------------------------------- | -------------------------------- | ---------------------------------- |
| 初始化的时候计算矩阵转制，并储存   | 每次调用的时候求矩阵转制，不储存 | 第一次调用的时候求矩阵转制，并储存 |
| 不需要使用转制的时候浪费内存空间   | 不储存                           |                                    |
| 所有矩阵初始化的时候都计算一次转制 | 每次调用都要计算一次转制         |                                    |

当然 python 支持动态为 object 添加属性，所以我们可以

```python
a.T = a.T()
```

但是这样的缺点是程序的维护性不够好，容易忘掉那些矩阵求过转制，哪些没有。@propert 解决了这些烦恼

## 0x01 @classmethod

### 提供不同的初始化方式

@classmethod 的第一大用途是支持各种不同初始化方式，同样的，我们直接看例子

```python
	@classmethod
    def zeros(cls,shape):
        r = shape[0]
        c = shape[1]
        return Matrix([[0 for _ in range(c)] for _ in range(r)])
```

Classmethod 相当于给 “类实例” (Class Object) 附上了一个方法，这里这个方法返回的是 Matrix 的构造函数。有点类似于 Cpp 里面的函数重载。

Python 中的类都是 `type` 类型的实例，所以我们可以给类附上方法。（类 与 元类 23333）

调用的话和看起来和我们熟悉的 numpy 类似

```python
print(Matrix.zeros((2,3)))

#[
# [0.00, 0.00,   0.00,   ],
# [0.00, 0.00,   0.00,   ],
#]
```

这里我写过 Matrix 的 `__str__` 方法，所以打印出来会比较好看。

### 函数包装进类

另外我们也可以用 classmethod 写一些操作 Matrix 的函数。

比如我们在实现好矩阵的 `__mul__ `方法以后，我们可以通过 classmethod 用另一种方式调用

```python
	@classmethod
    def dot(cls,A,B):
        return A * B #这里实现好了__mul__ 方法，可以直接调用
```

那么调用是这样的

```python
a = Matrix([1,2,3,4])

Matrix.dot(a,a.T) #等同于 a * a.T
# [[30]]
```

这样在我们在另一个程序里需要调用 Matrix 类的时候，我们只需要调用 Matrix 这一个类，里面就有所有对 Matrix 操作的函数。

## 0x02 @staticmethod

还有的用处是更改一些通用函数的表现

```python
class Matrix():
    layout = "%5.1f,"
    def __str__(self):
        out = "[\n"
        for i in range(self._r):
            out +=" ["
            for j in range(self._c):
                out += self.layout%self._data[i][j]
            out +="],\n"
        out+= "]"
        return out
    
    @staticmethod
    def change_layout(width,precision):
        Matrix.layout = "%%%d.%df,"%(width,precision)
```

我们来运行一下

```python
a = Matrix([[1,2,3,400]])
b = Matrix.zeros((2,3))
print(a)
print(b)
    
#[
# [  1.0,   2.0,   3.0, 400.0, ],
#]

#[
# [  0.0,   0.0,   0.0, ],
# [  0.0,   0.0,   0.0, ],
#]
```

如果我们希望改变输出格式，我们可以使用任意对象修改全局 layout 

```python
a.change_layout(6,8)

print(a.T)
print(b)

#[
# [1.00000000,],
# [2.00000000,],
# [3.00000000,],
# [400.00000000,],
#]

#[
# [0.00000000,0.00000000,0.00000000,],
# [0.00000000,0.00000000,0.00000000,],
#]
```

可以发现所有对象的输出方式都被改变了

如果我们也可以调用 Matrix.change_layout 效果是一样的

```python
Matrix.change_layout(3,0)

print(a)
print(b)

#[
# [  1,  2,  3,400,],
#]

#[
# [  0,  0,  0,],
# [  0,  0,  0,],
#]
```

就我目前遇到的问题来说，classmethod 还是挺好代替 staticmethod 的。可能在元编程方面，staticmethod 会用到的比较多。在构造类装饰器和单例模式中应该有用。

> python 还是挺有意思的，我希望更进一步能看懂这些装饰器的源码实现。把坑先挖在这，回头慢慢填吧。

## EOF