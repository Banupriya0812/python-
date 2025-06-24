
         # Positional-Only Arguments(with /)without keyword arguments 
# def my_function(x,/):
#     print(x)
# my_function(4)



         #  Positional-Only Arguments keyword arguments 
# def my_function(x):
#     print(x)
# my_function(x=3)


        # keyword argument
# def my_function(*,x):
#     print(x)
# my_function(x=3)

          #    positional and keyword 
# def my_function(a,b,/,*,c,d):
#     print(a+b+c+d)
# my_function(5,6,c=8,d=10)


         # recursion- function calling itself 
# def sai_maadhava(i):
#     if i>0:
#         r= i+sai_maadhava(i-1)
#         print(r)
#     else:
#         r=0
#     return r
# print("print the result :")
# sai_maadhava(5)


       #  lambda function with many arguments but 1 expression

# x=lambda s:s-8
# print(x(6))


# s=lambda a,b : a+b
# print(s(4,6))


           # lambda fun inside another function

# def sai(n):
#     return lambda r:r*n

# multiplier=sai(3)
# print(multiplier(10))


# def sai(n):
#     return lambda r:r*n

# trippler=sai(7)
# dubbler=sai(2)
# print(trippler(2))

# print(dubbler(3))


