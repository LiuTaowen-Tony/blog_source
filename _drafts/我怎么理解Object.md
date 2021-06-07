---
title: 我怎么理解Object
tags:
---

我理解 Object 是一组内存大小一致的物体。

是一种可以任意组合的结构。

和 HTML 的 div 类似。

基本类型的内存大小是不一致的。

但是对于所有 Object，我们都可以假装他们是一样大小的。



Object 是一个对基础类型和Object结构的引用.



Object 其实就是`void *` 

其实可以这样

```c
struct obj_proto
{
  union
  {
    long basic_long;
    double basic_double;
    void * basic_ptr;
  } holder;
  tag_t tag;
};

typedef obj_proto * Object;

Object add(Object a, Object b)
{
  visual(add, dependes on tag)
}

Object append(Object self, Object item)
{
  if (self->tag)
}
```

 