---
title: 我想清楚我到底讨厌 oop 的什么了
date: 2021-03-20 19:36:46
tags:
---

我认为 oop 最大的问题是模糊了引用和拷贝

对于数字

```cpp
x = 5;
y = x;
x = 6;
cout << "x: " << x << "; y: " << y << endl;
```

显然会输出 `x: 6; y: 5`

但是在 python 中，对于对象

```python
x = obj()
y = x
x.name = "x_name"

print(x.name, y.name)
```

我们会得到`x_name x_name`

这和等号在数字例子中的语义不符，所以这会造成理解困难。

我觉得，不如索性保留引用符号，但是禁止对 primitive type 进行引用，而是只能对 object type 进行引用，这样不存在语义困难。

