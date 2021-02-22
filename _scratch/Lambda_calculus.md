# Lambda Calculus

A very brief learning note.

> They are just meaningless tokens. But only you can make them meaningful.

> 说实话，这篇文章写的还是挺混乱的，主要是因为一些符号在数学里和计算机里命名不太一样，我就混着用了。。。

---

## Syntax:

v := "a" | "b" | "c" ... 

$\lambda$-term :=   
<v\> |  
(<v\> <v\>)|  
( "$\lambda$" <v\> .<$\lambda$-term\>)

> e.g. x is a lambda term  
> xy is a lambda term  --application term  
> $\lambda$x.xy is a lambda term  --abstraction term

---

### Omit terms:

Some parentheses will be omitted when it is safe to do so.

> not in BNF

($\lambda$x.<$\lambda$-term>)<$v_{1}$><$v_{2}$> $:=$  ((($\lambda$x.<$\lambda$-term>)<$v_{1}$>)<$v_{2}$>)

**Convention**: association to the left

$\lambda xy.$<$\lambda$-term> $:=  \lambda x.(\lambda y.$<$\lambda$-term>$)$

> I want to stop here for a moment. As you can see, for this one we convert a function with two inputs into a function with one input but out put another function with one input. And this is an example of "Currying". I don't want to go too deep here, because that will be another big bunch of stuff. The main idea is that with successive functions, we can convert multi-input function into single input function, and each function performs the simplest things. Maybe I will put this into post-script.

---

## Evaluation:

Evaluation in $\lambda$ calculus is named as "reduction". The process is deadly simple. There are two types, $\alpha$-Reduction and $\beta$-reduction.

---

### $\alpha$-Reduction

$\alpha$ reduction means that the name of variables can be changed freely. The names are not important.

Example:

$(\lambda xy.x+y) \Leftrightarrow (\lambda ab.a+b)$

A function have the same form is the same function.

---

### $\beta$-Reduction

$\beta$-reduction means to substitute the formal parameter(形参) with actual parameter(实参).

Examples:

($\lambda$x.xyz)(abc) $=$ abcyz

> substitute x with abc

($\lambda$x.xyz)($\lambda$x.x) $=$ (($\lambda$x.x)yz) $=$ yz

> apply $\beta$-reduction for two times

($\lambda$ x.($\lambda$ y.xy))y $=$ ($\lambda$x.($\lambda$t.xt))y $=$ $\lambda$t.yt 

> when there is a conflict in variable name, apply $\alpha$-reduction at first, then $\beta$-reduction

$(\lambda x.(\lambda y.(x(\lambda x.xy))))y \Leftrightarrow (\lambda x.(\lambda t.(x(\lambda q.qt))))y \Leftrightarrow [y/x](\lambda t.(x(\lambda q.qt))) = \lambda t.(y(\lambda q.qt))$

> a more complicated example

> There is a more complicated theory (bound and free variable) talking about in what occasion we need to apply $\alpha$-reduction, but I would not go with that, simply because I think it is too complicated. 
> 
> The main idea is that rename the variables to prevent name clashes.
> 
> The main idea is simple, you do not let variable name be the same as the content you substitute in. Before you substitute the content in, apply $\alpha$-reduction to the variables which is the same as the 

> Here I also want to mention something called "lazy-evaluation", which is useful in modern programming language. In consideration of making this note as brief as possible, I will put this part back in the post script. But it should worth to look at, maybe when you finish all other stuffs.


---

## Let's play with numbers!

"Let there be zero"

$0 \leftarrow \lambda sz.z$

> $\lambda sz.z \Leftrightarrow \lambda s.\lambda x.x$  
> 
>So that 0 is also a function which whatever we input, it will out put the identity function $\lambda$ x.x  
>
>$(0)(x) = \lambda x.x$

> Yes, it is not a thing, but we name it as zero.

Define 1,2,3,...

$1 \leftarrow \lambda sz.s(z) \\
2 \leftarrow \lambda sz.s(s(z))\\
...$

---

### Successor function

Now, let's define successor function.

$S \leftarrow \lambda wyx.y(wyx)$


Maybe we take a look that what does S0 yield

$S0 \Leftrightarrow (\lambda wyx.y(wyx))(\lambda sz.z)\\
= \lambda yx.y((\lambda sz.z)yx)$

> substitute w by 0

$= \lambda yx.y((\lambda z.z)x)\\
= \lambda yx.y(x)\\
\Leftrightarrow \lambda sz.s(z) \Leftrightarrow 1$

Yes, as we expected we get 1!


Then we can look at S1:

$S1 \Leftrightarrow (\lambda wyx.y(wyx))(\lambda sz.s(z))\\
\quad \;\, =\lambda yx.y((\lambda sz.s(z))yx)\\
\quad \;\, =\lambda yx.y((\lambda z.y(z))x)\\
\quad \;\, =\lambda yx.y(y(x)) \Leftrightarrow \lambda sz.s(s(z)) \Leftrightarrow 2$

> Mechanism:  
> - w : copying number into the expression
> - yx : substitute s,z into y,x
> - y(...) : add a layer of y

>Go over Peano theorem:
>
>$0 \in N\\
>n \in N \Rightarrow S(n) \in N\\
>\forall n, S(n)\not=0\\
>n\not=m \Rightarrow S(n)\not=S(m)\\$
>
>Induction principle

The numbers are defined in pretty natural way.

---

### Addition:

> Before introducing addition in $\lambda$ calculus, let's see how we define natural number addition in the "real world".
> 
> $x + 0 = x \quad;\quad x + S(y) = S(x + y)$
> 
> That is it, just as simple as it should be.


As for addition, we do not need to define another operator, numbers and Successor function should be enough.

It is just <num\>S<num\>. e.g. 2S3

Let's see how it works:

We can start with 1+1=2.

$1S1 \Leftrightarrow (\lambda sz.s(z))(\lambda wyx.y(wyx))(\lambda sz.s(z))\\
= (\lambda z.(\lambda wyx.y(wyx))(z))(\lambda sz.s(z))\\
= (\lambda wyx.y(wyx))(\lambda sz.s(z))\\
\Leftrightarrow S1 = 2$

No surprise, 1+1=2.

Now, look at another example:

$3S5 \Leftrightarrow (\lambda sz.s(s(sz)))(\lambda wyx.y(wyx))(\lambda sz.(s(s(s(s(sz))))))\\
= (\lambda z.S(S(Sz)))(\lambda sz.(s(s(s(s(sz))))))$

> Now we can see that applying S to 3 yields 3 Successor functions.

$= S(S(S(\lambda sz.(s(s(s(s(sz)))))))\\
\Leftrightarrow S(S(S5)) = 8$

> Apply Successor function to 5 for 3 times. Now we get 3+5=8

But we want it to be written in the form of $f(n_1,n_2)$.

This function will help us to get there.

$\lambda ab. a(\lambda wyx.y(wyx))b$

Yes, it is just putting the two numbers before and after the successor function.

---

### Multiplication

Before discussing about subtraction, we will look at multiplication, because subtraction is rather hard.

$MUL :=\lambda ab.a((ADD)(b))(0)$

> ADD is the addition function, 0 is $\lambda sz.z$

Let's see, if I am doing it correctly.

$MUL(2)(2) \Leftrightarrow 2(S2)\\
=2(3) \Leftrightarrow (\lambda sz.s(s(z)))(3)\\
=\lambda z.3(3(z)) \Leftrightarrow \lambda z.(\lambda sq. s(s(s(q))))((\lambda sq.s(s(s(q))))(z))\\
=\lambda z.(\lambda sq. s(s(s(q))))((\lambda q.z(z(z(q))))\\
=\lambda z.(\lambda sq. s(s(s(q))))((\lambda q.z(z(z(q))))\\
=\lambda z.(\lambda r.((\lambda q.z(z(z(q))))(((\lambda q.z(z(z(q))))(((\lambda q.z(z(z(q))))(r))))$

我承认我绕晕了，但直觉上我觉得我定义的没错。

> 0 我觉得在这里有很深的数学意义，直觉上觉得这跟0是加法的单位元有关系，但是我没给出一个好的解释。。



---

### Substraction

Subtraction is hard to deal with, because before we define subtraction, we need to define "Whole number" first. Otherwise, we will be in the risk that we subtract one number from another which ended up we get something that we haven't define.

Before look at the definition of subtraction in $\lambda$-Calculus, we will review how we define whole number in the real world. (Or you can say "the world of Maths")

We define whole number use a number pair.

In the following para, I will use lowercase to denote natural number and use uppercase to denote whole number.

>$A := (a,b)$
>
> a whole number can be defined as natural number pair
>
>$(a,b) = (c,d) := a+b=c+d$
>
> (a,b) is identical to (c,d) if and only if a+b=c+d; we have already defined the addition of natural number, here we are using it.
>
>$(a,b)+(c,d):=(a+c,b+d)$
>
> Define whole number addition.
>
>$(a,b)*(c,d):=(ac+bd,ad+bc)$
>
> Define whole number multiplication.
>
>$-(a,b) = (b,a)$
>
> Define "negative numbers".
>
>$X - Y:=X+(-Y)$
>
> Define whole number subtraction.

However, using the definition from the 

>If you know it it’s indeed rather easy: You cannot remove a f so you don’t. Instead you start by zero and count up to the number you want the predecessor of BUT by doing this you remember the last number you saw just before. Having reached the desired number you return the memorized last number … doh you might think – that is exactly how I find the predecessor of an character in the alphabet. Well ok – that is my way for most characters and that is because I – like every other person – do remember the ABC…Z series very well but seem not to have the mental capacity to remember the reversed series as well, so to find the predecessor of Q (I remember in triples so T would be to easy) I count up to Q: ABC…MNOPQ and having this still in cache I present you with P”
> Quote from http://gettingsharper.de/2012/08/30/lambda-calculus-subtraction-is-hard/

First, let's talk about Making pairs. Making pair function is showed as below:

MkPair $:= \lambda ab.\lambda s.(sab)$

a is the first item, and b is the second item, s is the selector function.

Enhance, we can define our selector function as follow.

Fst $:= \lambda ab.a$
Scd $:= \lambda ab.b$

It is quite straight forward.

To test, let's say, P:= MkPair $XY = \lambda s.(sXY)$

P Snd $\Leftrightarrow (\lambda s(sXY))Snd = Snd XY =Y$

Now, I think we have got a **Ring**!! Bravo!!!

Yes, we can define subtraction using number pairs, which is the same as we do in Peano's system.

---

## Boolean Algebra

### True or False

Look at how we define true and false.

$T:=\lambda ab.a$

$F:=\lambda ab.b$

It is quite simple.

---

### AND operator

$AND:=\lambda xy.x(y,F)$

> F is false we just defined

Maybe we can take some examples to test this definition.

$(AND)(T)(T) \Leftrightarrow (\lambda xy.x(y,F))(\lambda ab.a)(\lambda ab.a)\\
=(\lambda y.(\lambda ab.a)(y,F))(\lambda ab.a)\\
=(\lambda y.y)(\lambda ab.a)=T$

For this case, it seems correct. And we can use pseudocode to verify the other cases.

    FUNCTION AND(variable_1:BOOLEAN,variable_2:BOOLEAN) return:BOOLEAN
        if variable_1 == True:
            return variable_2
        else:
            return False

---

### OR operator

$OR:=\lambda xy.x(T,y)$

Easy to verify using pseudocode.

---

### NOT operator

$NOT:=\lambda x.(F,T)$

---

### If-Then-Else

It is still very easy.

$IfThenElse:=\lambda (C)(T\_expr)(F\_expr).C(T\_expr,F\_expr)$

> C is a Boolean expression as condition; T_expr is the expression which is going to be evaluated if the condition is valued true; F_expr is the expression which is going to be evaluated if the condition is valued false.

Let's first make an example:

$IfThenElse(T)(3S5)(2S4)\Leftrightarrow \lambda (C)(T\_expr)(F\_expr).C(T\_expr,F\_expr)(\lambda ab.a)(3S5)(2S4)\\
=(\lambda (T\_expr)(F\_expr).(\lambda ab.a)(T\_expr,F\_expr))(3S5)(2S4)\\
=(\lambda (T\_expr)(F\_expr).T\_expr,)(3S5)(2S4)\\
=(3S5)=8$

---

### Comparing

Sometimes we want to compare between 2 numbers

---

## Recurrsion

With boolean algebra, we can define some recursive expressions. 

### Y-Conbinator

We will examine the following expression Y:

$U:=(\lambda x.xx)\\
Y:=UU=(\lambda x.xx)(\lambda x.xx)$

Let's see what will Y yield if we evaluate it.

$Y \Leftrightarrow (\lambda x.xx)(\lambda x.xx) = (\lambda x.xx)(\lambda x.xx) \Leftrightarrow Y$

It is still Y.

>范式
>
>如果一个λ-项M中不含有任何形为((λx.N1)N2)的子项，则称M是一个范式，简记为n.f.。如果一个λ-项M通过有穷步β-归约后，得到一个范式，则称M有n.f.，没有n.f.的λ-项称为n.n.f.。
>
>通俗的说法是，将一个λ-项进行β-归约，也就是进行实参代入形参的过程，如果通过有穷步代入，可以得到一个不能够再进行代入的λ-项，那么这就是它的范式。如果无论怎样代入，总存在可以继续代入的子项，那么它就没有范式。
>
>例子
>
>M = λx.(x((λy.y)x))y，则Mà y((λy.y)y) à yy。M有一个n.f.。
>
>例子
>
>M =λx.(xx) λx.(xx)，则Màλx.(xx) λx.(xx)=M。注意到M的归约只有唯一的一个可能路径，所以M不可能归约到n.f.。所以M是n.n.f.。
>
>注意这个λx.(xx) λx.(xx)在λ calculus的协调性研究中是一个比较经典的项。((λ x. x x) (λ x. x x))被称为Ω, ((λ x. x x x) (λ x. x x x))被称为 Ω2。

> Y combinator is complex. It has inner relationships with golden diagonal and Godel's incompleteness theorem.


### Factorial

We will use factorial function as an example to see how to define recursive function in lambda calculus.

> 这里的程序比较复杂，我就用计算机的符号写了.

Ordinarily, in imperative programming, factorial function is defined like this.

    Fact(n) := if n==1 then 1 else n*(fact(n-1)) 

We want to do the same thing in $\lambda$ calculus.

    λn. IF (LEQ n 1) 1 (MUL n (FACT (SUB n 1)))
    IF := λabc.a(b,c)

It does not work. Because we haven't explicitly define what is FACT. 

We can expand this expression so that we can see it more clearly.

Then, what about this.

    Let FACT := λn. IF (LEQ n 1) 1 (MUL n (FACT (SUB n 1)))

Still not working. It is just writing the function in another form, but 

>建议看引用的部分，，因为我没想好怎么说。             

    递归的迷思

    敏锐的你可能会发现，就以上这两条公理，我们的lambda语言中无法表示递归函数，为什么呢？假设我们要计算经典的阶乘，递归描述肯定像这样：

    f(n):

    if n == 0 return 1

    return n*f(n-1)

    当然，上面这个程序是假定n为正整数。这个程序显示了一个特点，f在定义的过程中用到了它自身。那么如何在lambda算子系统中表达这一函数呢？理所当然的想法如下：

    lambda n. If_Else n==0 1 n*<self>(n-1)

    当然，上面的程序假定了If_Else是一个已经定义好的三元操作符（你可以想象C的“?:”操作符，后面跟的三个参数分别是判断条件、成功后求值的表达式、失败后求值的表达式。那么很显然，这个定义里面有一个地方没法解决，那就是<self>那个地方我们应该填入什么呢？很显然，熟悉C这类命令式语言的人都知道应该填入这个函数本身的名字，然而lambda算子系统里面的lambda表达式（或称函数）是没有名字的。

    怎么办？难道就没有办法实现递归了？或者说，丘齐做出的这个lambda算子系统里面根本没法实现递归从而在计算能力上面有重大的缺陷？显然不是。马上你就会看到Y combinator是如何把一个看上去非递归的lambda表达式像变魔术那样变成一个递归版本的。在成功之前我们再失败一次，注意下面的尝试：

    let F = lambda n. IF_Else n==0 1 n*F(n-1)

    看上去不错，是吗？可惜还是不行。因为let F只是起到一个语法糖的作用，在它所代表的lambda表达式还没有完全定义出来之前你是不可以使用F这个名字的。更何况实际上丘齐当初的lambda算子系统里面也并没有这个语法元素，这只是刚才为了简化代码而引入的语法糖。当然，了解这个let语句还是有意义的，后面还会用到。

    一次成功的尝试

    在上面几次失败的尝试之后，我们是不是就一筹莫展了呢？别忘了软件工程里面的一条黄金定律：“任何问题都可以通过增加一个间接层来解决”。不妨把它沿用到我们面临的递归问题上：没错，我们的确没办法在一个lambda函数的定义里面直接（按名字）来调用其自身。但是，可不可以间接调用呢？

    我们回顾一下刚才不成功的定义：

    lambda n. If_Else n==0 1 n*<self>(n-1)

    现在<self>处不是缺少“这个函数自身”嘛，既然不能直接填入“这个函数自身”，我们可以增加一个参数，也就是说，把<self>参数化：

    lambda self n. If_Else n==0 1 n*self(n-1)

    上面这个lambda算子总是合法定义了吧。现在，我们调用这个函数的时候，只要加传一个参数self，这个参数不是别人，正是这个函数自身。还是为了简单起见，我们用let语句来给上面这个函数起个别名：

    let P = lambda self n. If_Else n==0 1 n*self(n-1)

    我们这样调用，比如说我们要计算3的阶乘：

    P(P, 3)

    也就是说，把P自己作为P的第一个参数（注意，调用的时候P已经定义完毕了，所以我们当然可以使用它的名字了）。这样一来，P里面的self处不就等于是P本身了吗？自身调用自身，递归！

    可惜这只是个美好的设想，还差一点点。我们分析一下P(P, 3)这个调用。利用前面讲的Beta转换规则，这个函数调用展开其实就是（你可以完全把P当成一个宏来进行展开！）：

    IF_Else n==0 1 n*P(n-1)

    看出问题了吗？这里的P(n-1)虽然调用到了P，然而只给出了一个参数；而从P的定义来看，它是需要两个参数的（分别为self和n）！也就是说，为了让P(n-1)变成良好的调用，我们得加一个参数才行，所以我们得稍微修改一下P的定义：

    let P = lambda self n. If_Else n==0 1 n*self(self, n-1)

    请注意，我们在P的函数体内调用self的时候增加了一个参数。现在当我们调用P(P, 3)的时候，展开就变成了：

    IF_Else 3==0 1 3*P(P, 3-1)

    而P(P, 3-1)是对P合法的递归调用。这次我们真的成功了！

    不动点原理

    然而，看看我们的P的定义，是不是很丑陋？“n*self(self, n-1)”？什么玩意？为什么要多出一个多余的self？DRY！怎么办呢？我们想起我们一开始定义的那个失败的P，虽然行不通，但最初的努力往往是大脑最先想到的最直观的做法，我们来回顾一下：

    let P = lambda self n. If_Else n==0 1 n*self(n-1)

    这个P的函数体就非常清晰，没有冗余成分，虽然参数列表里面多出一个self，但我们其实根本不用管它，看函数体就行了，self这个名字已经可以说明一切了对不对？但很可惜这个函数不能用。我们再来回想一下为什么不能用呢？因为当你调用P(P, n)的时候，里面的self(n-1)会展开为P(n-1)而P是需要两个参数的。唉，要是这里的self是一个“真正”的，只需要一个参数的递归阶乘函数，那该多好啊。为什么不呢？干脆我们假设出一个“真正”的递归阶乘函数：

    power(n):

    if(n==0) return 1;

    return n*power(n-1);

    但是，前面不是说过了，这个理想的版本无法在lambda算子系统中定义出来吗（由于lambda函数都是没名字的，无法自己内部调用自己）？不急，我们并不需要它被定义出来，我们只需要在头脑中“假设”它以“某种”方式被定义出来了，现在我们把这个真正完美的power传给P，这样：

    P(power, 3)

    注意它跟P(P, 3)的不同，P(P, 3)我们传递的是一个有缺陷的P为参数。而P(power, 3)我们则是传递的一个真正的递归函数power。我们试着展开P(power, 3):

    IF_Else 3==0 1 3*power(3-1)

    发生了什么？？power(3-1)将会计算出2的阶乘（别忘了，power是我们设想的完美递归函数），所以这个式子将会忠实地计算出3的阶乘！

    回想一下我们是怎么完成这项任务的：我们设想了一个以某种方式构造出来的完美的能够内部自己调用自己的递归阶乘函数power，我们发现把这个power传给P的话，P(power, n)的展开式就是真正的递归计算n阶乘的代码了。

    你可能要说：废话！都有了power了我们还要费那事把它传给P来个P(power, n)干嘛？直接power(n)不就得了？! 别急，之所以设想出这个power只是为了引入不动点的概念，而不动点的概念将会带领我们发现Y combinator。

    什么是不动点？一点都不神秘。让我们考虑刚才的power与P之间的关系。一个是真正可递归的函数，一个呢，则是以一个额外的self参数来试图实现递归的伪递归函数，我们已经看到了把power交给P为参数发生了什么，对吧？不，似乎还没有，我们只是看到了，“把power加上一个n一起交给P为参数”能够实现真正的递归。现在我们想考虑power跟P之间的关系，直接把power交给P如何？

    P(power)

    这是什么？这叫函数的部分求值(partial evaluation)。换句话说，第一个参数是给出来了，但第二个参数还悬在那里，等待给出。那么，光给一个参数得到的是什么呢？是“还剩一个参数待给的一个新的函数”。其实也很简单，只要按照Beta转换规则做就是了，把P的函数体里面的self出现处皆替换为power就可以了。我们得到：

    IF_Else n==0 1 n*power(n-1)

    当然，这个式子里面还有一个变量没有绑定，那就是n，所以这个式子还不能求值，你需要给它一个n才能具体求值，对吧。这么说，这可不就是一个以n为参数的函数么？实际上就是的。在lambda算子系统里面，如果给一个lambda函数的参数不足，则得到的就是一个新的lambda函数，这个新的lambda函数所接受的参数也就是你尚未给出的那些参数。换句话来说，调用一个lambda函数可以分若干步来进行，每次只给出一部分参数，而只有等所有参数都给齐了，函数的求值结果才能出来，否则你得到的就是一个“中间函数”。

    那么，这跟不动点定理有什么关系？关系大了，刚才不是说了，P(power)返回的是一个新的“中间函数”嘛？这个“中间函数”的函数体我们刚才已经看到了，就是简单地展开P(power)而已，回顾一遍：

    IF_Else n==0 1 n*power(n-1)

    我们已经知道，这是个函数，参数n待定。因此我们不妨给它加上一个“lambda n”的帽子，这样好看一点：

    lambda n. IF_Else n==0 1 n*power(n-1)

    这是什么呢？这可不就是power本身的定义？（当然，如果我们能够定义power的话）。不信我们看看power如果能够定义出来像什么样子：

    let power = lambda n. IF_Else n==0 1 n*power(n-1)

    一模一样！也就是说，P(power)展开后跟power是一样的。即：

    P(power) = power

    以上就是所谓的不动点。即对于函数P来说power是这样一个“点”：当把P用到power身上的时候，得到的结果仍然还是power，也就是说，power这个“点”在P的作用下是“不动”的。

    可惜的是，这一切居然都是建立在一个不存在的power的基础上的，又有什么用呢？可别过早提“不存在”这个词，你觉得一样东西不存在或许只是你没有找到使它存在的正确方法。我们已经看到power是跟P有着密切联系的。密切到什么程度呢？对于伪递归的P，存在一个power，满足P(power)=power。注意，这里所说的“伪递归”的P，是指这样的形式：

    let P = lambda self n. If_Else n==0 1 n*self(n-1) // 注意，不是self(self,n-1)

    一般化的描述就是，对任一伪递归F（回想一下伪递归的F如何得到——是我们为了解决lambda函数不能引用自身的问题，于是给理想的f加一个self参数从而得到的），必存在一个理想f（F就是从这个理想f演变而来的），满足F(f) = f。

    那么，现在的问题就归结为如何针对F找到它的f了。根据F和f之间的密切联系（F就比f多出一个self参数而已），我们可以从F得出f吗？假设我们可以（又是假设），也就是说假设我们找到了一根魔棒，把它朝任意一个伪递归的F一挥，眼前一花，它就变成了真正的f了。这根魔棒如果存在的话，它具有什么性质？我们假设这个神奇的函数叫做Y，把Y用到任何伪递归的函数F上就能够得到真正的f，也就是说：

    Y(F) = f

    结合上面的F(f) = f，我们得到：

    Y(F) = f = F(f) = F(Y(F))

    也就是说，Y具有性质：

    Y(F) = F(Y(F))

    性质倒是找出来了，怎么构造出这个Y却又成了难题。一个办法就是使用抽象法，这是从工程学的思想的角度，也就是通过不断迭代、重构，最终找到问题的解。然而对于这里的Y combinator，接近问题解的过程却显得复杂而费力，甚至过程中的有些点上的思维跳跃有点如羚羊挂角无迹可寻。然而，在这整个Y combinator介绍完了之后我们将会介绍著名的哥德尔不完备性定理，然后我们就会发现，通过哥德尔不完备性定理证明中的一个核心构造式，只需一步自然的推导就能得出我们的Y combinator。而且，最美妙的是，还可以再往下归约，把一切都归约到康托尔当初提出的对角线方法，到那时我们就会发现原来同样如羚羊挂角般的哥德尔的证明其实是对角线方法的一个自然推论。数学竟是如此奇妙，我们由简单得无法再简单的lambda calculus系统的两条公理居然能够导出如此复杂如此令人目眩神迷的Y Combinator，而这些复杂性其实也只是荡漾在定理海洋中的涟漪，拨开复杂性的迷雾我们重又发现它们居然寓于极度的简洁之中。这就是数学之美。

    让我们先来看一看Y combinator的费力而复杂的工程学构造法，我会尽量让这个过程显得自然而流畅[7]：

    我们再次回顾一下那个伪递归的求阶乘函数：

    let P = lambda self n. If_Else n==0 1 n*self(n-1)

    我们的目标是找出P的不动点power，根据不动点的性质，只要把power传给P，即P(power)，便能够得到真正的递归函数了。

    现在，关键的地方到了，由于：

    power = P(power) // 不动点原理

    这就意味着，power作为一个函数（lambda calculus里面一切都是函数），它是自己调用了自己的。那么，我们如何实现这样一个能够自己调用自己的power呢？回顾我们当初成功的一次尝试，要实现递归，我们是通过增加一个间接层来进行的：

    let power_gen = lambda self. P(self(self))

    还记得self(self)这个形式吗？我们在成功实现出求阶乘递归函数的时候不就是这么做的？那么对于现在这个power_gen，怎么递归调用？

    power_gen(power_gen)

    不明白的话可以回顾一下前面我们调用P(P, n)的地方。这里power_gen(power_gen)展开后得到的是什么呢？我们根据刚才power_gen的定义展开看一看，原来是：

    P(power_gen(power_gen))

    看到了吗？也就是说：

    power_gen(power_gen) => P(power_gen(power_gen))


    现在，我们把power_gen(power_gen)当成整体看，不妨令为power，就看得更清楚了：

    power => P(power)

    这不正是我们要的答案么？

    OK，我们总结一下：对于给定的P，只要构造出一个相应的power_gen如下：

    let power_gen = lambda self. P(self(self))

    我们就会发现，power_gen(power_gen)这个调用展开后正是P(power_gen(power_gen))。也就是说，我们的power_gen(power_gen)就是我们苦苦寻找的不动点了！

    铸造Y Combinator

    现在我们终于可以铸造我们的Y Combinator了，Y Combinator只要生成一个形如power_gen的lambda函数然后把它应用到自身，就大功告成：

    let Y = lambda F.

    let f_gen = lambda self. F(self(self))

    return f_gen(f_gen)

    稍微解释一下，Y是一个lambda函数，它接受一个伪递归F，在内部生成一个f_gen（还记得我们刚才看到的power_gen吧），然后把f_gen应用到它自身（记得power_gen(power_gen)吧），得到的这个f_gen(f_gen)也就是F的不动点了（因为f_gen(f_gen) = F(f_gen(f_gen))），而根据不动点的性质，F的不动点也就是那个对应于F的真正的递归函数！

    如果你还觉得不相信，我们稍微展开一下看看，还是拿阶乘函数说事，首先我们定义阶乘函数的伪递归版本：

    let Pwr = lambda self n. If_Else n==0 1 n*self(n-1)

    让我们把这个Pwr交给Y，看会发生什么（根据刚才Y的定义展开吧）：

    Y(Pwr) =>

    let f_gen = lambda self. Pwr(self(self))

    return f_gen(f_gen)

    Y(Pwr)的求值结果就是里面返回的那个f_gen(f_gen)，我们再根据f_gen的定义展开f_gen(f_gen)，得到：

    Pwr(f_gen(f_gen))

    也就是说：

    Y(Pwr) => f_gen(f_gen) => Pwr(f_gen(f_gen))

    我们来看看得到的这个Pwr(f_gen(f_gen))到底是不是真有递归的魔力。我们展开它（注意，因为Pwr需要两个参数，而我们这里只给出了一个，所以Pwr(f_gen(f_gen))得到的是一个单参（即n）的函数）：

    Pwr(f_gen(f_gen)) => If_Else n==0 1 n*f_gen(f_gen) (n-1)

    而里面的那个f_gen(f_gen)，根据f_gen的定义，又会展开为Pwr(f_gen(f_gen))，所以：

    Pwr(f_gen(f_gen)) => If_Else n==0 1 n* Pwr(f_gen(f_gen)) (n-1)

    看到加粗的部分了吗？因为Pwr(f_gen(f_gen))是一个接受n为参数的函数，所以不妨把它令成f（f的参数是n），这样上面的式子就是：

    f => If_Else n==0 1 n*f(n-1)

    完美的阶乘函数！

> https://cgnail.github.io/academic/lambda-4/


> Now, I think we have some basic understanding toward lambda calculus.


# Postscript

## SKI Calculus & $\iota$ Calculus

These are equivalences to $\lambda$ calculus. They are aiming to use less symbols to construct computing systems. I am not going to go too detailed at this part.

### SKI Calculus

$I(x)=x\\
K(x,y)=x\\
S(x,y,z)=xz(yz)$


λ calculus $\rightarrow$ SKI calculus $\rightarrow$ SK calculus $\rightarrow$ ι calculus

## Compiling & Interpreting

Now, I think we have got some basic understanding toward $\lambda$-Calculus. Maybe it is a good time for us to design a interpreter of $\lambda$-Calculus.

I am only familiar with python, so that I will work on python. I know that we can use lambda expression in python but I will not use that, in purpose of understanding this language.

## Currying

## Lazy-evaluation

## bounded and free variables
λ-项中的变量自由出现法则
在一个λ-项中，变量要么是自由出现的，要么是被一个λ符号绑定的。还是以函数的方式来理解变量的自由出现和绑定。例如f(x)=xy这个函数，我们知道x是和函数f相关的，因为它是f的形参，而y则是和f无关的。那么在λx.xy这个λ-项中，x就是被λ绑定的，而y则是自由出现的变量。

直观的理解，被绑定的变量就是作为某个函数形参的变量，而自由变量则是不作为任何函数形参的变量。

Lambda变量绑定规则：

1.         在表达式x中，如果x本身就是一个变量，那么x就是一个单独的自由出现。

2.         在表达式λ x. E中，自由出现就是E中所有的除了x的自由出现。这种情况下在E中所有x的出现都称为被表达式中x前面的那个λ所绑定。

3.         在表达式(MN )中，变量的自由出现就是M和N中所有变量的自由出现。

另一种关于变量的自由出现的规则也许更直接：

1.         free(x) = x

2.         free(MN) = free(M) È free(N)

3.         free(lx • M) = free(M) – {x}

为什么要花大力气来给出变量自由出现的规则，是因为后面的很多地方要用到变量的自由出现的概念。例如α-变换和β-归约。

例子：分析λf.λx.fx中变量的自由出现和绑定状况。

λf.λx.fx =λf.E, E=λx.fx

E=λx.A, A=A1A2, A1=f, A2=x

所以在A中f和x都是自由出现的，

所以E中x是绑定λ x

所以整个公式中f是绑定第一个λ f的。