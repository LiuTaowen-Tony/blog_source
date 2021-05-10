怎么解多元线性常微分方程组



啥是多元线性常微分方程组：

$$
\begin{align}
\frac{dr_1}{dt} &= \vec a_1 \vec y_1 + g(t)\\
&\cdots\\
\frac{dr_n}{dt} &= \vec a_n \vec y_n + g(t)\\
\end{align}
$$
可以写作


$$
\frac{d\vec y}{dt} = A\vec y+ \vec g(t)
$$
那么我们可以表示成 
$$
\begin{align}
\mathcal L [\vec y] &= \frac{d\vec y}{dt} - A\vec y\\
\mathcal L [\vec y] &= \vec g(t)
\end{align}
$$
因为都是线性操作符，所以可以先求通解，再求特解
$$
\mathcal L[\vec y] = 0
$$
如果 $A$ 可逆，我们可以用对角矩阵求，如果 A 不可逆，我们可以用乔丹标准型求。



## A 可逆

$$
V^{-1}\frac{d\vec f}{dt} = (V^{-1}AV)\ (V^{-1}\vec y) \\
\frac{d (V^{-1}  \vec f)}{dt} = (V^{-1}AV)\ (V^{-1}\vec y)
$$

我们先求$V^{-1}\vec f$ 然后求 $VV^{-1}\vec f$ 即可

因为
$$
(V^{-1}AV)\ (V^{-1}\vec y) = \Lambda (V^{-1}\vec y)\\
=
\begin{bmatrix}
\lambda & 0 & 0\\
0 & \cdots & 0\\
0 & 0 & \lambda
\end{bmatrix}
(V^{-1}\vec y)
=\frac{d (V^{-1}  \vec f)}{dt}s
$$
这样我们得到了 $n$ 个一元微分方程

我们直接解就行

最后需要记得

$V \times (V^{-1} \vec y_{GS})$



值得注意的是！！！ 如果有虚的特征值也是可以的！！！

可以解出虚的特征向量，之后