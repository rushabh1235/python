"""python Generators are simple way to creating Iterators.an iterater is an object that contaions a countable no of value"""
def fib(n):
    print("start")
    a=-1
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
        yield c
n=int(input("enter no"))
f=fib(n)
print(next(f))
print(next(f))
# print(next(f))
# print(next(f))
"or"
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# "OR"
# for i in f:
    # print(i)

no="123"
print(iter(no))
i=iter(no)
print(next(i))
print(next(f))
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
