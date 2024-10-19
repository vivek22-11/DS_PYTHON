

import numpy as np
arr=np.array([7,20,12])
print(arr)


import numpy as np
arr1=np.array([7,20,12])
arr2=np.array([3,5,2])
print(arr1)
print(arr1.dtype)


import numpy as np
arr=np.array([10,20,30])
print(arr)


#create a multi dimenstional array
import numpy as np
arr=np.array([[10,20,30],[40,50,60]])
print(arr)


import numpy as np
arr=np.array([10,20,30,40],ndmin=2)
print(arr)

import numpy as np
arr=np.array([10,20,30,40],ndmin=3)
print(arr)

# '''change the data type'''
import numpy as np
arr=np.array([10,20,30],dtype=complex)
print(arr)

import numpy as np
arr=np.array([10,20,30],dtype=float)
print(arr)

#'''get dimension of the array'''
import numpy as np
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)


#'''finding the size of each item in the array'''
import numpy as np
arr=np.array([10,20,30])
print("each item conatin in byte :",arr.itemsize)


#'''get the data type of each array item'''
import numpy as np
arr=np.array([10,20,30])
print("each item is of the type :",arr.dtype)


#'''get the shape and size of array'''
import numpy as np
arr=np.array([[10,20,30,40],[60,70,80,90]])
print("Array Size:",arr.size)
print("Array Shape:",arr.shape) 


#'''creating array from list with type float'''
import numpy as np
arr=np.array([[10,20,30],[40,50,60]],dtype='float')
print("Array create by using list:\n",arr)


#'''create a sequence of integer using arange()'''
import numpy as np
arr=np.arange(0,20,3)
print("a sequential array with steps of 3:\n",arr)



#'''Array indexing in numpy'''
import numpy as np
arr = np.arange(11)
print(arr)
print(arr[2])
print(arr[-2])


#'''multi dimenstional array indexing'''
import numpy as np
arr=np.array([[10,20,30,40,50],[60,70,80,90,100]])
print(arr)
print(arr.shape)
print(arr[1,1])
print(arr[0,4])
print(arr[1,-1])


#'''access array elements using slicing [Start:End:Step]''' 
import numpy as np
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]                          
print(x)
x1=arr[-2:3:-1]
print(x1)
x2=arr[-2:10]
print(x2)


#'''indexing in numpy'''
import numpy as np
arr=np.array([[10,20,10,40],
              [40,50,70,90],
              [60,10,70,80],
              [30,90,40,30]])
print(arr)
x=arr[:3,::2]
print(x)


import numpy as np
arr = np.arange(35).reshape(5,7)
print(arr)


import numpy as np
arr = np.arange(12).reshape(3,4)
print(arr)


import numpy as np
rows = np.array([False,True,True])
wanted_rows = arr[rows, : ]
print(wanted_rows)


#'''convert one dimensional array to list'''

import numpy as np
array = np.array([10,20,30,40]) 
print("array:",array)
print(type(array))

lst = array.tolist()
print("list:",lst)
print(type(lst))


#'''convert multi dimensional array to list'''

import numpy as np
lst = [20,40,60,80]
array = np.array(lst)
print("array:",array)


lst = [20,40,60,80]
array = np.asarray(lst)
print("Array:",array)
print(type(array))

#numpy array properties
'''
ndarray.shape
ndarray.ndim
ndarray.itemsize
ndarray.size
ndarray.dtype
'''
#'''ndarray.shape to get the shape of array '''

import numpy as np
array = np.array([[1,2,3],[4,5,6]])
print(array.shape)
print(array)

import numpy as np
array = np.array([[1,2,3],[4,5,6]])
array.shape=(3,2)
print(array)


import numpy as np
array = np.array([[1,2,3],[4,5,6]])
new_array=array.reshape(3,2)
print(new_array)



#'''ndarray.ndim is used to find the diemension'''

import numpy as np
array = np.array([[1,2,3,4],
                  [7,8,6,7],
                  [9,10,11,12]])
print(array.ndim)



#'''apply arithmetic operations on numpy arrays'''

import numpy as np
arr1 = np.arange(16).reshape(4,4)
arr2 = np.array([1,3,2,4])
print(arr1)
print(arr2)


add_arr = np.add(arr1,arr2)
print(f"Adding two arrays: \n{add_arr}")

sub_arr=np.subtract(arr1,arr2)
print(f"subtracting two arrays: \n{sub_arr}")

mul_arr=np.multiply(arr1,arr2)
print(f"multiplying two arrays: \n{mul_arr}")

div_arr=np.divide(arr1,arr2)
print(f"Dividing two arrays: \n{div_arr}")


#'''numpy.reciprocal() to perform reciprocal operation'''

import numpy as np
arr1 = np.array([20,45,32,10])
rep_arr1 = np.reciprocal(arr1)
print(f"after applying reciprocal function  to array:\n{rep_arr1}")


import numpy as np
arr1 =np.array([3,4,5])
pow_arr1 = np.power(arr1, 3)
print(f"after applying power function to array:\n{pow_arr1}")


import numpy as np
arr1 =np.array([3,4,5])
arr2 =np.array([6,7,8])
print("first array: \n",arr1)
print("second array: \n",arr2)
pow_arr2 = np.power(arr1, arr2)
print(f"after applying power function to array:\n{pow_arr2}")


from numpy import array
l=[1.0,2.0,3.0]
a=array(l)
print(a)
print(a.shape)
print(a.dtype)


from numpy import empty
a= empty([3,3])
print(a)


from numpy import zeros
a = zeros([3,3])
print(a)

from numpy import ones
a = ones([3,3])
print(a)


#'''create array with vstack (vartical stack)'''

from numpy import array
from numpy import vstack
a1=array([1,2,3])
print(a1)
a2=array([4,5,6])
print(a2)
a3=vstack((a1,a2))
print(a3)
print(a3.shape)


#'''create array with hstack (horizontal stack)'''
from numpy import array
from numpy import hstack
a1=array([1,2,3])
print(a1)
a2=array([4,5,6])
print(a2)
a3=hstack((a1,a2))
print(a3)
print(a3.shape)

#'''INDEX'''

from numpy import array
data = [11, 22, 33, 44, 55]
data = array(data)
print(data)
print(type(data))

from numpy import array
data = [[11, 22],
[33, 44],
[55, 66]]
data = array(data)
print(data)
print(type(data))

from numpy import array
data =array([11,22,33,44,55])
print(data[0])
print(data[4])

from numpy import array 
data=array([11,22,33,44,55])
print(data[5])

from numpy import array
data =array([11,22,33,44,55])
print(data[-1])
print(data[-5])

from numpy import array
data = array([
[11, 22],
[33, 44],
[55, 66]])
print(data[0,0])

#slicing
from numpy import array
data= array([
    [11,22],
    [33,44],
    [55,66]])
print(data[0,])

from numpy import array
data = array([11,22,33,44,55])
print(data[1:4])

from numpy import array
data = array([11,22,33,44,55])
print(data[-2:])

#''' split input and output data '''
from numpy import array
data = array([[11,22,33],
              [44,55,66],
              [77,88,99]])
x,y=data[:, :-1], data[:, -1]
print(x)
print(y)

#'''broadcast scalar to one dimenstional array'''
from numpy import array
a = array([1,2,3])
print(a)
b=2
print(b)
c= a+b
print(c)

#vector Addition
from numpy import array
a = array([1,2,3])
print(a)
b=array([1,2,3])
print(b)
c= a+b
print(c)

#vector subtraction
from numpy import array
a = array([1,2,3])
print(a)
b=array([0.5,0.5,0.5])
print(b)
c= a-b
print(c)

''' L1 NORMS VERSUS L2 NORMS'''

#vector L1 norm
from numpy import array
from numpy.linalg import norm
a= array([1,2,3])
print(a)
l1=norm(a,1)
print(l1)

#vector L2 norm
from numpy import array
from numpy.linalg import norm
a= array([1,2,3])
print(a)
l2=norm(a)
print(l2)

#triangular matrices
from numpy import array
from numpy import tril
from numpy import triu
m= array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
print(m)
#lower triangulr matrix
lower = tril(m)
print(lower)

#upper triangular matrix
upper = triu(m)
print(upper)

#digonal matrix
from numpy import array
from numpy import diag
#define square matrix
m= array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
print(m)
#extract diagonal vector
d=diag(m)
print(d)
#create Diagonal matrix from vector
D =diag(d)
print(D)

#identity matrix
from numpy import identity
i = identity(3)
print(i)

#Inverse Equivalence
from numpy import array
from numpy.linalg import inv
Q = array([
    [1,0],
    [0,-1]])
print(Q)
v=inv(Q)
print(v)

# orthogonal matrix
from numpy import array
from numpy.linalg import inv
# define orthogonal matrix
Q = array([
[1, 0],
[0, -1]])
print(Q)
# inverse equivalence
V = inv(Q)
print(Q.T)
print(V)
# identity equivalence
I = Q.dot(Q.T)
print(I)

# transpose matrix
from numpy import array
# define matrix
A = array([
[1, 2],
[3, 4],
[5, 6]])
print(A)
# calculate transpose
C = A.T
print(C)

# invert matrix
from numpy import array
from numpy.linalg import inv
# define matrix
A = array([
[1.0, 2.0],
[3.0, 4.0]])
print(A)
# invert matrix
B = inv(A)
print(B)
# multiply A and B
I = A.dot(B)
print(I)

# sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
# create dense matrix
A = array([
[1, 0, 0, 1, 0, 0],
[0, 0, 2, 0, 0, 1],
[0, 0, 0, 2, 0, 0]])
print(A)
# convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)
# reconstruct dense matrix
B = S.todense()
print(B)

from numpy import array
from numpy.linalg import inv
q=array([[1,2],
         [0,-1]])
print(q) 
v=inv(q)
print(q,v)
print(v) 


from numpy import array
from numpy.linalg import inv
q=array([[1,0],
         [0,1]])
print(q)
v=inv(q)
print(q,v)
print(v)

import numpy as np
np.__version__
# write a numpy program to get help with the add function
print(np.info(np.add))

x=np.array([1,2,3,4])
print("Original Array: ")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

x=np.array([0,1,2,3])
print("Original Array: ")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

x=np.array([1,0,0,0])
print("Original Array: ")
print(x)
print("Test if any of the elements of the said array is non-zero:")
print(np.any(x))

x=np.array([0,0,0,0])
print("Original Array: ")
print(x)
print("Test if any of the elements of the said array is non-zero:")
print(np.any(x))


import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original marix")
print(p)
print(q)
result=np.outer(p,q)
print("Outer product of the said two vectors:")
print(result)


#write a numpy program to compute the cross product of two given vectors
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original marix")
print(p)
print(q)
result1=np.cross(p,q)
result2=np.cross(q,p)
print("Cross product of the said two vectors(p,q):")
print(result1)
print("Cross product of the said two vectors(q,p):")
print(result2)


#write a numpy program to compute the determinant of a given square
import numpy as np
#from numpy import linalg as LA
a = np.array([[1,0],[1,2]])
print("Original 2-d array")
print(a)
print("Determinant of the said  2-D array:")
print(np.linalg.det(a))


#write a NumPy program to compute the eigen values and right eigen vectors
import numpy as np
m=np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n",m)
w,v=np.linalg.eig(m)
print("Eigenvector of the said matrix",w)
print("Eigenvalues of the said matrix",v)

#inverse of the matrix
import numpy as np
m=np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result=np.linalg.inv(m)
print("Inverse of said matrix:")
print(result)


#normal Distribution
import numpy as np
x=np.random.normal(size=15)
print(x)


#write a numpy program to genrate six random integers between 10 and 30
import numpy as np
x=np.random.randint(low=10,high=30,size=6)
print(x)


#write a numpy program to create a 3*3*3 array with random values
import numpy as np
x=np.random.random((3,3,3))
print(x)


#min and max values
import numpy as np
x=np.random.normal(5,5)
print("Original Array:")
print(x)
xmin, xmax = x.min(), x.max()
print("Minimum and maximum values:")
print(xmin, xmax)


#write a numpy program to get the maximum values 
import numpy as np
x=np.arange(4).reshape((2,2))
print("\n Original array:")
print(x)
print("\n maximum values along the second axis:")
print(np.amax(x, 1))
print("minimum values along the second axis:")
print(np.amin(x, 1))
