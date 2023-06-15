from collections import Counter
# a="aaasassassdsddfsdsffdsaaaaafdf"
a=['rushabh','minaxi','sandip','riyansh','rushabh','rushabh','riyansh','sandip','sandip']
# print(a)
ele=Counter(a)
print(ele)
print(dict(ele))
# print(list(ele.elements()))
# print(ele.most_common(1))
# print(ele.most_common(2))
# print(ele.most_common(2)[0][0])
# print(ele.most_common(2)[1][0])

from collections import namedtuple
# stu=namedtuple('stu','name,branch,sem')
# det=stu('rushbah','ce',4)
# print(det)
# student=namedtuple(typename, field_names)
# student=namedtuple("student","name,div,collage")
# s=student("rushabh","4CE-3","silver oak university")
# print(s)

from collections import deque
# n=deque()
n=deque([1,2,3,4])
n.append(4)
# n.append(5)
# n.appendleft(6)
# n.remove(5)
print(list(n))
# n.pop()
# n.extend([1,2,3])
# print(n)
# n.extendleft([1,2,3])
# print(n)
# n.popleft()
# print(type(n))
# n.rotate(2)
# print(n)
# n.rotate(-2)
# print(n)

