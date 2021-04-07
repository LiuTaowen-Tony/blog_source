---
title: '笔记：Vector Calculus Note: Week 1'
date: 2020-07-12 23:51:44
tags:
---

# Vector Calculus: Week 1

## 0x00 Lecture 3 & 4 dot product and cross product

点乘没有结合律

叉乘没有交换律和结合律 $\vec A\times \vec B=-\vec B\times \vec A$

两者都有分配律

## 0x01 kronecker delta and Levi-Civita symbols

### Kronecker delta

$$
\delta_{ij}=
\begin{cases}
	1, i=j\\
	0, i\not=j
\end{cases}
$$

### Levi-Civita symbols

$$
\epsilon_{ijk}=
\begin{cases}
1,i,j,k = 1,2,3 \dots\\
-1,i,j,k =3,2,1 \dots \\
0, otherwise
\end{cases}
$$

如果ijk 是123，231，312，$\epsilon_{ijl}=1$

如果ijk 是321，213，132,$\epsilon_{ijk}=-1$

### Einstein summation convention

$\epsilon_{ijk} = \sum\sum\sum \epsilon_{ijk}$

$\delta_{ij}=\sum\sum\delta_{ij}$

$\vec A \cdot \vec B = A_i B_i$

### 另外

$$
\delta_{ij}=\delta_{ji}\\
\delta_{ij}\delta_{jk}=\delta_{ik} \\
\delta_{ii}=3 \\
\delta_{ij}A_{i}=A_{j}\\
\epsilon_{ijk}=\epsilon_{jki}
$$

## 0x02 Some useful operation laws

1. 这个证明我没好好想，总不能全都乘开算吧

$$
\epsilon_{ijk}\epsilon_{lmn}=
\left |
\begin{matrix}
\delta_{il} \quad \delta_{im} \quad \delta_{in}\\
\delta_{jl} \quad \delta_{jm} \quad \delta_{jn}\\
\delta_{kl} \quad \delta_{km} \quad \delta_{kn}
\end{matrix}
\right |\\
= \delta_{il}(\delta_{jm}\delta_{kn}-\delta_{jn}\delta_{km})
- \delta_{im}(\delta_{jl}\delta_{kn}-\delta_{jn}\delta_{kl})
+ \delta_{in}(\delta_{jl}\delta_{km}-\delta_{kl}\delta_{jm})
$$





2. 

$$
\epsilon_{ijk}\epsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{kl}\delta_{jm}
$$

证明

用 $\epsilon_{ijk}\epsilon_{lmn}=\delta_{il}(\delta_{jm}\delta_{kn}-\delta_{jn}\delta_{km})-\delta_{im}(\delta_{jl}\delta_{kn}-\delta_{jn}\delta_{kl})+\delta_{in}(\delta_{jl}\delta_{km}-\delta_{kl}\delta_{jm})$

替换l->i , m->l, n->m
$$
\epsilon_{ijk}\epsilon_{ilm}=\delta_{ii}(\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl})
- \delta_{il} (\delta_{ji}\delta_{km}-\delta_{jm}\delta_{ki})
+ \delta_{im}(\delta_{ji}\delta_{kl}-\delta_{ki}\delta_{jl})
\\
= \delta_{ii}\delta_{jl}\delta_{km}
-\delta_{ii}\delta_{jm}\delta_{kn}
-\delta_{il}\delta_{ji}\delta_{km}
+\delta_{il}\delta_{jm}\delta_{ki}
+\delta_{im}\delta_{ji}\delta_{kl}
-\delta_{im}\delta_{jl}\delta_{ki}
$$
用前面的定律$\delta_{ij}\delta_{jk}=\delta_{ik}$
$$
= \delta_{ii}\delta_{jl}\delta_{km}
-\delta_{ii}\delta_{jm}\delta_{kn}
-\delta_{lj}\delta_{km}
+\delta_{jm}\delta_{kl}
+\delta_{jm}\delta_{kl}
-\delta_{jl}\delta_{km}
\\
=\delta_{jl}\delta_{km}
-\delta_{jm}\delta_{kl}
$$
**这里我不太理解为什么可以把$\delta_{ii}=3$带进去，我想的是后面没有i的项无论i是几这项都是1，所以应该是算出来是负的答案，没想明白qwq**

## 0x03 Vector identities

1. $A\cdot(B\times C)=B\cdot(C\times A)=C\cdot(A \times B)$
2. $(A\times B)\cdot(C\times D)=(A\cdot C)(B\cdot D)-(A\cdot D)(B\cdot C)$
3. $A\times(B\times C)=(A\cdot C)B-(A\cdot B)C$

这里简单证明一下第三条:
$$
[A\times (B\times C)]_i = \epsilon_{ijk}A_j\epsilon_{klm}B_lC_m\\
=\epsilon_{ijk}\epsilon_{klm}A_jB_lC_m\\
=\epsilon_{kij}\epsilon_{klm}A_jB_lC_m\\
=(\delta_{il}\delta_{jm}-\delta_{im}\delta_{lj})A_jB_lC_m\\
=A_jB_iC_j-A_jB_jC_i\\
=(A\cdot C)B-(A\cdot B)C
$$


#### Lagrange Identity

$|\vec A \times \vec B|^2=|A|^2|B|^2-(A\cdot B)^2$
$$
|A\times B|^2 = (A\times B)\cdot(A \times B)\\
=(A \cdot A)(B \cdot B) - (A \cdot B)(B \cdot A)\\

=A^2B^2-(A\cdot B)^2
$$

## EOF

