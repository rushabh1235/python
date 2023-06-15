from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
# x=[4,6,8]
# y=[1,4,7]
# pyplot.plot(x,y)
# pyplot.title("daigram")
# pyplot.xlabel("X AXIS")
# pyplot.ylabel("Y AXIS")
# pyplot.show()

# x=[1,2,3]
# y=[4,5,6]
# a=[1,2,3]
# b=[7,8,9]
# style.use('ggplot')
# plt.plot(x,y,'c',label='LINE1',linewidth=2)
# plt.plot(a,b,'y',label='LINE2',linewidth=2)
# plt.text(2,5,"point",bbox={"fc":"gree","boxstyle":"circle"})


# plt.title("info")
# plt.xlabel("X -->")
# plt.ylabel("Y -->")

# plt.legend()
# plt.grid(True,color='k')
# plt.show()

"(bar graph) is categorical variable"
# x=[1,3,5,7,9]
# y=[5,2,7,8,2]
# a=[2,4,6,8,10]
# b=[8,6,2,5,6]

# plt.bar(x,y,color='g',width=0.5,label='first')
# plt.bar(a,b,color='k',label='second',width=0.5)
# plt.title("bar graph")
# plt.xlabel("X ==>")
# plt.ylabel("y==>")

# plt.legend()
# plt.show()

"(histogram) is quentatativ variable"
x=[12,15,17,18,19,25,28,36,58,78,48,68,98,72,26,44,77,888,900]
y=[10,20,30,40,50,60,70,80,90,111,123]

plt.hist(x,y,histtype='bar',rwidth=0.5)

plt.title("histogram")
plt.xlabel("-->X-->")
plt.ylabel("-->y-->")

plt.show()

"scater plote"
# x=[1,2,3,7,8,9]
# y=[4,5,6,1,2,3]
# plt.scatter(x,y,color='k',label='scatter',marker="")

# plt.title("histogram")
# plt.xlabel("-->X")
# plt.ylabel("-->y")
# plt.legend()
# plt.show()

"stack plote"
# day=['mon','tue','wed','thu','fri','set']
# work=[9,5,2,4,6,1]
# game=[5,3,4,7,8,2]
# music=[7,3,4,9,1,2]

# plt.plot([],[],label='work',color='m',linewidth=5)
# plt.plot([],[],label='game',color='c',linewidth=5)
# plt.plot([],[],label='music',color='r',linewidth=5)

# plt.stackplot(day,work,game,music,colors=['m','c','r'])

# plt.title("stack or area plote")
# plt.xlabel("X->")
# plt.ylabel("y->")
# plt.legend()
# plt.show()

