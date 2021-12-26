---
title: '笔记：Vector Calculus Note: Week 2'
date: 2020-07-12 23:52:44
tags:
---

# Vector Calculus Note: Week 2



## 0x00 Lecture 10 Partial derivatives

### Definition: 

$$\frac{\partial f}{\partial x}=lim_{h\to 0}\frac{f(x+h,y)-f(x,y)}{h}$$

### 双重微分:

如果函数在所有方向上连续: $\frac{\partial^2f}{\partial x\partial y}=\frac{\partial ^2f}{\partial y \partial x}$

证明待会qwq



### 泰勒级数：

$$
f(x,y) = f + xf_x+yf_y+\frac{1}{2}(x^2f_{xx}+2xyf_{xy}+y^2f_{yy})+\frac{1}{6}...
$$

## 0x01 Chain rule

$$
df = f(x+dx,y+dy)-f(x,y)\\
=(f(x+dx,y+dy)-f(x+dx,y))\\
+(f(x+dx,y)-f(x,y))\\
=\frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy
$$

$$
\frac{df}{dr}=\frac{\partial f}{\partial x}\frac{dx}{dr}+\frac{\partial f}{\partial y}\frac{dy}{dr}
$$

## 0x02 Triple Product Rule

$f(x,y,z)=0$

$z=z(x,y)$

$y=(x,z)$

用 chain rule：

$dz = \frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy \\$

$dy = \frac{\partial y}{\partial x}dx+\frac{\partial y}{\partial z}dz \\$

之后代入

$dy = \frac{\partial y}{\partial x}dx+\frac{\partial y}{\partial z}(\frac{\partial z}{\partial x}dx+\frac{\partial z}{\partial y}dy)$

$(1-\frac{\partial y}{\partial z}\frac{\partial z}{\partial y})dy=(\frac{\partial y}{\partial x}+\frac{\partial y}{\partial z}\frac{\partial z}{\partial x})dx$

因为 dy 和 dx 是无关的，所以前面的系数必为0

结论：

$\frac{\partial y}{\partial z}\frac{\partial z}{\partial y} =1$

$\frac{\partial y}{\partial x}\frac{\partial y}{\partial z}\frac{\partial z}{\partial y}= -\bold 1$

因为交换对称，所以换顺序不影响

之后这里补充一个例子

## 0x02 Del Operator

$\nabla = [\frac{d}{dx}\frac{d}{dy}\frac{d}{dz}]^T $

几种用法：

$\nabla f$ 这个是 scalar 乘 vector ，算得是 f 的梯度

$\nabla \cdot \vec f$ 点乘，算的是散度 divergence

$\nabla \times \vec f$ 叉乘， 算的是旋堵 curl

$\nabla \cdot \nabla = \nabla ^2 = \frac{d^2}{dx^2}+\frac{d^2}{dy^2}+\frac{d^2}{dz^2}$	拉普拉斯算子，注意这是一个标量，可以作用于向量场或者标量场

还有特殊的，

$\vec u \cdot \nabla = u_1\frac{d}{dx}+u_2\frac{d}{dy}+u_3\frac{d}{dz}$ ，这里的点乘不能交换顺序，需要注意

它可以作用到向量场或者标量场

