"start python"
# print("hello \\nushabh prajapati")
# print("hello riyu")
# name="rushabh "
# print(name)
# var1="sacvas"
# var2=53.45
# # print(name+var1)
# print("enter the firstname")
# num1=int(input())
# print("enter the lastname")
# num2=int(input())
# print("full name is",num1+num2)

# upper=65 - 90
# lower=97 - 122

# a=round(12.9845274623857,5)
# print(a)

"""string ma last ma aavta pertucular char("je rpartision ma lakhyo hoy ae") ne dur kare tya thi biji string chalu"""
"string mathi badha word dur na thay je rpartition ma lakelu hoy (""last ma aavto char dur thay"")"
k="hello@rushabh@hyy"
# print(k.rpartition('@'))

"zip"
x=[1,2,3]
y=[4,5,6]
# for i,j in zip(x,y):
#         print(set((i,j)))
#         print(list((i,j)))
#         print(tuple((i,j)))
#         print(i,j)
# z=zip(x,y)
# print(z)
# print(dict(z))    
# print(list(z)) #in ans is tuple form
# print(tuple(z))

"any"
# x=[1,2,True]
# a=any(x)
# print(a) #return true if any char or no is true in list,tuple,dict,set any...

"divmod"
# a=divmod(25,3)
# print(a)

"some buildin functions"
# import numpy as np
# name=input().strip()
# nam="         @#$sdlhvods sdnvkpwdfqdq"
# name=nam.strip(" @#$s")
# name="prajapati rushabh genmalbhai"
# name="prajapati-rushabh-genmalbhai" #split convert string to list
# print(np.array(name))
# name=name.split('-')
# name=name.split(' ')
# print(name)
# print(name)
# print(type(name))
# print(name.count("u"))
# print(name.replace("rushabh","sandip"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.find("rush"))
# print(name[0::3])
# name=['r','u','s']
# print(name[::-1])
# print(name.endswith("bhai"))
# print(name.startswith("praja"))
# print(name.title())#.....etc
list=["rushabh","sandip","minaxi","riyu","ramila"]
# numbers=[7,8,5,1,4,2]
# print(numbers)
# numbers.sort()
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(numbers)
# numbers.insert(2,6)
# print(numbers)
# list.remove('sandip',)
# print(list)
# numbers.pop()
# numbers.append(9)
# numbers.reverse()
# print(numbers)
# print(numbers.index(8))
# print(numbers[2:3])
# name=",,.  rushabh .,, ;/"
# print(name.strip(",. ;/"))
# list = [1,2,3]
# list.extend([4,5,6])
# print(list)

"name"
# []=list ,{"":""}=dicstionary , ()=Tuple ,{}=set 

"tupple"
# tp=(4,5,6,54)
# print(tp[0])
# print(tp.index(4))
# print(tp)
        # mutable=can change --->list
        # immutable=can not change --->touple
        
        
"simple program"
# print("enter your age")
# age=int(input())
# if 7<=age<=18:
#         print("you can drive")
# elif age==18:
#         print("you come and fisical text")
# else:
#         print("you can not drive")

"simple program"
# numbers=[23,4,5,6]
# print("enter the number")
# num=int(input())
# if num in numbers:
#          print("yes")
# else:
#         print("no")

"swap no"
# print("sum of two number is",sum)
# a=2
# b=3
# a,b=b,a
# print("a=",a,"b=",b)

"sortform dict"
# list=[["sddg",23],["qe",323],["qwer",21312]]
# print(dict(list))
# print("hello guys",end="")

# list=["rushbah","sandip","minaxi"]
# print(list)
# list.remove("sandip")
# print(list)

# lis=["r","e",8,9,5]
# print(list(reversed(lis)))
# lis.reverse()
# print(lis)

# a=[1,3,2,4]
# c=a[::-1]
# print(a)
# print(c)
# # c=[1,3,2,4]
# print(a==c)
# print(a is c)
 


# print(r"hello \namaste")
# print(ord('k'))
# print(chr(107))

# import sys
# # print(len(sys.argv))   

# name="AAABCAAADE"
# n=len(name)
# k=3
# l=n//k  
# print(name[::l])
# def marge_tools(string,k):
#         n=len(string)
#         l=n//k
#         print(string.split())
        

# string,k=input(),int(input())
# marge_tools(string,k)

"programs"
# for i in range(1,4):
#         for j in range(4-i):
#                 print(end=" ")
#         for k in range(1,i):
#                 print(k,end="")
#         for l in range(i,0,-1):
#                 print(l,end="")
#         print()
        
# import numpy as np
# a=[1,2,3,4,5,6,7,8,9]
# c=a[:2]
# print(a[2::]+a[0:2:])

# input()
# happy=0
# i=['1','2','3']
# A=set(input().split())
# b=set(input().split())
# if i in A:
#         happy +=happy
# elif i in B:
#         happy -=happy
# print(A)
 
# n=int(input())
# lists=set()
# for i in range(n):
#         name=input()
#         lists.add(name)
# print(len(list(lists)))

# n=int(input())
# s=set(map(int,input().split()))
# for i in range(1,4):
#         command=list(input().split())
#         if command[0]=="pop":
#                 s.pop()
#         elif command[0]=="remove":
#                 s.remove(int(command[1]))
#         elif command[0]=="discard":
#                 s.discard(int(command[1]))
       
# sum=0
# for i in s:
#         sum=sum+i
# print(sum)

# n1=input()
# no1=set((map(int,input().split())))
# print(no1)
# n2=input()
# no2=set(map(int,input().split()))
# print(len(no1.union(no2)))

# from collections import Counter
# n=int(input())
# lists=[]
# for i in range(n):
#         lists.append(input())
      
# r=Counter(lists)
# print(len(r))
# for i in r.values():
#         print(i,end=" ")

# name=input()
# s=name.split()
# r=''
# print(s)
# for i in s:
        # r=r+i.capitalize()+" "
        # name=name.replace(i,i.capitalize())
# print(r)

# class sum:
        # def __init__(self,x,y):
                # self.x=x
                # self.y=y
        # def __add__(a, b):
        #         return a.x+b.x
        # def __str__(self):
        #         return "this is "+str(self.x)
        # def __mul__(a, b):
        #         return a.x*b.x
        # def __lt__(a, b):
        #         return a.x<b.x
        # def __gt__(a, b):
                # return a.x>b.x
# r=sum(10,"rushabh")
# k=sum(30,"sandip")
# print(r+k)
# print(r)
# print(r*k)
# print(r.y)
# if r<k:
#         print("less than")
# else:
#         print("gretar than")
# if r>k:
        # print("grater than")
# else:
        # print("less than")
       
# def sum(n):
#         if n<=0:
#                return n
#         else:
#                 return n+sum(n-1)
         
# print(sum(5))

# name=input()
# n=name[::-1]
# if name==n:
#         print("yes")
# else:
#         print("no") 


# no="hello guys this is apple and this is also apple"
# no1="apple"
# print("the count of apple is",no.count(no1))        
# firstname="prajapati"
# lastname=" rushabh"
# print(firstname+lastname)

# def fib(n):
#         if n<=1:
#                 return n
#         else:
#                 return fib(n-1)+fib(n-2)
# for i in range(10):
#         print(fib(i))

# primeno=[]
# for i in range(1,101):
#         for j in range(2,i):
#                 if i%j==0:
#                         break
#         else:
#                 primeno.append(i)
                
# print(primeno)

# import time
# from datetime import date
# def year100(no):
#         if len(no)<=3:
#                 age=int(no)
#                 print("age =",age)
#                 print("enter currentyear")
#                 currentyear=int(input())
#                 print("your 100 year complate in",currentyear+(100-age))
#         else:
#                 year=int(no)
#                 print("year =",year)
#                 # TIME=time.localtime()
#                 # YEAR=TIME.tm_year
#                 today=date.today()
#                 YEAR=today.year
#                 if year>=YEAR:
#                         print("you are not yet born")
#                 else:
#                         YEAR=year+100
#                         print("your 100 year complate in",YEAR)

# no=input()
# year100(no)

# apple=int(input())
# min=int(input())
# max=int(input())
# for i in range(min,max+1):
#         if apple%i==0:
#                 print(i," is divisor by", apple)
#         else:
#                 print(i," is not divisor by", apple)
                
# class vehicle:
#         state="gujrat"
#         def __init__(self,name,speed):
#                 self.name="bus"
#                 self.speed=90                
# class bus(vehcile):
        
# for i in range(1,6):
#         for j in range(1,i+1):
#                 print("*", end=" ")
#         print()
# for i in range(6,0,-1):
#         for j in range(1,i+1):
#                 print("*", end=" ")
#         print()

# strg="radio"
# mid=len(strg)//2
# last=len(strg)-1
# ans=strg[0]+strg[int(mid)]+strg[int(last)]
# print(ans)

# print(25/4)
# print(25//4)
# name = "prajapati rushabh genmalbhai"
# print(len(name))

# name="RuShAbH"
# lower=[]
# upper=[]
# for i in name:
#         if i.islower():
#                 lower.append(i)
#         else:
#                 upper.append(i)
# NAME="".join(lower+upper)
# print(NAME)

# name="rushabh@123.gmail.com"
# digit=0
# character=0
# special=0
# for i in name:
#         if i.isdigit():
#                 digit +=1
#         elif i.isalpha():
#                 character +=1
#         else:
#                 special +=1
# print(digit)
# print(character)
# print(special)

# s1="rudi"
# s2="KHYA"
# s2=s2[::-1]
# s3=""
# for i in range(len(s1)):
#         s3=s3+s1[i]
#         s3=s3+s2[i]
# print(s3)

# s1="rushd"
# s2="rushabh"
# for i in s1:
#         if i not in s2:
#                 break
# else:
#         print("yes")
           
# strs="rushabh123112@gmail.com"
# sum=0
# no=[]
# for i in strs:
#         if i.isdigit():
#                 no.append(i)
#                 sum =sum+int(i)
# avg=sum/len(no)
# print(avg)

# name="prajapati rushabh"
# nam=" ".join(reversed(name.split()))
# nam=name.split()
# print(nam)

# from itertools import product
# lis=[1,2,3]
# ls=[1,2,3]
# pro=product(lis,ls)
# print(tuple(pro))
