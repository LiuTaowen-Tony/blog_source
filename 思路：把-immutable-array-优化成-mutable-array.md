---
title: 思路：把 immutable array 优化成 mutable array
date: 2021-04-07 19:04:03
tags:
---

需要 pattern matching 确定一个函数是否是安全的

```
def foo(x, y, z):
	...
	body
	...
	return y, x
	
def main(args):
	...
	y, x = foo(x, y, z)
	...
	return 0
```

对于所有包含数组的函数，只有两种情况

1. 数组“穿过”函数
   - 安全
   - 不安全
2. 数组在这个函数中被生成

首先确定在函数内部确定能不能在同一个 scope 里无冲突。

```
def bar(x, y):
	x = x.add(1)
	x = x.add(2)
	return x
```

那么这个函数对于 输入 `param1` 和 输出 `ret1` 是安全的，如果输入 `param1` 和 输出 `ret1` 是同一个 symbol, 那么可以复用一个数组。

如果有递归调用，那么就是一个sat问题。

对于最外层函数（生成 array 的函数）

```
def baz(x, y):
	x = new Array(5)
	x = x.add(x)
	x = bar(x, x) // 安全函数调用
	print(x)
	return None
```





