---
title: 笔记：逻辑- Part1
date: 2021-01-18 21:21:00
tags:
---

## 句法、语义和证明

一个逻辑系统有三部分组成 syntax, semantics, and proof theory.

## 命题逻辑的句法

这里只是句法，他们不包含任何意思，只是符合某种要求的字符串。只有引入语义之后，他们才有意思。

我们用 BNF 定义句法

原子是可以赋布尔值的变量

T 和 反T 是逻辑关联词！！！没有任何含义

```
atom : "a" | "b" | ... | "z" | atom atom
atomic : atom | "T" | "反T"
negated-atomic : "(~" atomic ")"
literal : atomic | negated-atomic

formula : literal | conjuction | disjucntion 
        | implication | negated-formula
negated-formula : "(~" formula ")"

conjuct : formula
disjuct : formula
antecedent : formula
consequent : formula

conjuction : "(" conjuct "and" conjuct ")"
disjuction : "(" disjuct "or" disjuct ")"
inplication : "(" antecedent "implies" consequent ")"
```

原本书上定义没这么详细，我把具体的名字也写在一起了。

注意：clause 的定义

```
clause : literal | clause "or" literal
```

## 命题逻辑的语义

我认为逻辑公式的语义等同于逻辑命题的取值(不确定对不对)

对逻辑公式求值时，我们需要 situation。situation 不同，逻辑公式的值可能不同。

有时候求值可能看起来很不符合常识。

已知：今天下雨；二大爷被狗咬了。

对 “今天下雨 -> 二大爷被狗咬了” 求值。

其值为真。

所以这再次印证：逻辑语言中的“逻辑”和自然语言中的逻辑是不一样的。

真值只有两个：1 / 0 T 和 反T 不是真值

用真值表定义 formula 的值。

## 谓词逻辑的句法

signature is a collection of constants, and relation symblos with specified arities.

Signature 相当于一个词汇表的感觉

Fixing a L
```
terms : constant in L | variable in L
```

Signature 是词汇表

L-formula 是合法的逻辑命题

L-Structure （一般称为M model）是一个语义系统，是一幅图，我把它理解成一个在 Signature-L 下包含所有真命题的集合。

Soundness 和 Completeness 是有关 “语义系统” 和 “句法系统”的。

Soundness 所有的可证明的都是真的。

Completeness 所有真命题都是可证明的。

Consistency 是说 不能同时证明 A 和 非A。

哥德尔不完备定理是说 。。 不能同时满足 Completeness 和 Consistency。

![截屏2021-04-13 下午5.10.59](/Users/tony/Library/Application Support/typora-user-images/截屏2021-04-13 下午5.10.59.png)

这页 ppt 给我的感觉是怎么把 一阶逻辑转化成命题逻辑。通过 h 函数指定变量的值。

不对，这里是用 h 指明了 free variable 的值。而不是用 h 给 \forall x 赋值![截屏2021-04-13 下午5.18.32](/Users/tony/Library/Application Support/typora-user-images/截屏2021-04-13 下午5.18.32.png)

这里就是用 h 指明 bounded variable 的值，但是给我感觉非常不好，它在用表达能力强的自然语言定义表达能力弱的一阶逻辑。

g = sub x h 的意思是 g 只在指定 x 的值上有所不同![截屏2021-04-13 下午5.28.05](/Users/tony/Library/Application Support/typora-user-images/截屏2021-04-13 下午5.28.05.png)