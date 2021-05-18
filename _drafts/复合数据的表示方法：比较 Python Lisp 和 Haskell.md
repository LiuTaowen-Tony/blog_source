---
title: 对复合数据、类型和鸭子类型的理解：比较 Python Lisp 和 Haskell
tags:
---

## 复合数据的表示

Python

```python
# (name, age)
xiao_ming = ("XiaoMing", 24)
# something like <tuple <string "XiaoMing"> <int 24>>

# (magnitude, argument)
z = (5, 1.5)

# [(name, age)]
class_member = [xiao_ming, ("GouErDan", 13), ("LiLei", 24)]

xiao_ming_object_dict = {
	"name" : "XiaoMing",
	"age" : 24
}
```

Lisp

```scheme
;; (name age)
(define xiaoming (cons "XiaoMing" 24))

;; (magnitude, argument)
(define z '(5, 1.5))

(define class-member `(,xiaoming ("GouErDan" 13) ("LiLei" 24)))

;;; Lisp 创造对象非常方便，直接一个 quote 就可以了
```

和我的那篇 函数 函数值 表达式 里面类似，cons 函数生成一个 list 对象
list 对象 看起来是 `'(a b c ...)`

`(list a b c) == '(a b c) == (cons (a (cons b (cons c ()))))`

lisp 刻意 “混淆” 了 表达式 和 函数 的区别
`list` 和`'quote` 应该理解为`cons`的语法糖

Haskell

```haskell
-- (name, age)
xiaoming = ("XiaoMing", 24)

-- (magnitude, argument)
z = (5, 1.5)

-- [(name, age)]
classMember = [xiaoming, ("GouErDan", 13), ("LiLei", 24)]
```

看起来和 Python 是一模一样的

## 类型的表示

我理解的类型是数据的标签

Python

```python
class Person():
	def __init__(self, name : str, age : int):
    self.name = name
    self.age = age
    
# <Person "some_name" "some_age">
```

 Python 其实是创造了一个 哈希表 来储存对象的数据，对象的类别其实是一个标签，提示程序员这个对象有这些这些数据可以使用

C

```c
struct person {
	char *name;
	int name_length;
	int age;
};

// 和下面相等

typedef struct {
  char *name;
  int name_length;
  int age;
} person;
```

C 语言则是精打细算内存空间，一个 person 只用 24 个 byte 表示。这里 person 也是一个 tag，表示一个由 char *, int, int 组成的组合

Lisp

```scheme
(define make-person
  (lambda (name age)
    (cons 'person (cons name age))))
```

Lisp 对类型的理解就是 类型是标签。

如果用 Python 表示的话类似于

```python
def make_person(name, age):
  return ("person", (name, age))
```

Haskell

```haskell
data Person = Person String Int

xiaoming :: Person
xiaoming = Person "XiaoMing" 39
```

Haskell 最开始比较让我困惑的地方就是它的 Constructor 有时候和 Type 重名，导致我没分清楚这是两个东西。

## 鸭子类型

我对鸭子类型的理解是极端细化的类型，它完全利用动词定义名词。



比如说对于 加法 运算，两个整数可以相加，所以整数是 Addable。

对于 字符串加法（concat），两个字符串可以相加，所以字符串也是 Addable。

因为 整数 和 字符串 都可以分别施加加法，所以他们都是 Addable。

但是整数可以施加乘法，所以整数也是 Multipliable。

字符串没有这样好的性质，所以字符串不是整数。

整数的其他性质（可以进行的运算）（比如两个整数的形式除法生成一个有理数）定义了整数是整数。



ArrayList 和 TreeSet 都实现了 iterate 接口，生成 iterator 对象（实现 next 和 hasNext 接口），所以他们都是 Iterable。

但是 我们可以用 get 取得列表中的 第 n 个元素，所以列表才被定义为列表。



它的哲学含义类似于 “椅子是可以坐的物体”。“桌子是盛放物体的平台”。如果我坐在桌子上，那么 “桌子” 就是 “椅子” 。



感觉这玩意和 Rust 的思想方式有点类似，它利用 trait 定义接口。



## 后面的不重要

List in python

```python
a = [1, 2, 3, 4] # 生成一个列表
a1 = [x * 2 for x in a] # map
a2 = [x for x in a1 if x % 3 == 0] # filter
s = reduce(lambda x, y : x + y, a2) # reduce
```

Lisp

```scheme
(define a '(1 2 3 4)) ;; 生成一个列表
(define a1
  (map (lambda (x) (* 2 x)) a1)) ;; map
(define a2
  (filter (lambda (x) (eq? 0 (mod x 3))) a1)) ;; filter
(define s
  (fold (lambda (x y) (+ x y)) 0 a2)) ;; reduce / fold
```

Haskell

```haskell
a = [1, 2, 3, 4]
a1 = [x * 2 | x <- a]
a2 = [x | x <- a1, mod 3 x == 0]
s = foldl' 0 (+) a2
```

比较起来是差不多的