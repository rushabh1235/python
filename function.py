"f string"
# string Format
# b="born"
# c=2002
# sys=f"rushabh {b} in {c}"
# sys="rushabh %s in %d"%(b,c)
# s="rushabh {} {}"
# sys=s.format(b,c)
# print(sys)

"fibonaci"
# def fibonaci(a,b):
#     for i in range(5):
#         ans=a+b
#         a=b
#         b=ans
#         print(ans,end=" ")
# fibonaci(-1,+1)

"sum program"
# def sum(i):
#     ans=0
#     for i in range(i):
#         ans=ans+i
#     print("sum is =",ans) 
# if __name__=="__main__":
#     sum(5)   

"age program"
# print("enter your age")
# age=int(input())
# print("enter your born year")
# b_year=int(input())
# def year(b_year):
#     c_age=2022-b_year
#     return c_age
# if age>18:
#     c_age=year(b_year)
#     print("you age in 2022 is",c_age)

"change globle veriable"
# n=10
# r=33
# print(n)
# def rushabh():
#     global n #if you change globle veriable so you can pormision  
#     n=n+10
#     print("your ans=",n)
#     r=50
#     print(r)#this print function first search inner veriable if inner veriable is not difine so search globle veriable 
# print(n)  #this print function first search globle veriable if globle veriable is not difine so throw error 
# rushabh()
# print(n)    

"fibonaci use recursion"
# def fib(n):
#     if n<=1:
#         return n
# #     elif n==1:
# #         return(1)
#     else:
#         return(fib(n-1)+fib(n-2))
# for i in range(5):
#     print(fib(i))

"fectorial ele"
# def fibonaci(n):
#     if n==1:
#         return 1
#     else:
#         return n * fibonaci(n-1)
# no=int(input("\nenter no"))
# f=fibonaci(no)
# print(f)

" if__name__== '__main__' use other file"
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# def name(n):
#     if n=='rushabh':
#         return ("right name")
#     else:
#         r=input("enter name")
#         return name(r)
# print("now you are here =>",__name__)
# if __name__=='__main__':
#     n=input("name\n")
#     print(name(n))
#     n=int(input("\nenter the no"))
#     print(sum(n))

"lambda function"
# ans = lambda x,y:x*x+y*y
# print(ans(2,3))


"*args..."
# def name(args): #convert tupel form
    # print(com.upper())
    # for i in args:
        # print(i.upper())
        # "or"
        # print(i)   
# lis=["rushabh","sandip","papa","mummy","minaxi","bhabhi"]
# name("rushabh","sandip","papa","mummy","minaxi","bhabhi")
# com="this is my family"
# rname=["rushabh","sandip","papa","mummy","minaxi","bhabhi","riyansh"] 
# name(rname)#listform
# name(*rname)
# name(lis)#listform
# name(*lis)  
# def num(*args):
#     no=0
#     for i in args:
#         no +=i
#     print(no)
# num(1,2,3) 
# num(1,2,3,4)
# num(1,2,3,4,5,6)

"**kwargs"
# def doc(**kwargs):
    # for key,value in kwargs.items():
    #     print(key,value)  
    # for key in kwargs:
        # print(key)  
    # for i in kwargs.keys():
    #     print(i)
    # for i in kwargs.values():
    #     print(i)  
# lib={"rushabh":"khatu","sandip":"ramila","bhvar":"minaxi"}
# doc(**lib)
# def dic(**kwargs):
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(key)
# dic(name="rushabh",father="genalbhai",mother="manjulaben")
# dic=dict(name="sandip",wife="ramila",son="riyansh")
# print(dic)
# print(dic.keys())
# print(dic.values())
# print(dic.items())