---
title: 笔记：用 mxnet 实现 Dropout
date: 2020-09-08 00:31:58
tags:
---

# 用 mxnet 实现 Dropout

## 0x00 Dropout是啥

在一个神经网络中，某一个隐藏单元的表达式是
$$
h_i = \phi (x_1w_{1}+x_2w_{2}+...+b)
$$
在使用丢弃法的时候，我们以p为概率丢掉$h_i$,同时为了平衡丢掉一些参数带来的影响，我们同时有1-p的概率对$ h_i$ 做 $h_i := \frac{h_i}{1-p}$的拉伸。

那么相当于我们做了这样的操作：

$h_i' = \frac{\xi_i}{1-p}h_i$

其中$\xi_i$是一个0,1随机变量

这样输入输出的期望值不会变化

因为丢弃同一层参数的可能是一样的，所以神经网络在学习的时候不会过度依赖一层中特定一个神经元。起到了正则化的作用。

## 0x01 在mxnet中的实现

```python
from mxnet import autograd,gluon,init,nd
from mxnet.gluon import loss as gloss,nn

def dropout(X,drop_prob):
    assert 0 <= drop_prob <= 1
    keep_prob = 1 -drop_prob
    mask = nd.random.uniform(0,1,X.shape) < keep_prob
    return mask * X / keep_prob

def net(X):
    X = X.reshape((-1,num_inputs))
    H1 = (nd.dot(X,W1)+b1).relu() #nd.对象直接.relu
    if autograd.is_training():
        #只在训练的时候dropout，为了在test的时候保持稳定
        H1 = dropout(H1,drop_prob1)
    H2 = (nd.dot(H1,W2)+b2).relu()
    if autograd.is_training():
        H2 = dropout(H2,drop_prob2)
    return nd.dot(H2,W3)+b3
```

## 0x02 也可以调用nn模块实现

```python
net = nn.Sequential()
nn.add(
	nn.Dense(256,activation="relu"),
	nn.Dropout(drop_prob1),
	nn.Dense(256,activation="relu"),
	nn.Dropout(drop_prob2),
	nn.Dense(10)
)
net.initialize(init.Normal(sigma=0.1))

```

## EOF

