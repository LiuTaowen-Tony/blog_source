---
title: 笔记：opencv学习 Part2
date: 2020-08-19 10:31:54
tags:
---

图像求梯度，sobel算子
$$
G_y = \begin{bmatrix}
-1&-2&-1\\
0&0&0\\
1&2&1
\end{bmatrix}
\quad
G_x = \begin{bmatrix}
-1&0&1\\
-2&0&2\\
-1&0&1
\end{bmatrix}
$$


```python
dst = cv2.Sobel(src,ddepth,dx,dy,ksize)

#ddepth 是图像深度，不是图像通道数
# dy dx 都是 bool
# ksize 是 kernel size

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
#因为梯度有的是负的，所以要转化为绝对值才能到0-255

#分别计算sobelx和sobely，不建议分别计算

sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
```

Ssharr算子

拉普斯拉算子

#### Canny 边缘提取

1. 高斯滤波--降噪
2. 计算每个像素点的梯度强度和方向
3. 非极大只抑制
4. 双阈值
5. 

非极大值抑制

算出来角度，算线性插值亚像素值的梯度模长，最大值才保留

也可以离散化位8个方向，这样就不用插值了

双阈值

maxVal 《 梯度大于maxVal --》一定是边界

minVal < 梯度 < maxVal ---> 如果周围是边界，那么它才是边界

梯度 < minVal ---> 不是边界

```python
img = cv2.imread()

v1 = cv2.Canny(img,80,150) #参数是minVal 和 maxVal 双阈值
v2 = cv2.Canny(img,50,100)

#阈值比较大的时候只检测比较大的边界，小的时候可以检测小的边界
```

图像金字塔

高斯金字塔（下采样）（图像变小）

- 用高斯核卷积
- 将偶数行列去掉

高斯金字塔（上采样）（图像变大）

- 每个方向扩大为两倍，新增行列用0填充
- 卷积

```python
up = cv2.pyrUp(img)
```

拉普拉斯金字塔

- $L_i = G_i - PyrUp(PyrDown(G_i))$
- G_i 是原始图像
- 提取的东西类似边缘

图像轮廓

```python
cv2.findContours(img,mode,method)

# mode:
    # RETR_EXTERNAL
    # RETR_LIST
	# RETR_CCOMP
    # RETR_TREE 用这个就行了，把所有轮廓镶嵌在一起
    
# method:
	# CHAIN_APPROX_NONE 轮廓线条
    # CHAIN_APPROX_SIMPLE 轮廓顶点
    
cv2.drawContours(img,contours,-1,颜色，2)
# -1是所有的轮廓，0，1，2，3是第几个轮廓
```

还可以指定轮廓近似程度

还可以找外界矩形，外接圆



模版匹配

看看子图像在总图像的哪个地方

逐个像素点比较差异

```python
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

#res 是相关系数矩阵，返回四个参数
```







