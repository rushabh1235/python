"calculator"
# k=1
# while k==1:
#     num1=int(input("enter the no\n"))
#     num2=int(input("enter the no\n"))
#     print("select +,-,*,%,/")
#     num3=input()
#     if num3=='+':
#         num3=num1+num2
#     elif num3=='-':
#         num3=num1-num2
#     elif num3=='*':
#         num3=num1*num2
#     elif num3=='%':
#         num3=num1%num2
#     elif num3=='/':
#         num3=num1/num2
#     print("ans =",num3)
#     print("enter 1 to contonue")
#     i=int(input())
#     if i==1:
#         print("1 more time")
#     else:
#         break  

"guessnumber"
# num=7
# i=0
# while i<5:
#     int(input())
#     if  number<num:
#         print('guess greter')
#     elif number>num:
#             print('guess lesser')
#     else:
#         print('win')
#         break
#         i=i+1

"r.k" 
# import time
# t=time.time()
# for row in range(5):
#     for col in range(7):
#         if col==0 or (col==2 and row<=2) or (row==0 and col<=2) or (row==2 and col<=2) or (row-col==2) or (col==3 and row>3) or (col==4) or (col-row==2 and row>2) or (col+row==6):
#             print("*",end="  ")
#         else:
#             print(end="   ")
#     print()
# print(time.time()-t)

"k"
# for row in range(5):
#     for col in range(3):
#         if col==0 or (row-col==2) or (col+row==2):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

"hart"
# for row in range(5):
#     for col in range(7):
#         if (row==0 and col!=3) or (col==0 and row<=1) or (col==6 and row<=1) or (row-col==1) or (col+row==7) or (col==3 and row>0 and row<2):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

"  *      "
"  * *    "
"  * * *  " 
# no=int(input("enter the number"))
# for i in range(no):
#     for j in range(i+1):
#         print("*",end=" ")
# print()

"  * * *  " 
"  * *    "
"  *      "
# no=int(input("enter the number"))
# for i in range(no):
#     for j in range(no-i):
#         print("*",end=" ")
#     print()

"leap year"
# from win32com.client import *
# speak=Dispatch("sapi.spvoice")
# speak.Speak("this is leap year program")
# speak.Speak("please enter year")
# # print("enter the year")
# year=int(input())
# if year%4==0:
#     speak.Speak("this year is leap year")
#     print("year is leap year")
# elif year%400==0:
#     speak.Speak("this year is leap year")
#     print("year is leap year")
# else:
#     speak.Speak("this year is  not leap year")
#     print("year is not leap year")

"short hand if_else"
# print("enter your age")
# age=int(input())
# print("you are adulat bro so you can drive") if age>18 else print("you are not adult so you can not drive")
# no1=int(input("enter 1 no"))
# no2=int(input("enter 1 no"))
# print(max(no1,no2))

"avrage"
# from statistics import *
# list=[1,2,3]
# print(mean(list))
"or"
# ans=sum(list)/len(list)
# print(ans)

"even or odd"
# no1=int(input("enter no\n"))
# if no1%2==0:
#     print("this no is even no")
# else:
#     print("this no is odd no")

"fectorial"
# def fect(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fect(n-1)
    
# no=int(input("enter no\n"))
# print(fect(no))

# "prime or not"
# no=int(input("enter no\n"))
# for i in range(2,no):
#     if no%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")