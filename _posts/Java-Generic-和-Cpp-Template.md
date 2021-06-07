---
title: Java Generic 和 Cpp Template
date: 2021-04-06 21:12:59
tags:
---

Java Generic 更像一种类型，它只能作用在 Object （这里的 Object 更像指针）上。如果有需要用到某类型的方法的时候，通过 down cast 和虚表机制来寻找函数。因为 Java 用了 Object 来表示指针，所以在编译的时候，<del>我们已经知道 size 信息</del>，所以我们只编译出一份代码。 



Cpp template 更像是一种宏，他不能用 `<T extends Comparable<T>>`，但是内部允许`ad-hoc`函数调用和操作符重载。为了 零开销抽象 所以 cpp 针对每种不同的类型编译出不同的代码。

```cpp
template <typename T>
T add(T a, T b){
	return a + b;
}

add(1, 2);
add(1., 2.);
```

这份代码会编译出来两个不同的 add，和函数重载类似。

对于 Java

```Java
public static <T extends Addable> T add(T a, T b) { 
  //Addable 是我杜撰的
	return a.add(b);
}

public static void main() {
	add(1, 2);
	add(1., 2.);
}
```

只会生成一份代码，利用虚表寻找 add 真实对应的方法。

