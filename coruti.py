from time import *
def files():
    a=open("rushabh.txt","r")
    a="hello friends my self rushabh and i am computer engineering student and i live in ahmedabad, gujrat"
    sleep(3)
    print("reading complate")
    
    while True:
        # print("yes")
        text=(yield)
        if text in a:
            print("yes")
        else:
            print("no")
f=files()
# f.__next__() #you write next so genrator called
next(f)
f.send("rushabh")
f.send("sandip")
f.colse()
 
# from time import *
# def detailes():
#     info="hello guys this is visuale studio and i work in python and python is so eazy and very help full"
#     sleep(3)
#     print("reading complate")
    
#     while True:
#         text=(yield)
#         if text in info:
#             print("yes this text is define")
#         else:
#             print("sorry this text is not define")
        
# f=detailes()
# # f.__next__()
# next(f)
# k=1
# while k==1:
#     TEXT=input()
#     f.send(TEXT)
