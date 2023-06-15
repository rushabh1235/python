import numpy as np
# a=np.array([[1,2,3,4,5,6],[7,8,9,1,2,3]])
# b=np.array([[1,2,3,4,5,6],[7,8,9,1,2,3]])

# b=np.array([[7,8,9,2,3],[1,2,3,1,2],[4,5,1,1,3],[1,2,3,4,2]])
# c=np.array([[1,2,3],[4,5,6]])
# a=np.array([1,2,3,4,5,6,7,8,9])
# print(a)
# print(a[1,0:5:2])
# print(b[[0,1,2],[1,2,3]])
# c=np.zeros((2,3))
# b[1:3,1:4]=c
# print(b)
# print(b[[0,2,3],3:])    
# print(np.cumsum(a))
# print(np.delete(b,2))
# b=np.array([1,2,3,4,1])
# print(c)
# print(np.arange(0,5))
# print(np.array_split(a,2))
# print(a.shape) 
# print(np.shape(a))
# print(np.sqrt(a))
# print(np.std(a))
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# print(np.exp(4))
# print(np.log10(10))

# print(np.dstack((a,b)))
#this function return index no
# print(np.where(a%2==0))

# print(np.sort(b))
# print(np.shape(np.hstack((a,b))))
# print(a.max())
# print(a.min())
# print(a.sum())
# a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(a.shape)
# print(a.ndim)
# print(np.shape(a))
# print(a.ravel())
# print(np.linspace(1,5,20))
# print(a.reshape(3,3))
# print(b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a.itemsize)
# print(a.ndim)
# print(a.dtype)
# print(a.size)
# a=np.array([1,2,3,4,5,6,6,7,8,9])
# print(a.itemsize*a.size)
# print(len(a))
# print(a[0:,1])
# print(np.sqrt(a[1:2,1]))
# print(a[1:2,(1,2)])
# print(np.sqrt(a[1:,2]))
# print(a.sum(axis=0))
# print(a.sum(axis=1))

# a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# b=a.reshape(3,2)
# print(b.ndim)
# print(a.size)
# b=a.reshape(3,2,2)
# print(b)
# print(b[0,1,1])

# print(np.random.random())
# print(np.random.rand(3,3))
# print(np.random.randint(1,10,(3,3)))

# import numpy as np

# abc = ['abc']
# xyz = ['xyz']

# # string concatenation
# print(np.char.add(abc, xyz))    # ['abcxyz']

# print(np.char.add(abc, 'pqr'))  # ['abcpqr']

# # string multiplication
# print(np.char.multiply(abc, 3)) # ['abcabcabc']

# # numpy.char.center: This function returns an array of the required width so that the input string is
# # centered and padded on the left and right with fillchar.

# print(np.char.center(abc, 20, fillchar = '*'))  # ['********abc*********']

# # numpy.char.capitalize(): This function returns the copy of the string with the first letter capitalized.
# print(np.char.capitalize('hello world'))        # Hello world

# # numpy.char.title(): This function returns a title cased version of the input string with the first letter
# # of each word capitalized.
# print(np.char.title('hello how are you?'))      # Hello How Are You?

# # numpy.char.lower(): This function returns an array with elements converted to lowercase. It calls
# # str.lower for each element.
# print(np.char.lower(['HELLO','WORLD']))         # ['hello' 'world']

# # numpy.char.upper(): This function calls str.upper function on each element in an array to return
# # the uppercase array elements.
# print(np.char.upper('hello'))                   # HELLO

# # numpy.char.split(): This function returns a list of words in the input string. By default, a whitespace
# # is used as a separator
# print(np.char.split('Omkar Pathak'))            # ['Omkar', 'Pathak']
# print(np.char.split('2017-02-11', sep='-'))     # ['2017', '02', '11']

# # numpy.char.join(): This method returns a string in which the individual characters are joined by
# # separator character specified.
# print(np.char.join(':','dmy')) 