#!/usr/bin/env python
# coding: utf-8

# # numpy ( Numerical python)
# read --> https://docs.scipy.org/doc/numpy/user/quickstart.html
-> numpy  is the core library for scientific computing in python
-> it provides a high performance multidimensional array object and tools for working with those arrays
-> to install numpy:--> conda install numpy   (or)
        type in cmd---> pip install numpy
# In[4]:


import numpy as np  # we can use numpy must be import 


# In[5]:


import sys
import time
import matplotlib.pyplot as matpy


# In[6]:


print('to cerate a array' )

a= np.array([1,2,3])                  # one dimensional array
print('one dim --->\n',a)
b= np.array([(1,2,3),(34,5,6)])     # two dimensional array [][]
print('two dim --->\n',b)
c= np.array([(1,2,3,4),(34,5,6,7),(1.9,3,'go','pi')])     # mult dimensional array [][][]
print('mult dim --->\n',c)


# In[7]:


print('convert list into array')
#
d=[[1,2,3],[1,2,5],[6,7,8]]
D=np.array(d) #to convert list into array
print(D)


# ### comparsion of list and array

# In[8]:


print('arrays are used less memorys')
#
r=range(10000)
print('memory of list used :',sys.getsizeof(5)*len(r)) # import sys

r=np.arange(10000)
print('memory of list used :',r.size*r.itemsize)
#
print('arrays are fast ie.,it take less time')
#
SIZE = 1000000
l1=range(SIZE)
l2=range(SIZE)
start = time.time()
result = [(x,y) for x,y in zip (l1,l2)]
print('time taken by list :',(time.time()-start)*1000,'msec') #import time

a1=np.arange(SIZE)
a2=np.arange(SIZE)
start = time.time()
result = a1+a2
print('time taken by array :',(time.time()-start)*1000,'msec')
#


# ### numpy arras

# In[9]:


print('to cerate a array' )
a= np.array([1,2,3])                  # one dimensional array
print('one dim --->\n',a)
b= np.array([(1,2,3,4),(34,5,6,5)])     # two dimensional array [][]
print('two dim --->\n',b)
c= np.array([(1,2,3,4),(3,5,6,7),(1,3,5,5)])   # mult dimensional array [][][]
print('mult dim  --->\n',c)


# ### finding array porperties

# In[12]:


print('finding array porperties:')
print('---------------------------')
print('array dimension-->a ',a.ndim)     # it returns the dimension of array
print('array b-->',b.ndim,'array c-->',c.ndim)
print('size of each element in array ',a.itemsize)  #it returns the each element size in the array
print('data type of elementin arrey ',a.dtype)#it return type of elements in the arrey
print('size of array',a.size)         # it returns size of array
print('shape of array',a.shape)     # it returns shape of array
print('shape of array',c.shape)     #o/p (no.of row, no.of colu)
#


# ### RESHAPE 
# Returns an array containing the same data with a new shape.

# In[17]:


print('reshape -->array.reshape(row,col)')
print('two dim --->\n',b)
#b=b.reshape(4,2)                it is covererts one shape into anther shape with in the array size
#print('reshape arrar \n',b)
B=np.reshape(b,(4,2))
print(B)


# ### meshgrid

# In[24]:


xx= np.array(range(0,10))
yy= np.array(range(0,6))
x,y = np.meshgrid(xx,yy)
print(x)
print(y)


# ### array math opration

# In[44]:


print(' max,min & sum of numder in the array elements:')
print(a)
print('max number in the array : ',a.max())

print('sum of number in the array : ',a.sum())
print('returns max number index  in the array : ',a.argmax())
print('returns min number index in the array : ',a.argmin())
#
print('axis based opration in array :')               
print(c)
print('sum of each colum elements in array:\n',c.sum(axis=0)) #if axis=0 then sum of each colum elements in array will be return
print('sum of each row elements in array  :\n',c.sum(axis=1)) #if axis=1 then sum of each row elements in array will be return
print('sqrt of each element in array :\n',np.sqrt(c))
print('standard deviation of array :\n',np.std(c))


# In[ ]:


print("arrays +,-,*,/")

a=np.array([(1,2,3,4,),(4,5,6,7),(8,9,0,1)])
b=np.array([(1,3,5,6,),(4,5,6,7),(1,2,3,4,)])
print('add-->\n',a+b)
print('sub-->\n',a-b)
print('mul-->\n',a*b)
print('div-->\n',a/b)


# In[ ]:


print('array a \n',a,'\n array b\n' ,b)
print('vertical stack of  array-->\n   ',np.vstack(a))# it  cerated  a vertical stack of array one are more array dependes on arg()
print('vertical stack of two array-->\n',np.vstack((a,b,)))  # (array 1,array 2)
print('array a \n',a,'\n array b\n',b)
print('horizontal stack of array-->\n'   ,np.hstack(a)) # it  cerated a horizontal stack of array one are more array dependes on arg()
print('horizontal stack of two array-->\n',np.hstack((a,b)))# (array 1,array 2)
print('flate')#  it  cerated vertical  into  horizontal  array and changes will not be feedback to the old array
print(' ravel of array-->\n',a.ravel())#  it  cerated vertical  into  horizontal  array and changes will be feedback to the old array


# ### equal deffernce numbers b/e two number

# In[46]:


print('equal deffernce numbers b/e two numbers : np.linspace(start no,end no,no.of numbers b/e two numbers')
print(np.linspace(1,5,6)) #to get a equal deffernce numbers b/e two numbers
print(np.logspace(1,5,6))


# #### zeros or ones

# In[ ]:


print(np.zeros(4)) #to print a no. zeros in n dim array
print(np.ones(5))  #to print a no. ones in n dim array
print(np.zeros((4,4))) #4 dim array


# #### eye
# Creates an identity matrix

# In[48]:


I=np.identity(3,dtype=int)# creat squ mx
print(I)
ey=np.eye(4,3)#any dim
print(ey)


# In[51]:


ey=np.eye(4,3,k=2)#k=+ve for col k=-ve for row
print(ey)
print('------------------')
ey=np.eye(4,3,k=-2)#k=+ve for col k=-ve for row
print(ey)


# In[40]:


ey[0]=np.nan
ey[1]=np.inf#over flow
print(ey)
print(ey[0],ey[1])
np.isnan(ey)


# In[41]:


print(np.where(np.isnan(ey)))
print(np.where(np.isinf(ey)))


# In[43]:


ey[np.where(np.isnan(ey))]=0.5
ey[np.where(np.isinf(ey))]=0.6
print(np.where(ey > 0.6))


# In[ ]:


print('special functions')
#
print('to get a sin valve',np.sin(30))
print('to get a cos valve',np.cos(30))
print('to get a tan valve',np.tan(30))
print('to get a exponen valve',np.exp([1,3,4]))
print('to get a ln valve',np.log([1,3,4])) # nuturl log =>ln base 2
print('to get a ln valve',np.log10([1,3,4]))#log with base 10


# In[ ]:


print('to get a sin,cos & tan etc.., plots')
#sin plot
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)                  #just replace sin with tan ,cat etc .,
matpy.plot(x,y)              #to plot x y plot & must be import matplotlib.pyplot
matpy.show()                 #to show a plot popup


# In[ ]:


#cos plottial
x=np.arange(0,3*np.pi,0.1)
y=np.cos(x)
matpy.plot(x,y)
matpy.show()


# In[ ]:





# In[ ]:


r=[1,1,2,3,4,5]
r1=np.array(r)
print(np.dtype(r1))
r1.astype(float)
print(r1)


# ## NumPy Indexing and Selection
#  select elements or groups of elements from an array.

# In[29]:


print('slicing ---> array[row:1-end row,col:1-end col]')
print("array c :",c)
print('slicing 1 :',c[0,2])   # index calling
print('slicing 2 :',c[0:,3]) # array[row:1-end row,indxe]
print('slicing 3 :',c[1:,1]) 
print('slicing 4 :',c[:,2])
print('slicing 5 :',c[0:2,3])


# ### Broadcasting
# Numpy arrays differ from a normal Python list because of their ability to broadcast:

# In[13]:


#Setting a value with index range (Broadcasting)
arr = np.arange(0,11)
arr[0:5]=100
print(arr)


# In[15]:


#Important notes on Slices
slice_of_arr = arr[0:6]

print(slice_of_arr)


# In[18]:


#Change Slice
slice_of_arr[:]=99
#Show Slice again
print('slice_of_arr',slice_of_arr)
print('arr',arr)#Now note the changes also occur in our original array!


# ### Indexing a 2D array (matrices)

# In[20]:


arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

print(arr_2d)


# In[21]:


#Indexing row
arr_2d[1]


# In[24]:


# Format is arr_2d[row][col] or arr_2d[row,col]

# Getting individual element value
print(arr_2d[1][0])

print(arr_2d[1,0])


# In[27]:


# 2D array slicing
print(arr_2d)
#Shape (2,2) from top right corner

print(arr_2d[:2,1:])(r,c)


# In[32]:


#Shape bottom row
print(arr_2d[2])
print(arr_2d[2,:])


# ###  Selection
# selection based off of comparison operators.

# In[35]:


arr = np.arange(1,11)
arr


# In[38]:


print(arr>4)


# In[39]:


arr[arr>4]


# ## Random
# Numpy also has lots of ways to create random number arrays:

# In[40]:


'''
https://docs.scipy.org/doc/numpy/reference/routines.random.html
'''
# numpy random sampling :
import numpy as np

#rand(d0, d1, …, dn)Random values in a given shape.(r,col)
print('rand\n',np.random.rand(3,2))

#randn(d0, d1, …, dn)Return a sample (or samples) from the “standard normal” distribution.
print('randn \n',np.random.randn(3,4))#(row,col)
      
#randint(low[, high, size, dtype])Return random integers from low (inclusive) to high (exclusive)
print('randint',np.random.randint(2,5,size=10))
print('randint', np.random.randint(2, size=10))
print('randint',np.random.randint(5, size=(2, 4)))#Generate a 2 x 4 array of ints between 0 and 4, inclusive:

#random_integers(low[, high, size]) Random integers of type np.int between low and high, inclusive.
print('random_integers',np.random.random_integers(10))
print('random_integers',np.random.random_integers(5,size=(3,2)))

#random_sample([size])Return random floats in the half-open interval [0.0, 1.0).
#random([size])Return random floats in the half-open interval [0.0, 1.0)
#ranf([size])Return random floats in the half-open interval [0.0, 1.0)
#sample([size])	Return random floats in the half-open interval [0.0, 1.0)
print('sample\n',np.random.random_sample((5,)))
print('sample \n',np.random.random_sample((5,6)))

#choice(a[, size, replace, p])Generates a random sample from a given 1-D array
print('choice',np.random.choice(5, 3)) #This is equivalent to np.random.randint(0,5,3)
print(np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0]))#Generate a non-uniform random sample from np.arange(5) of size 3:
print(np.random.choice(5, 3, replace=False))#Generate a uniform random sample from np.arange(5) of size 3 without replacement:
#                                         #This is equivalent to np.random.permutation(np.arange(5))[:3]
print(np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0]))#Generate a non-uniform random sample from np.arange(5) of size 3 without replacement:

aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
print(np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3]))

#bytes(length)	Return random bytes.
print('bytes',np.random.bytes(5))


# In[42]:


print(dir(np))


# In[ ]:




