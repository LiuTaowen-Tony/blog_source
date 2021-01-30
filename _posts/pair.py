list = None
tuple = None
dict = None

# List_proto = lambda x0, x1, *xs : (
#     Pair(x0, List(x1, *xs)) if xs else Pair(x0, x1) # when xs == False if it is empty
# )


# Because typing lambda x : lambda y : lambda z is tedious, I cheated a little bit
# f = lambda a,b : a * b
# Curry_(f)(1)(2) = f(1, 2)
Curry_ = lambda f : lambda x : lambda y : f(x, y)
Curry_3 = lambda f : lambda x : lambda y : lambda z : f(x, y, z)

# using lazy evaluation to avoid exceptions
If = Curry_3(lambda cond, lazy1, lazy2: (
    lazy1() if cond else lazy2()
))

# Cons_proto(x)(y)(1) = y
# Cons_proto(x)(y)(0) = x
Cons_proto = Curry_3(lambda x, y, position: (
    If (position == 0)
        (lambda : x)
        (lambda : (If (position == 1)
            (lambda : y)
            (lambda : None)))
))

Top = None
Bottom = None

# List_R : we can only apply foldr on it
# List_proto(Bottom)(1)(2)(3)(Top) = Pair(Pair(Pair(Bottom)(1))(2))(3)
# this is not our desired list since head and tail won't work

Stack_R_proto = Curry_3(lambda x, y, z: (
    Cons_proto(x)(y) if z == Top else
    Stack_R_proto(Cons_proto(x)(y))(z)
))

# Append_R_proto(stack_R)(item) = Pair(stack_R)(item)
Append_R_proto = Cons_proto

Top_R_proto = lambda stack : (
    stack(1)
)

Rest_R_proto = lambda stack : (
    stack(0)
)

Fold_R_proto = Curry_3(lambda f, acc, xs: (
    If (Rest_R_proto(xs) is None)
        (lambda : f
            (Top_R_proto(xs))
            (acc))
        (lambda : Fold_R_proto
            (f)
            (f (Top_R_proto(xs)) (acc))
            (Rest_R_proto(xs)))
))

# since it is not convineint to build stack_r
# build stack_l by "reversing" stack_r

Build_L_Out_Of_R = lambda stack_R : (
    Fold_R_proto
    (lambda x : lambda y :Cons_proto(y)(x))
    (Bottom)
    (stack_R)
)

Stack_L_proto = Curry_3(lambda x, y ,z : (
    (Build_L_Out_Of_R)(Cons_proto(x)(y)) if z == Top else
    Stack_L_proto(Cons_proto(x)(y))(z)
))

Head_L_proto = lambda stack_l : stack_l(1)
Tail_L_proto = lambda stack_l : stack_l(0)

# use fst and snd to avoid clash with list
Fst = "fst"
Snd = "snd"

Pair_proto = Curry_(lambda x, y : (
    lambda position :
    If (position == "fst") 
        (lambda : x) 
        (lambda : If (position == "snd")
            (lambda : y)
            (lambda : None))
))

# Nothing = lambda : None
# Just x = (lambda x : lambda : x)(x)

# a -> [(a,b)] -> Maybe b
Lookup_proto = Curry_(lambda target, xs : (
    If (Tail_L_proto(xs) is None)
        (lambda : lambda : None)
        (lambda : If (Head_L_proto(xs)(Fst) == target)
            (lambda : lambda : Head_L_proto(xs)(Snd))
            (lambda : Lookup_proto(target)(Head_L_proto(xs))))
))

# Object_Root1_proto = (
#     Stack_L_proto
#     (Top)
#     (Pair_proto("show")())
#     (Bottom)
# )

# example : list((map)(f))
# list :: f -> f(data)
# function_applier_proto = lambda f : f (data)
# construct_list :: (Top)(..)(End) -> function_applier_proto
List_Constructor_eg1 = Curry_3(lambda x, y ,z : (
    (lambda f : f((Build_L_Out_Of_R)(Cons_proto(x)(y))))
    if z == Top else
    List_Constructor_eg1(Cons_proto(x)(y))(z)
))

# Object_Constructor_proto = 
# # Lookup_proto = Curry_(lambda target, xs: (
# #     If (Rest_R_proto(xs) is None)
# #         (lambda : raise "Error : item not found <lookup_proto>")
# #         (If (Top_R_proto(xs)(fst) == target)
# #             (lambda : Top_R_proto(xs)(snd))
# #             (lambda : Lookup_proto(target)(Rest_R_proto(xs))))
# # )

# [(a,f)] -> (a -> f)
# input : map , output a function equivalent to nested if
Case_proto1 = lambda map : (
    lambda target : (Lookup_proto)(target)(map)
)

# we need somehow reverse List_R to get List_L
# List_L_proto(1)(2)(3)(endList) = Pair(1)Pair((2)(3))

x = Stack_L_proto(Bottom)(3)(2)(1)(Top)
