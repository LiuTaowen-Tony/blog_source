---
title: 文章：C++ 引用传递和指针传递
date: 2020-09-16 14:05:21
tags:
---

# C++ 引用传递和指针传递

## 0x00 指针传递

指针传递让函数在内部操作外部的数据，同时在一定程度上也减少了内存的消耗。

这类函数接受指针作为输入，内部可以对指针指向的值做更改。

```cpp
void swap_ptr(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}
```

相当于构造了两个局部指针变量，x，y。这个x，y和原调函数的x，y的地址是不一样的，因为他把输入转化为了指针，但是引用传递里面的变量的地址和原调函数里面变量的地址是一样的。

然后取x，y的值进行交换操作，存在原来的地址上。

对于数组来说，cpp只使用指针变量。这样不需要复制一份数组的内容，之后才传入，可以减少开销。

## 0x01 引用参数

普通的函数是值传递，函数内部的变量是不会影响外部的。

但是引用传递的话，被调函数变量的变化直接反映在主调函数的变量上。相当于对主调函数里的变量的指针指向的值直接做修改。

```cpp
# include <stdio.h>

void swap_ref(int& x,int& y){
    printf("\ninside swap_ref, x,y address: %p,%p\n",&x,&y);
    int temp =x;
    x = y;
    y = temp;
}

void swap(int x,int y){
    printf("\ninside swap, x,y address, %p,%p\n",&x,&y);
    int temp = x;
    x = y;
    y = temp;
}

int main(){
    int x = 5;
    int y = 10;
    printf("before swapping: %d,%d\n",x,y);
    printf("x,y address: %p,%p\n",&x,&y);
    swap(x,y);
    printf("    after ordinary swap: %d,%d (unchanged) \n",x,y);
    swap_ref(x,y);
    printf("    after reference swap: %d,%d\n",x,y);
}
```

输出在这里

```
before swapping: 5,10
x,y address: 0x7ffee2ef26dc,0x7ffee2ef26d8

inside swap, x,y address, 0x7ffee2ef26ac,0x7ffee2ef26a8
    after ordinary swap: 5,10 (unchanged) 

inside swap_ref, x,y address: 0x7ffee2ef26dc,0x7ffee2ef26d8
    after reference swap: 10,5
```

