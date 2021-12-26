---
title: 文章：JS Python 和 C++ 的this指针；鸭子类型和猴子补丁
date: 2020-09-18 21:44:07
tags:
---

# JS Python 和 C++ 的this指针；鸭子类型和猴子补丁

> 我对这三种语言其实都只是刚刚入门，一定有许多理解不到位的地方，就在这里记录下我现在的理解吧。

## 0x00 C++

首先我们来聊聊最古老 C++ 里面的 this 指针。

C++ 里的 this 指针据说是为了兼容 C 而设计的。因为当初 C++ 是没有自己的编译器的，所以当时想编译 C++ 程序，我们只能把 C++ 编译到 C 之后再编译到机器码。

我们拿一个例子来解释：

```cpp
class Cat{
    private:
    char *_name;
    
    public:
    void SetName(char* name):
    {
        _name = name;
    }
};
```

如果希望编译到 C 的话，C 里面是没有 class 类型的，所以我们只能用类似的 struct 代替。

```C
struct Cat{
    char *_name;
};

void SetName(struct Cat *this, char * name){
    this->_name = name
}
```

因此，我们使用 this 指针来指代 当前的这个 object 。 在 C++ 中，大部分情况下，我们都可以省略 this 指针，直接操纵属性。

## 0x01 Python

和 C++ 类似，Python 也有一个指向自己的指针 self。但是这个 self 必须显式地表达。它的思想和 C++ 类似，Python 中的方法是类的方法，传入 self 则是把类的方法绑定到 实例 上。（这里和 JavaScript做对比）

我们来举个例子看看

```python
class Class_Name:
    
    name = None
    
    def method_name(self):
        return self.name
  
Object_Name = Class_Name()
Object_Name.name = "oBjEcT"

#我们调用
Object_Name.method_name()
#相当于调用
Class_Name.method_name(Object_Name)

# oBjEcT
# oBjEcT

print(Object_name.method_name)
print(Class_Name.method_name)

#<function method_name at 0x00000000000>
#<bound method method_name of <__main__.Class_Name object at 0x00000000000>>
```

self 就是把应该放到括号里的 object_name 放到了 Class_Name 的位置，在调用函数之前就确定了 self 指向的对象。（这里和 JavaScript做对比）

另外这里提一嘴 动态类型语言 的特性，猴子补丁和鸭子类型

别人说这两个是两个事，我觉得这两个是一个事，但是归根结底，这两个还是两个事。:dog:狗头保命（

### 鸭子类型

鸭子类型是说一个 Python 不会强行检查一个类型，只要接口存在就能调用。

```python
class Dog:
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind
        
    def bark(self):
        return f"whoo~ whoo~ whoo~ {self.name}"

class Person:
    def __init__(self,name,nationality):
        self.name = name
        self.nationality = nationality
        
    def say_hi(self):
        return f"Hi, my name is {self.name}"
    
    def get_nationality(self):
        return self.nationality
    
Dog_1 = Dog("Dog_1","Labrador retriever")
Person_1 = Person("Person_1","Atlantis")

print(Dog.bark(Person_1))
print(Person.say_hi(Dog_1))

#whoo~ whoo~ whoo~ Person_1
#Hi, my name is Dog_1
```

这里狗调用了人的方法，人调用了狗的方法，但是因为人和狗都有 name 属性，所以人和狗都没有报错。

但是如果狗想调用人的getnationality方法，就会报错。

```python
Person.get_nationality(Dog_1)
```

### 猴子补丁

鸭子类型是猴子补丁的基础

如果我们想让狗成精，让狗开始说人话，我们不需要改动狗类的定义。

```python
Dog.bark = Person.say_hi

Dog_1.bark()
#Hi, my name is Dog_1
```

这里动态修改了狗的 bark 方法的那么这时，狗说的就是人话。

上面修改了所有狗的 bark 方法，那么如果我想让单独一只狗会飞怎么办呢？

```python
def fly(self):
    def _fly(*args,**kwargs):
        return f"{self.name} is flying"
   	return _fly

Dog_1.fly = fly(Dog_1)

print(Dog_1.fly())

# Dog_1 is flying
```

这样这只狗就飞了。

看起来猴子补丁没得卵用对吧，但是实际上还是有用的。比如我在调用别人的代码，但是不知道源码的情况下，我可以给原作者定义的类增加或修改功能。或者在做复杂的逻辑的时候，遇到了意外的bug，可以让代码暂停，修改bug之后从出问题的地方继续运行。

值得注意的是，`self` 并不是 Python 的一个关键字，我们完全可以用 `this` 甚至是 `_ `代替。但是，为了程序的可读性，我们按照习惯，依然使用 `self`。

## 0x02 JavaScript

相比 Python 和 C++ ， JavaScript 是更为灵活的语言，就OOP方面来讲。对于JavaScript 它也支持类似 Python 的猴子补丁和鸭子类型，而且更进一步，它的 this 指针是在函数运行时绑定的，这给了 JavaScript 更强的表现力（也更容易出错）。

```javascript
var object1 = {
    name:"ob1",
    getName:function(){
    console.log(this.name);
	}
};

object1.getName()

// ob1

var object2 = {
    name:"ob2",
};

object2.getName = object1.getName
object2.getName()
// ob2
```

像 C++，JavaScript 在定义函数时不需要显式传入 this 指针。但是在调用 实例 的 属性 时，必须使用 this 指针，这里像 Python 。但是和 Python 不一样的是 JavaScript 的指针不是在调用之前就传入的，而是在函数运行时动态传入的。

```javascript
//Python

Person_1.bark = Dog_1.bark
Person_1.bark() 
//Dog_1 已经和 bark 里的 self 指针绑定了
//所以还是 Dog_1
//whoo~ whoo~ whoo~ Dog_1

//JavaScript

object2.getName = object1.getName
object2.getName()
//object1.getName 还没有和 object1绑定
//在运行时才检查是谁调用了这个方法，所以和 object2 绑定
// ob2

//Python 的等价代码

Person_1.bark = Dog.bark(Person_1)

```

JavaScript 在使用猴子补丁的时候比 Python 潇洒一些，不用使用闭包来传入对象指针。可惜这样虽然灵活，但是容易在实际编程的时候指针指向奇怪的地方。

```javascript
var Persona_A = {
    name:"persona_a",
    getName: function(){
        setTimeout(function(){
        	console.log(this.name)
    	})
   	},
}

Persona_A.getName()
//undefined
```

因为 this 指针默认指向函数调用外面一层环境，setTimeout 的环境是 window ，没有 name 属性，所以会输出 undefined。

我们可以用多种方法解决这个问题，比较简单并且和 Python C++ 相似的一种是使用 that 接管 this 指针。

```javascript
var Persona_A = {
    name:"persona_a",
    getName: function(){
        that = this
        setTimeout(function(){
        	console.log(that.name)
    	})
   	},
}

Persona_A.getName()
//persona_a
```

## 0x03 总结

C++ 和 Python 的 实例 都是基于类的 实例。他们的 方法 都是 类 的 方法。在 实例 调用 方法 时，是在调用类的方法，并把 实例 绑定到 类 的 方法 上。

相较于 C++ 可隐式使用 this 指针，Python 的 self 带来了更好的可读性和语法统一性。（`object_name.method_name()` 是 `Class_Name.method_name(self)` 的语法糖）同时也提供了一种实现猴子补丁的实现方法。

然而，这个语法糖对于初学者来说却是十分令人困惑的。大多数教材都不会告诉初学者 `object_name.method_name()` 是一个语法糖。因此初学者会认为这是一种固定写法，并不能理解在定义方法时显式传入 self 带来的统一性的精妙之处。另外，在初学时，如果忘记显式传入 self 变量，报错提示是函数变量数不对，同样会让初学者困惑。但是 Python 这个语法设计无疑是精妙的，只是在错误提示和教材方面做的不够好。

反观 JavaScript，它的 方法 则是 实例 的方法。运行时绑定 this 带来了更好的灵活性，同时在简单的程序中，this 的指向也更加直观。JavaScript 的 this 也挺升了使用猴子补丁的直观性。

this 在运行时绑定 带来的不确定问题 可以用 that 或者 apply/bind/call 来解决。我认为 this 是 JavaScript 的特色之一，契合了 JavaScript 基于原型的面向对象的设计理念。面对复杂的层次关系，我们也可以使用 apply/bind/call 来避免 this 带来的混乱。

对于小的任务来说，猴子补丁和鸭子类型非常方便，灵活，优雅。但是对于大一点的任务，滥用猴子补丁则会让维护变得困难。

## EOF

