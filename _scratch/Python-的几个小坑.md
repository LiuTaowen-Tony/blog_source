---
title: Python 的几个小坑
date: 2020-10-18 01:36:01
tags:
---

第一个是 python 不支持柯里化函数装饰器 

```python
@typify(float,float)(float)
def distance(x, y):
    return sqrt(x * y)

# This is wrong
# 这个没啥解决方法

```

第二个是单行 `if else ` 语句会先执行两个分支，之后返回正确的分支

```python
cond = lambda p,t,f : t if p else f

print(
    cond(
        (a is None),
        (a),
        (a+1)
    )(5)
)

# 额，这个不算 python 的坑，是我的错
# 因为，这里是函数运算优先级的问题

cond = lambda p,t,f:(
	(lambda x: t)(None)
    if p
    else (lambda x: f)(None)
)

#这样就不会抛出异常了
```

