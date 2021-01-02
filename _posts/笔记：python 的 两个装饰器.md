---
title: 笔记：python 的 两个装饰器
date: 2020-10-16 23:22:09
tags:
---
# python 的 两个装饰器

> 两个装饰器，一个用来自动把递归转化为记忆化递归。另一个用来强制类型检查。
> 那就记录在这里啦

## 0x00 记忆化递归

> 后来发现 functool 里内置了这个函数

```python
def memorise(func):
    def warpper(*args):
        if memory.get((*args,func)):
            return memory.get((*args,func))
        else:
            memory.update({(*args,func):func(*args)})
            return memory.get((*args,func))
    return warpper

memory = {}
```

就是维护一个字典，如果算过这个函数和参数的组合，那么就自动记录结果。要求是被装饰的对象是纯函数，不然会出问题。

我想写一个检测函数是不是纯函数的装饰器，但是python 好像没有提供接口，打开函数看里面的构造，要到ast层才能解决。

那么用法在这里

```python
@memorise
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

时间消耗

```python
def timeit(func):
    def warpper(*args,**kwargs):
        now = time.time()
        out = func(*args,**kwargs)
        print(time.time() - now)
        return out
    return warpper

@timeit
def main():
    fib(490)

main()

# 0.0024330615997314453
```

只用了 不到 0.024 秒 我们就算完了 第 490 个 斐波那契数。👍

不能直接在 `fib` 外面套 `timeit` 是因为 `fib` 是递归函数。

## 0x01 强制类型检查

第二个装饰器是强制类型检查，因为 python 的类型注释不是强制的。就算我们设置了类型注释，我们也有可能输入非预期的类型。

```python
def foo(a:int,b:float)->str:
    return a + b

print(
    foo("a","b")
)

# ab
```

这样只是方便 IDE 和 程序员 判断一个函数的类型。但是如果我们想用 JIT 技术优化 python 代码的话，这样就不行了。 emm 虽然我不会写 JIT 引擎，不过作为万里长征第一步，确定动态类型代码的类型一定是要解决的。可惜这段代码只会在运行时判断类型，并不能在编译期确定，因此，没有什么卵用。

```python
def typify(*types,out_type=None):

    if out_type is None:
        in_types = (*types,)[0:-1]
        out_type = (*types,)[-1]
    else:
        in_types = (*types,)

    def warpper(func):
        def warpper_(*args,**kwargs):

            values = list({**kwargs}.values())
            extended_args = [*args,] + values
            pairs = list(zip(extended_args,in_types))

            type_matched_flag = reduce(lambda x,y : x and y,map(new_isinst,pairs))

            if type_matched_flag:
                result = func(*args,**kwargs)
                if isinstance(result,out_type):
                    return result
                else:
                    raise TypeError("Output type unmatched")
            else:
                raise TypeError("Input type unmatched")

        return warpper_

    #utils

    new_isinst = lambda x:isinstance(x[0],x[1])

    def reduce(func,iter):
        lst = list(iter)
        if len(lst) == 1:
            return lst[0]
        else:
            fst,snd = lst.pop(),lst.pop()
            lst.append(func(fst,snd))
            return reduce(func,lst)

    return warpper
```

这段代码支持两种使用方式

方式一

```python
@typify(int,int,int)
def sum(a,b):
    return a + b
```

最后一个参数是返回值的类型，前面的参数都是输入参数的类型。

方式二

```python
@typify(int,int,out_type = int)
def sum(a,b):
    return a + b
```

这里我们可以用 `out_type` 指定返回值类型，那么自然剩下的就是输入的类型。

可惜 python 不支持在装饰器里使用柯里化

```python
@typify(int,int)(int)
def sum(a,b):
    return a + b

# 这个是错的，python 不支持这种语法
# 不然可以很优雅的
```

