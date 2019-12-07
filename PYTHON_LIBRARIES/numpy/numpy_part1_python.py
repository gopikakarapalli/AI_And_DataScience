# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:25:14 2018

@author: Gopi
read --> https://docs.scipy.org/doc/numpy/user/quickstart.html

-> numpy ( Numerical python)
-> numpy  is the core library for scientific computing in python
-> it provides a high performance multidimensional array object and tools for working with those arrays
-> to install numpy:--> conda install numpy   (or)
        type in cmd---> pip install numpy
                     
"""
import numpy as np  # we can use numpy must be import 

import sys
import time
import matplotlib.pyplot as matpy

print('to cerate a array' )
#
a= np.array([1,2,3])                  # one dimensional array
print('one dim --->\n',a)
b= np.array([(1,2,3),(34,5,6)])     # two dimensional array [][]
print('two dim --->\n',b)
c= np.array([(1,2,3,4),(34,5,6,7),(1.9,3,'go','pi')])     # mult dimensional array [][][]
print('mult dim --->\n',c)
#
print('convert list into array')
#
d=[[1,2,3],[1,2,5],[6,7,8]]
D=np.array(d) #to convert list into array
print(D)
#
print('comparsion of list and array ')
print('-----------------------------')
#
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
print('numpy array:')
print('-----------------')
#
print('to cerate a array' )
a= np.array([1,2,3])                  # one dimensional array
print('one dim --->\n',a)
b= np.array([(1,2,3,4),(34,5,6,5)])     # two dimensional array [][]
print('two dim --->\n',b)
c= np.array([(1,2,3,4),(3,5,6,7),(1,3,5,5)])   # mult dimensional array [][][]
print('mult dim  --->\n',c)
#
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
print('reshape -->array.reshape(row,col)')
print('two dim --->\n',b)
b=b.reshape(4,2)               #it is covererts one shape into anther shape with in the array size
print('reshape arrar \n',b)
#
print('slicing ---> array[row:1-end row,row:1-end row]')
print("array c :",c)
print('slicing 1 :',c[0,2])   # index calling
print('slicing 2 :',c[0:,3]) # array[row:1-end row,indxe]
print('slicing 3 :',c[1:,1]) 
print('slicing 4 :',c[:,2])
print('slicing 5 :',c[0:2,3])
print('slicing 5 :',c[0:2,3])
#
print('array math opration')
#
print('equal deffernce numbers b/e two numbers : np.linspace(start no,end no,no.of numbers b/e two numbers')
print(np.linspace(1,5,6)) #to get a equal deffernce numbers b/e two numbers
#
print(' max,min & sum of numder in the array elements:')
print(a)
print('max number in the array : ',a.max())
print('min number in the array : ',a.min())
print('sum of number in the array : ',a.sum())
#
print('axis based opration in array :')               
print(c)
print('sum of each colum elements in array:\n',c.sum(axis=0)) #if axis=0 then sum of each colum elements in array will be return
print('sum of each row elements in array  :\n',c.sum(axis=1)) #if axis=1 then sum of each row elements in array will be return
print('sqrt of each element in array :\n',np.sqrt(c))
print('standard deviation of array :\n',np.std(c))
#
print("arrays +,-,*,/")
#
a=np.array([(1,2,3,4,),(4,5,6,7),(8,9,0,1)])
b=np.array([(1,3,5,6,),(4,5,6,7),(1,2,3,4,)])
print('add-->\n',a+b)
print('sub-->\n',a-b)
print('mul-->\n',a*b)
print('div-->\n',a/b)
'''

'''
print('array a \n',a,'\n array b\n' ,b)
print('vertical stack of  array-->\n   ',np.vstack(a))# it  cerated  a vertical stack of array one are more array dependes on arg()
print('vertical stack of two array-->\n',np.vstack((a,b,)))  # (array 1,array 2)
print('array a \n',a,'\n array b\n',b)
print('horizontal stack of array-->\n'   ,np.hstack(a)) # it  cerated a horizontal stack of array one are more array dependes on arg()
print('horizontal stack of two array-->\n',np.hstack((a,b)))# (array 1,array 2)
print('flate')#  it  cerated vertical  into  horizontal  array and changes will not be feedback to the old array
print(' ravel of array-->\n',a.ravel())#  it  cerated vertical  into  horizontal  array and changes will be feedback to the old array
#
print(np.zeros(4)) #to print a no. zeros in n dim array
print(np.ones(5))  #to print a no. ones in n dim array
print(np.zeros((4,4))) #4 dim array
#
print('special functions')
#
print('to get a sin valve',np.sin(30))
print('to get a cos valve',np.cos(30))
print('to get a tan valve',np.tan(30))
print('to get a exponen valve',np.exp([1,3,4]))
print('to get a ln valve',np.log([1,3,4])) # nuturl log =>ln base 2
print('to get a ln valve',np.log10([1,3,4]))#log with base 10
#
print('to get a sin,cos & tan etc.., plots')
#sin plot
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)                  #just replace sin with tan ,cat etc .,
matpy.plot(x,y)              #to plot x y plot & must be import matplotlib.pyplot
matpy.show()                 #to show a plot popup
#cos plottial
x=np.arange(0,3*np.pi,0.1)
y=np.cos(x)
matpy.plot(x,y)
matpy.show()



'''

r=[1,1,2,3,4,5]
r1=np.array(r)
print(np.dtype(r1))
r1.astype(float)
print(r1)
'''




print(dir(np))















