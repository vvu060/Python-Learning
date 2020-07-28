#Basics

import numpy as np

a = np.array([1,2,3])
b = np.array([[7.0,8.0,9.0],[5.0,6.0,4.0]])
#print(b)

#Get Dimension
print(a.ndim)

#Get Shape
print(b.shape)

#Get Type
print(a.dtype)

#Get Size
print(b.itemsize)

#Get total Size
print(a.size*a.itemsize)
print(b.nbytes)

-----------------------------------------------------------------------------

#Changing Specific elemts

import numpy as np

a = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])

#Get Specific Element [row, column]
print(a[1,6])

#Get Specific Row
print(a[0,:])

#Get Specific Column
print(a[:,0])

#[start_index:end_index:stepsize]
print(a[0, 1:6:2])
print(a[0, 1:-1:2])

#Get Specific element (work outside in)
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b[0,1,0])
b[:,1,:] = [[9,9],[8,8]]
print(b)

---------------------------------------------------------------------------

#Initializing different array

import numpy as np

a = np.zeros((2,2))
print(a)

b = np.ones((3,2,3))
print(b)

c = np.full((2,2), 88, dtype='int32')
print(c)

d = np.full_like(a,4)
print(d)

e = np.random.rand(4,2)
print(e)

f = np.random.random_sample(a.shape)
print(f)

g = np.random.randint(7, size=(3,3))
print(g)

h = np.identity(3)
print(h)

arr = np.array([[1,2,3]])
i = np.repeat(arr,3, axis=0)
print(i)

-------------------------------------------------------------------------------------------

#Initializing below arrary

[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]
 
import numpy as np

output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1]  = 9
print(z)

output[1:4,1:4] = z
print(output)

--------------------------------------------------------------------------------------------

#Copying an array
import numpy as np

a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a)

--------------------------------------------------------------------------------------------

#Mathematical operations on array
import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,0,1,0])
print(a+2)
print(a-2)
print(a/2)
print(a*2)
print(a**2)
print(np.sin(a))
print(np.cos(a))
print(a+b)

------------------------------------------------------------------------------------

#Statistics

import numpy as np

stats = np.array([[1,2,3],[4,5,6]])
print(np.max(stats))
print(np.min(stats, axis=0))
print(np.sum(stats))

----------------------------------------------------------------------------------------

#Reshaping Arrays

import numpy as np

#Reshaping Arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
after = before.reshape((4,2))
print(after)

#Vertical Stacking of arrays
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v1]))

#Horizontal Stacking of arrays
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.hstack([v2,v1]))

-------------------------------------------------------------------------------------------

