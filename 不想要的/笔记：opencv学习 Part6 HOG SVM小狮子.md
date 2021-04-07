---
title: 笔记：opencv学习 Part6 HOG SVM小狮子
date: 2020-08-22 09:55:43
tags:

---

1. 样本
2. 训练
3. 预测

样本

1. 正样本、负样本
2. 获取样本 网络 公司内部 自己收集
3. 自己收集 视频

正样本、负样本

- 尽可能多样
- 环境、干扰多样

训练

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

#1. 参数
PosNum = 820
NegNum = 1931
winSize = (64,128) # 这是小狮子图像的大小
blockStride = (16,16)
blockStride = (8,8)
cellSize = (8,8)
nBin = 9

#2. hog

hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,
                        cellStride,cellSize,nBin)

#3. svm

svm = cv2.ml.SVM_create()

#4. compute hog

featureNum = int(((128-16)/8+1)*((64-16)/8+1)*4*9) #3780
featureArray = np.zeros(((PosNum+NegNum),featureNum),np.float32)
labelArray = np.zeros(((PosNum+NegNum),1),np.float32)

for i in range(0,PosNum):
    fileName = f"pos\{str(i+1)}.jpg"
    img = cv2.imread(fileName)
    hist = hog.compute(img,(8,8))
    for j in range(0,featureNum):
        featureArray[i,j] = hist[j]
    labelArray[i,0] = 1
    
for i in range(0,NegNum):
    fileName = f'neg\{str(i+1)}.jpg'
    img = cv2.imread(fileName)
    hist = hog.compute(img,(8,8))
    for j in range(0,featureNum):
        featureArray[i+PosNum,j] = hist[j]
    labelArray[i+PosNum,0] = -1

#5. label

svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)

#6. train
ret = svm.train(featureArray,cv2.ml.ROW_SAMPLE,labelArray)
#7. pred

alpha = np.zeros((1),np.float32)
rho = svm.getDecisionFunction(0,alpha)
print(rho)
print(alpha)
aphaArray = np.zeros((1,1),np.float32)
support

```

svm

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

rand1 = np.array([
    [155,48],
    [159,50],
    [164,53],
    [168,56],
    [172,60]
])#女生身高体重

rand2 = np.array([
    [152,53],
    [156,55],
    [160,56],
    [172,56],
    [176,65]
])#男生身高体重

label = np.array([[0],[0],[0],[0],[0],[1],[1],[1],[1],[1]])

data = np.vstack((rand1,rand2))
data = np.array(data,dtype = 'float32')#转化成float32

# 0 负样本 1 正样本

#生成svm

svm = cv2.ml.SVM_create()

# 属性设置
"""
类型有
C_SVC -->多分类
NU_SVC -->多分类
ONE_CLASS -->一个样本，用来找样本边界
EPS_SVR ---> 回归
NU_SVR -->回归

核
LINEAR
POLY 多项式
RBF
SIGMOID
CHI2
INTER
"""
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)
#C svm


#xunlian
result = svm.train(data,cv2.ml.ROW_SAMPLE,label)

# visualize the data

width = 50
height = 50
image = np.zeros((height, width, 3), dtype=np.uint8)

# show the decision region


red = (0,0,255)
blue = (255,0,0)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        sampleMat = np.matrix([[j+140,i+40]], dtype=np.float32)
        response = svm.predict(sampleMat)[1]
        if response == 1:
            image[i,j] = red
        elif response == 0:
            image[i,j] = blue

# show the training data

black = (0,0,0)
white = (255,255,255)

for i in range(10):
    cv2.circle(image,(int(data[i][0]-140),int(data[i][1]-40)),3,(black if label[i][0]==0 else white), -1)

# show image

image = cv2.resize(image,(200,200))
cv2.imshow("",image)
cv2.waitKey(0)

pt_data = np.array([[167,55],[162,60]])
print(pt_data)
pt_data = np.array(pt_data,dtype = "float32")

par1,par2 = svm.predict(pt_data)
print(par2)
print(par1)
```