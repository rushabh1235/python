from itertools import product
# a=[1,2]
# b=[4,5]
# print(a)
# print(b)
# pro=product(a,b)
# print(list(pro))
# pro=product(a,b,repeat=2)
# print(list(pro))

from itertools import permutations
# a=[1,2,3]
# print(a)
# no=permutations(a)
# print(list(no))
# no=permutations(a,2)
# print(list(no))

from itertools import combinations,combinations_with_replacement
# a=[1,2,3,4]
# print(a)
# no=combinations(a,2)
# print(list(no))
# no=combinations_with_replacement(a,3)
# print(list(no))

from itertools import accumulate
import operator
n=[1,2,3,4,5,2,1,2]
# print(n)
# acu=accumulate(n)
# print(list(acu))
# acu=accumulate(n,func=operator.mul)
# print(list(acu))
# acu=accumulate(n,func=operator.sub)
# print(list(acu))
# n=[1,2,3,4,5,2,1,2,7,3,1,3]
acu=accumulate(n,max)
print(list(acu))
