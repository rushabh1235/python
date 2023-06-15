"enumerate"
# list=[5,4,6,7,8,2,3,9]
# list=['rushabh','sandip','babbu','ramila','minaxi']
# for index,item in enumerate(list):
#     if index%2==0:
#         print(item)
# for item in enumerate(list):
    # print(item)

"import file and use function and variable"
# from function import *
# sum(100)
"OR"
# import function 
# print(function.sum(10))
# print(function.list)

"function decorator" 
"just imagine 1 fuction is alrady define and you something add this function but without use perticular this function"
def dec(sum):
    def inner():
        sum(100)  
    return inner

# @dec
def sum(n):
    sum=0
    for i in range(n):
        sum=sum+i
    print(sum)    
sum(5)
sum=dec(sum) #or @dec
sum()

# import functools
# def dec(ans):
#     # @functools.wraps(ans)
#     def inner():
#         a=ans()+900
#         return a
#     return inner
# # @dec
# def ans():  
#     return 100
# ans=dec(ans) #dec(ans)=inner
# # print(ans.__name__)
# print(ans())

# def dec(prin):
#     def inner(self):
#         if self.name=="rushabh":
#             print("congratulation")
#         else:
#             prin(self)
#     return inner

# class stu:
#     def __init__(self,name,branch):
#         self.name=name
#         self.branch=branch
#     # @dec
#     def prin(self):
#         print(f"hello this is {self.name} and branch is {self.branch}")
    
# s=stu("rushabh","CE")
# s.prin()

# class stu:
#     def __init__(self,name):
#         self.name=name
#     def prints(self):
#         print(self.name)

# s=stu("rushabh")
# s.prints()

# class stu:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self):
#         print(self.name)

# s=stu("rushabh")
# s()


# class stu:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self):
#         e=self.name()
#         return e.upper()

# @stu
# def correct():
#     return "rushabh"

# print(correct())


# class stu:
#     def __init__(self,correc):
#         self.correc=correc
#     def __call__(self,*args):
#         if args[1]==0:
#             return "so sorry"
#         else:
#             return self.correc(*args)
            

# @stu
# def correct(a,b):
#     return a/b

# print(correct(10,5))



# def dec(sum):
#     def inner():
#         sum(100)
#     return inner

# @dec
# def sum(n):
#     s=0
#     for i in range(n):
#         s=s+n
#     print(s)

# sum(10)
# sum=dec(sum)
# sum()

