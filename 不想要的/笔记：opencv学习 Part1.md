---
title: 笔记：opencv学习 Part1
date: 2020-08-18 23:42:41
tags:
---

读取视频操作

```python
vc = VideoCapture("test.mp4")

#检查是否打开正确

if vc.isOpened():
	open,frame = vc.read()
else:
	open = False

# vc.read 返回两个值，第一个是一个flag表示这一帧有没有图像
# frame表示这一帧的图像的张量

while open: #如果视频正确读取
	ret, frame = vc.read() #read 返回下一帧的图像
	if frame is None: #最后全都读完了就退出
		break
    if ret == True:
        #这里是对图像每一帧的操作
        cv2.imshow("result",frame)
        
        #这是一个比较神奇的操作，waitKey 应该是返回一个Ascii
        #表示键盘按下的按键， & 是按位 and 操作，如果返回值
        #的最后 8 位（0xFF 是 11111111）是 27 （ESC 的
        # Ascii）那么也退出
        if cv2.waitKey(100) & 0xFF == 27:
            break
            
#清理内存
vc.release()
cv2.destroyAllWindows()


    
	
```



open cv 的通道顺序是 b g r 不是 r g b 

```python
b,g,r = cv2.split(pic)

pic  = cv2.merge((b,g,r))

b = pic[:,:,0]
```

卷积的时候需要在图像周围补值

```python
top_size,bottom_size,ls,rs = 50,50,50,50

pic = cv2.copyMakeBorder(
    pic,
    top_size,
    bottom_size,
    ls,
    rs,
    borderType = something
)

```

因为表示图片的数据类型是uint-8

所以相加超过255的时候会做对256取模的操作。

如果想让超过255的值映射到255，那应该用

```python
cv2.add(pic,pic_filter)
```

二值化操作，thershold函数





均值滤波--> 简单平均操作, 类似的还有 boxFilter

```python
blur = cv2.blur(img,(3,3)) #3*3大小的卷积核，参数全部是1

#[1,1,1;1,1,1;1,1,1]

blur = cv2.GaussianBlur(img,(5,5),1) #5*5的卷积核，1应该是正态分布参数

blur = cv2.medianBlur(img,5) #5*5的卷积核，取中值作为结果，效果还是挺好的，注意的是第二个参数是一个数字不是元组
```

横竖拼接数组

```python
a = np.array([[1,1],[1,1]])
b = np.array([[2,2],[2,2]])
c = np.array(([3,3],[3,3]))

np.nstack(a,b,c)

#np.array(
#[[1,1,2,2,3,3],
# [1,1,2,2,3,3]
#)

#还可以用vstack竖着拼接

np.vstack(a,b,c)
```

图像形态学处理

有膨胀腐蚀和开操作闭操作，同时还有梯度操作。

腐蚀，去掉细纹

膨胀，腐蚀的拟操作

开运算，先腐蚀再膨胀

闭运算，先膨胀再腐蚀

梯度，膨胀 - 腐蚀 （留下一个圈圈）

礼帽操作，留下刺刺（膨胀-原来）

黑帽，原来-腐蚀



