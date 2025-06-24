
        # create class 
# class myclass:
#   x=8
# print(myclass.x)


           #class calling an object
# class myclass:
#     x=8

# s1=myclass()
# print(s1.x)


            #class with objects (__init__ assign value to object)
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("sai",8)

# print(p1.name)
# print(p1.age)


           #class  object with string format 
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name} {self.age}"
# p=person("sai",8)
# print(p)


            #class objects with methodsfor functioning object
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def sai(self):
#         print("my name is " +self.name)
       
        
# p=person("sai", 8)  
# p.sai()

            #self parameter (any name we can give in place of self)
class person:
    def __init__(maadhava,name,age):
       maadhava.name= name
       maadhava.age=age
    def sai(maadha):
        print("my name is "+ maadha.name)

p1=person("saii",8)
p1.sai()