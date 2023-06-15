# list=["asfsa","sdsds","ascsqds","asasd"]
# for i in list:
#     print(i)
# ans=[i for i in list]
# print(ans)

# for i in range(101):
#     if i%10==0 :
#         print(i)
        
"its called list comprehensions"
list=[i for i in range(101) if i%10==0]
list=["yes" if i%2==0 else "no" for i in range(10)] 
# print(type((list)))
print(list)

"its called set comprehensions"
# set={i for i in {1,2,3,4,5}} 
# print(type(set))
# print(set)

"its called dic comprehensions  most use for reverse key and values"
# from itertools import *
d1={"c language":"programing language",
        "java":"object orianted language",
        "python":"object orieanted language"}
# print(type(d1))
# d1={value:key for key,value in d1.items()}
# print(d1)
# print(list(combinations(d1,2)))

"its called generator comprehensions"
# value=(f"even {i}" for i in range(10) if i%2==0)
# value=("even" if i%2==0 else "odd" for i in range(10))
value=("even" if i%2==0 else "odd" for i in range(10))
# value=("even" if i%2==0 else "odd")
# print(type(value))
# print(next(value))
# for i in value:
#    print(i)
# print(value.__next__())  
# print(value.__next__())  
# print(value.__next__())  
