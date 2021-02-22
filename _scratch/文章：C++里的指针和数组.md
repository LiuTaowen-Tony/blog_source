---

title: 文章：C++里的指针和数组
date: 2020-09-16 22:48:55
tags:
---

# 指针和数组

结论：

数组就是一个指向数组第一个元素的指针。

```
arr[k] == *(arr+k)
```

当我们声明数组的时候，根据每个元素的内存占用，编译器先空出 列表长度 内存占用的空间。然后把这个块地址区域的其实地址赋给列表的变量名。

```c++
int arr[5] = {1,2,3,4,5};
```

| 地址空间 | 值   | 变量名 |
| -------- | ---- | ------ |
| 0x10     | 0x54 | arr    |
| ...      |      |        |
| 0x54     | 1    |        |
| 0x55     | 2    |        |
| 0x56     | 3    |        |

但是不一样的是 `&`操作符的表现

```c++
int *ptr2 = &ptr1;
int *ptr3 = arr;
int *ptr4 = &arr;

(arr == &arr);
```



| 地址空间 | 值          | 变量名 |
| -------- | ----------- | ------ |
| 0x10     | 0x54        | arr    |
| 0x11     | 0x72        | ptr1   |
| 0x12     | 0x11        | ptr2   |
| 0x13     | 0x54 一样！ | ptr3   |
| 0x14     | 0x54 一样！ | ptr4   |

对于数组来说 `&arr` 和 `arr` 完全一致，



直接输出数组的话，输出的值是数组的第一个元素的地址

```cpp
# include <stdio.h>

int arr[]={1,2,3,4,5};

printf("arr : %p\n",arr);
```

可以用指针的方式访问数组的元素，输出的是数组的第一个元素的值

```cpp
printf("*arr : %d\n",*arr)
```

或者我们也可以使用数组的下标

```cpp
printf("arr[0] : %d\n",arr[0])
```

数组所在的地址储存的是数组第一个元素。它看起来像个指针，但是如果我们取它的地址的话，我们会发现它的地址就是第一个元素的地址。

```cpp
printf("&arr : %p\n",&arr)
```

如果我们想编写一个函数处理数组的话，我们直接把数组传入就行。

```cpp
int sum(int arr[],int length){
    int sum = 0;
    for(int i = 0; i < length; i++){
        sum += arr[i];
    }
    return sum;
}
```

我们也可以用指针指向数组，不需要取地址操作。ptr 的内容是数组第一个元素的地址。

```cpp
int arr[] = {1,2,3,4,5};
int *ptr = arr;

printf("ptr : %p\n",ptr);
```

和数组不一样的是，ptr 和 &ptr 是不同的。而 arr （不加下标或星号）和 &arr 是一样的。

```cpp
printf(" ptr : %p\n",ptr);
printf("&ptr : %p\n",&ptr);
printf(" arr : %p\n",arr);
printf("&arr : %p\n",&arr);
```

但是在定义字符串的时候，我们可以用指针的形式。

```cpp
char *str = "hello,world";
```

不过输出的话就会比较麻烦，需要一个char一个char地输出。(我这里编译不报错，但是不能输出，但是别的地方看他们的程序是可以输出的。)

```cpp
for(;*str!=0x00;str++){
    printf("%c",*str)
}
```

感觉上应该是先生成了一个“hello，world”数组，之后把str指向hello，world。但是因为我现在不知道hello，world的地址，所以没办法直接访问。

```cpp
char str_arr[] = "hello,world";
char *str_ptr = str_arr;

//应该等价于 

char *str_ptr = "hello,world";
```

但是使用指针创建的字符串会被存入常量区，只有读取权限，没有写入权限。这是和数组字符串不同的。

```cpp
int main(){
    char *str = "Hello World!";
    str = "I love C!";  //正确
    str[3] = 'P';  //错误
    return 0;
}
```

另外我们可以使用下标的形式访问数组。据说是在编译优化的时候，数组会被优化成指针，所以下标和指针取值在很多情况下是通用的。

```cpp
char *str_ptr = "hello,world";

printf("str_ptr[0] : %c\n",str_ptr[0]);

char str_arr[] = "hello,world";

printf("*str_arr : %c\n",*str_arr);
```



另外数组的下标和数组名是可以互相替换的。`arr[i]` 和 `i[arr]` 类似于`*arr+i` 和 `*i + arr`

```cpp
int arr[] = {1,2,3};

printf("0[arr] : %d\n",0[arr]);

printf();
```

在作为函数参数的时候，使用指针和数组是一样的。

```cpp
void output_ptr(int *arr,int len){
    for(int i = 0; i < len; i++){
        printf("%d",arr[i]);
    }
}

void output_arr(int arr[],int len){
    for(int i = 0; i < len; i++){
        printf("%d",arr[i]);
    }
}

int main(){
    int arr[] = {1,2,3,4,5};
    int *ptr = arr;

    output_arr(arr,5);
    output_arr(ptr,5);
    output_ptr(arr,5);
    output_ptr(ptr,5);
    //这四个输出是一样的

    return 0;
}
```
