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
