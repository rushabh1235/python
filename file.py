"file"
# f=open("sandip.txt","w")
# f=open("sandip.txt","a")
# f=open("sandip.txt","r")
# f.write("hello friends my self sandip \ni am sivil engineering student and i live in ahmedabad, gujrat\n")
# print(f.read())
# f.close()
# print(f.read(7))
# cont=f.read()
# for i in cont:
    # print(i)
# print(f.readline())
# print(f.readline())
# print(f.readlines()) #==>convert string form
# f=open("rushabh.txt","w")
# f.write("my mom is beautiful woman in the word\n")
# print(f.tell())
# print(f.tell())
# f.seek(0)
# print(f.read())
# f.write("rushabh is always topper\n")
# f=open("rushabh.txt","a")
# f.write("rushabh earn 80000 per month")

"with open braket as file"
# with open("sandip.txt") as f:
    # print(f.read())
    # print(f.tell())
    # f.seek(10)
    # print(f.read())
    # print(f.readline())
    # print(f.readline())
    # print(f.readlines())
# with open("rushabh.txt","w") as t:
    # f.write("\nrushabh you are great")
# with open("rushabh.txt","a") as t:
    # t.write("\nthis is file")
    # print(f.tell())
#     f.seek(10)
#     print(f.read())
    # print(f.tell()) 
# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.readline())
# f.seek(10)
# print(f.readline())

"some write detailes and read use file"
# def rushabh():
#     print("1 for write or 2 for read")
#     n=int(input())
#     if n==1:
#         with open("rushabh.txt","a") as r:
#             print("write your 1 for protine and 2 for gymdetailes ")        
#             it=int(input())
#             if it==1:
#                 print("enter your protines\n")
#                 protine=input("\n")
#                 r.write(protine)
#             else:
#                 print("enter your gymdetailes\n")
#                 gym=input("\n")
#                 r.write(gym)
#     else:
#         with open("rushabh.txt") as r:
#             print(r.read()) 
# def sandip():
#     print("1 for write or 2 for read")
#     n=int(input())
#     if n==1:
#         with open("sandip.txt","a") as r:
#             print("write your 1 for protine and 2 for gymdetailes ")        
#             it=int(input())
#             if it==1:
#                 print("enter your protines\n")
#                 protine=input("\n")
#                 r.write(protine)
#             else:
#                 print("enter your gymdetailes\n")
#                 gym=input("\n")
#                 r.write(gym)
#     else:
#         with open("sandip.txt") as r:
#             print(r.read())
# print("1==>rushabh \n2==>sandip\nchoice 1 or 2\n")            
# ch=int(input())
# if ch==1:
#     rushabh()
# else:
#     sandip()
