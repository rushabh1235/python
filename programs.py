# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return ([i,j])
# lis=[3,2,4]
# np=Solution()
# x=np.twoSum(lis,6)
# print(x)

# from collections import *
# s = sorted(input())
# ans=Counter(s)
# a=ans.most_common(3)
# for key,value in a:
#     print(key,value)    
        
# def merge_the_tools(string, k):
#     s=""
#     c=0
#     for i in string:
#        if i not in s:
#            s=s+i
#        c+=1
#        if c==k:
#             print(s)
#             c=0
#             s=""

# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)                
                    
# def print_formatted(number):
#         for i in range(1,n+1):
#             print(i,oct(i).replace('0o',''),hex(i).replace('0x',''),bin(i).replace('0b',''))
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

    #ABCDCDC
    #CDC
# import re   
# def count_substring(string, sub_string):                            
#     c=0
#     for i,value in enumerate(string):
#         if sub_string in string[i:i+len(sub_string)]:
#             c +=1
#     return c
        
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count=count_substring(string, sub_string)
#     print(count)    

# if __name__ == '__main__':
#     s = input()
#     for i in s:
#         if i.isalnum():
#             print(True)
#             break
#     else:
#         print(False)
#     for i in s:
#         if i.isalpha():
#             print(True)
#             break
#     else:
#         print(False)
#     for i in s:
#         if i.isdigit():
#             print(True)
#             break
#     else:
#         print(False)
#     for i in s:
#         if i.islower():
#             print(True)
#             break
#     else:
#         print(False)
#     for i in s:
#         if i.isupper():
#             print(True)
#             break
#     else:
#         print(False)
        
# import textwrap

# def wrap(string, max_width):
#     s=string
#     ss=""
#     mw=max_width
#     for i,value in enumerate(s):    
#         ss += value
#         if len(ss)==mw:
#             print(ss)
#             ss=""
#     else:
#         print(ss)
#         # return

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     wrap(string, max_width)
    # print(result)
   
   
# 1222311
# (1, 1) (3, 2) (1, 3) (2, 1)

# from itertools import *
# no=input()
# for i,j in groupby(no):
#     print(tuple([len(list(j)),int(i)]),end=" ")

# l=set(map(int,input().split())) 
# no=int(input())
# for i in range(no):
#     r=set(map(int,input().split()))
#     if l.issuperset(r):
#         ans=True
#     else:
#         ans=False
#         break
# print(ans)

# cube = lambda x:x**3
# def fibonacci(n):
#     a=0
#     b=1
#     l=[]
#     for i in range(n):
#         if i<=1:
#             l.append(i)
#         else:
#             ans=a+b
#             l.append(ans)
#             a=b
#             b=ans        
#     return l
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))

# people = [input().split() for i in range(int(input()))]
# people.sort(key=lambda x:x[2])
# for i in people:
#     print(i)

# import operator

# def person_lister(f):
#     def inner(people):
#         # complete the function
#         peoples=sorted(people,key=lambda x:int(x[2]))
#         l=[]
#         for i in peoples: 
#             l.append(f(i))
#         return l
#     return inner

# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')

# l1=[1,2,3,7,8,9]
# l2=[4,5,6]
# for a,b in zip(l1,l2):
#     print(a,b)
# a=zip(l1,l2)
# print(list(a))

# x,y,z=[i for i in input().split()]
# print(x)
# print(y)
# print(z)

# x,y,z=input().split()
# print(x)
# print(y)
# print(z)

# from  collections import * 
# n=int(input())
# a=deque()
# for i in range(n):
#     x=input().split()
#     if x[0]=="append":
#         a.append(x[1])
#     elif x[0]=="appendleft":
#         a.appendleft(x[1])
#     elif x[0]=="pop":
#         a.pop()
#     elif x[0]=="popleft":
#         a.popleft()
# else:
#     x=list(a)
#     for i in x:
#         print(i,end=" ")    

# from collections import *
# def ans(l):
#     large=None
#     while l:
#         if l[0]>=l[-1]:
#             large=l.popleft()
#         else:
#             large=l.pop()
#         if len(l) == 0:
#             return "Yes"
#         if large < l[0] or large < l[-1]:
#             return "No"
#     no_cubes=int(input())
# for i in range(int(input())):
#     l=deque(map(int,input().split()))
#     print(ans(l))

# def print_rangoli(size):
#     for i in range(1,size+1):
#     # for i in range(size,0,-1):
#         print("-"*(size+(size)-(i*2)),end="")
#         # print("-"*((i*2)-2),end="") 
#         for j in range(size,size-i,-1):
#         # for j in range(size,i-1,-1):
#             print(j,end="-")        
#         for k in range(size,size,-1):
#             print(k,end="-")    
#         print()
    
    
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

# import string
# a=string.ascii_lowercase
# print(a)
# size=int(input())
# for i in range(size):
#     l=[]
#     x="-".join(a[i:size])
#     print(x)
#     l.append(x[::-1]+x[1:])
#     print(l)
# for i in l[::-1]:
    # print(i)
    
# from collections import defaultdict
# d=defaultdict(list)
# a=[]
# m,n=list(map(int,input().split()))
# for i in range(m):
#     x=input()
#     d[x].append(i+1)
# print(d)    

# for j in range(n):
#     b=input()
#     a.append(b)
    
# for i in a:
#     if i in d:
#         print(' '.join(map(str, d[i])))
#     else:
#         print("-1") 

# from math import *
# ab=int(input())
# bc=int(input())
# print(round(degrees(atan(ab/bc))),chr(176),sep="")

# import re
# no=int(input())
# p=r'^[+-.]?[0-9]*\.[0-9]+$'
# for i in range(no):
#     s=input()
#     print(bool(re.match(p, s)))

# import math
# print(math.gcd(54,24))

# from collections import Counter
# no=int(input())
# size=map(int,input().split())
# total=Counter(size)
# c=int(input())
# money=0
# for i in range(c):
#     shoes,price=map(int, input().split())
#     if total[shoes]:
#         money += price
#         total[shoes] -= 1
# print(money)    

# a=list(map(int,input().split()))
# call=Counter(a)
# print(call)
# size,price=map(int,input().split())
# print(size,price)

# from collections import defaultdict
# d=defaultdict(list)
# m=int(input())
# for i in range(m):
#     x=input()
#     d[x].append(i+1)
# print(' '.join(map(str,d['a'])))

# from math import *
# total=0
# k,m=map(int,input().split())
# for i in range(k):
#     l=list(map(int,input().split()))
#     print(l)
#     k=sorted(l)
#     a=list(map(lambda x:x**2,l))
#     print(a)
#     r=max(k)
#     total += pow(r,2)
# print(int((total)%m))

# from itertools import product
# a=[]
# k,m=map(int,input().split())
# for i in range(k):
#     l=list(map(int,input().split()[1:]))
#     print(l)
#     a.append(list(map(lambda x:x**2,l)))
#     print(a)
# print(max(list(map(lambda x:sum(x)%m,product(*a)))))

# a=[1,2,3]
# b=[4,5,6]
# d=[7,8,9]
# c=[a,b,d]
# print(c)
# x=product(*c)
# y=product(a,b)
# print(list(x))
# print(list(y))

# import re
# try:
#     print(bool(re.compile(input())))
# except:
#     print(False)

# s="hello rushabh how are you rushabh i hope you doing well"
# ans=re.sub('rushabh', 'sandip', s)
# print(ans)

# import math

# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.np=real
#         self.no=imaginary
#     def __add__(self, no):
#         return Complex(self.real+no.real,self.imaginary+no.imaginary)
#     def __sub__(self, no):
#         return Complex(self.real-no.real,self.imaginary-no.imaginary)
#     def __mul__(self, no):
#         return Complex(self.real*no.real-self.imaginary*no.imaginary,
#                         self.real*no.real+self.imaginary*no.imaginary)
#     def __truediv__(self, no):
#         return self.real/no.real,self.imaginary/no.imaginary
#     def mod(self):
#         return Complex(self.real%no.real,self.imaginary%no.imaginary)
#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# import re
# no=int(input())
# for i in range(no):
#     n=input()
#     try:
#         assert re.match("(\d{4}-){3}\d{4}$",n) or re.match("\d{16}$", n)
#         n=re.sub('-','',n)
#         assert re.match(r'[456]',n)
#         assert not re.search(r'(\d)\1{3,}', n)
#     except:
#         print('invalid')
#     else:
#         print('valid')
      
# a=re.search(r"(\d)\1{3,}",input())
# print(a)

# from datetime import *
# def time_delta(t1, t2):
#     formates="%a %d %b %Y %H:%M:%S %z"
#     T1=datetime.strptime(t1, formates)
#     T2=datetime.strptime(t2, formates)    
#     return abs(T1-T2)

        
# if __name__ == '__main__':

#     t = int(input())
#     for t_itr in range(t):
#         t1 = input()
#         t2 = input()

#         delta = time_delta(t1, t2)
#         print(int(delta.total_seconds()))
        
# from itertools import *
# no=int(input())
# str=input().split()
# n=int(input())
# c=0
# for i in combinations(str,n):
#     if 'a' in i:
#         c += 1
# print(c/len(list(combinations(str,n))))

# if __name__ == '__main__':
#     n = int(input())
#     l=[]
#     for i in range(n):
#         sen=input().split()
#         if sen[0]=='insert':
#             l.insert(int(sen[1]),int(sen[2]))
            
#         elif sen[0]=='remove':
#             l.remove(int(sen[1]))
        
#         elif sen[0]=='append':  
#             l.append(int(sen[1]))
            
#         elif sen[0]=='pop':
#             l.pop()
            
#         elif sen[0]=='reverse':
#             l.reverse()
            
#         elif sen[0]=='sort':
#             l.sort()
            
#         elif sen[0]=='print':
#             print(l)

# n=int(input())
# score=list(set(map(int, input().split())))
# score.sort()
# print(score[-2])

# import math
# import os
# import random
# import re
# import sys

# if __name__ == '__main__':
#     nm = input().split()
#     n = int(nm[0])
#     m = int(nm[1])
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#     k = int(input())
#     arr.sort(key=lambda x:x[k])
#     for i in arr:
#         print(' '.join(map(str,i)))

# s=[1,2,3]
# print('....'.join(map(str, s))

# import pyqrcode
# import png
# from pyqrcode import QRCode

# s="rushabh"
# url=pyqrcode.create(s)
# url.png('myqrcode.png',scale=6)
# url.svg('myqrcode.svg',scale=8)

# import numpy as np
# n,m=map(int,input().split())
# a=np.array([input().split() for i in range(n)],dtype=int)
# b=np.array([input().split() for i in range(n)],dtype=int)
# print(a+b)
# print(a-b)
# print(a*b)
# x=a/b
# print(x.astype(int))
# print(np.mod(a,b))
# print(np.power(a,b))

# from collections import OrderedDict,Counter
# d=OrderedDict()
# item=int(input())
# a=[]
# for i in range(item):
#     n,s,v=input().rpartition(" ")
#     v=int(v)
#     d[n]=v
#     a.append(n)

# x=Counter(a)
# for k1,v1 in d.items():
#     for k2,v2 in x.items():
#         if k1==k2:
#             print("=>",k1,(v1*(v2)))

# k="rushabh prajapati"
# r=k.split()
# print(' '.join(reversed(r)))

# class ans:
#     def allmet(self,s):
#         a=[[]]
#         for i in s:
#             a += [j+[i] for j in a]
#         return a
# a=ans()
# print(a.allmet([4,5,6]))

# a=[[]]
# for i in a:
# print([5]+[4])

# n=input()
# l=[]
# u=[]
# o=[]
# e=[]
# for i in n:
#     if i.islower():
#         l.append(i)
#     elif i.isupper():
#         u.append(i)
#     elif i.isdigit():
#         if int(i)%2!=0:
#             o.append(i)
#         else:
#             e.append(i)
# print(''.join(sorted(l)+sorted(u)+sorted(o)+sorted(e)))

# import math
# class Points(object):
#     def __init__(self, x, y, z):
#         self.x=x
#         self.y=y
#         self.z=z
        
#     def __sub__(self, no):
#         return Points((self.x-no.x),(self.y-no.y),(self.z-no.z))
#     def dot(self, no):
#         return (self.x*no.x)+(self.y*no.y)+(self.z*no.z)
#     def cross(self, no):
#         return Points((self.x*no.y-self.y*no.x),(self.y*no.z-self.z*no.y),(self.z*no.x-self.x*no.z))
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
# if __name__ == '__main__':
#     points = list()
#     for i in range(4):
#         a = list(map(float, input().split()))
#         points.append(a)
#     a, b, c, d = Points(*points[0]),Points(*points[1]),Points(*points[2]),Points(*points[3])
#     x = (b - a).cross(c - b)
#     y = (c - b).cross(d - c)
#     angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
#     print("%.2f" % math.degrees(angle))

# n=int(input())
# no=input().split()
# print(any(a==a[::-1] for a in no) and all(int(i)>0 for i in no)) 
    
# n=int(input())
# for i in range(1001):
#     if i*i==n:
#         print("yes")
#         break
# else:
#     print("no")

# for i,j in d.items():
#     print(j,i)

# l=[]
# for i in range(2,100):
#     for j in range(2,i-1):
#         if i%j==0:
#             break
#     else:
#         l.append(i)
# print(listh(set(l)))

# from functools import reduce
# a=(1,2,3)
# li3=reduce(lambda x,y:x+y,a)
# print(li3)

# a=0
# b=1
# for i in range(10):
#     print(b)
#     a,b=b,a+b

# def fect(n):
#     if n<=1:
#         return n
#     else:
#         return n*fect(n-1)
# print(fect(5))

# a=(1,2,3)
# b=a,4,5,6
# print(b)

# x=2
# a=x*2*(x+2*3%2)
# print(eval('a'))
# print(eval('2*2*2+(2+2)'))

# a=[]
# for i in range(2,101):
#     a.append(i)
# print(a)

# # print(a[1::3])
# n=0
# for i in a[0:]:
#     # print(a[n::i])
#     # n+=1
#     for j in a[n::i]:
#         a.remove(j)
#         # a.append(i)
#         n+=1
# print(a)

# a=int(input())
# b=int(input())
# if a>b:
#     greter=a
# else:
#     greter=b
# while True:
#     if greter % a == 0 and greter % b == 0:
#         print("LCM = ",greter)
#         break
#     greter +=1
   
# let no=123 so no len=3 so no all ele one by one ** 3 and sum of all no == mail no so no called armstrong
# no=input()  
# t=0     
# for i in no:
#     t += int(i) ** len(no)
# if int(no) == t:
#     print("arm")
# else:
#     print("no")

# no=list(map(int, input().split()))

# def ins(no):
#    # insertion sort
#     for i in range(6):
#         min=i
#         for j in range(i,6):
#             if no[j]<no[i]:
#                 min=j
        
#         temp=no[i]
#         no[i]=no[min]
#         no[min]=temp
#    # bubble sort
#     for i in range(6):
#         for j in range(6):
#             if no[i]<no[j]:
#                 temp=no[i]
#                 no[i]=no[j]
#                 no[j]=temp
# no=[7,3,1,2,3,4]
# ins(no)
# print(no)   

# from math import *
# s=input()
# ss=list("".join(s))
# l=len(ss)
# for i in range(1,l,2):
#     k=ss[i]
#     ss[i]=ss[i-1]
#     ss[i-1]=k
# print("".join(ss))

# l1=[1,2,3,9]
# l2=[5,6,7]
# l3=[]
# for i in l1:
#     l3.append(i)
#     for j in l2:
#         l3.append(j)
#         l2.remove(j)
#         break
# print(l3)

# from collections import defaultdict
# def add(*arg):
#     k=defaultdict(int)
#     for i in arg:
#         for m,n in i.items():
#             k[m] +=n
#     return dict(k)
# l1={"r":10,"e":9,"a":3}
# l2={"r":14,"e":12,"a":99}        
# print(add(l1,l2))

# from collections import Counter
# l1={"r":10,"e":9,"a":3,"q":12}
# l2={"r":14,"e":12,"a":99}
# l3 = dict(Counter(l1)+Counter(l2))
# print(l3)

# strong no : let no=120 so now get fectorial of each 1,2 and 0 and than sum of each fec 
#             == no it's called strong no
            
# auto morfic no = let no 120 so squar of no 120 last degit == no ex= 5 squar ==25 so 
#                 last degit of 25 is 5 so 5 is auto morficno
                
# harshad no = let no=145 so sum of each degit div this no so this is harsand not
#             ex 24 so sum of 2+4=6 so this 6 is div to 24 it is harshad no

# abandant number = let no 32 so 32 divisor sum > no so it's called abandant no
#                     ex 16 so 16 divisors 1,2,4,8 so sum=15 so 16<15 so 16 is abandant no