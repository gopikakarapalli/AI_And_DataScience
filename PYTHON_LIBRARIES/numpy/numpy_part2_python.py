'''
https://docs.scipy.org/doc/numpy/reference/routines.random.html
'''
# numpy random sampling :
import numpy as np

#rand(d0, d1, …, dn)Random values in a given shape.(r,col)
print('rand\n',np.random.rand(3,2))

#randn(d0, d1, …, dn)	Return a sample (or samples) from the “standard normal” distribution.
print('randn \n',np.random.randn(3,4))#(roe,col)
      
#randint(low[, high, size, dtype])Return random integers from low (inclusive) to high (exclusive)
print('randint',np.random.randint(2,5,size=10))
print('randint', np.random.randint(2, size=10))
print('randint',np.random.randint(5, size=(2, 4)))#Generate a 2 x 4 array of ints between 0 and 4, inclusive:

#random_integers(low[, high, size]) Random integers of type np.int between low and high, inclusive.
print('random_integers',np.random.random_integers(10))
print('random_integers',np.random.random_integers(5,size=(3,2)))

#random_sample([size])	Return random floats in the half-open interval [0.0, 1.0).
#random([size])	Return random floats in the half-open interval [0.0, 1.0)
#ranf([size])	Return random floats in the half-open interval [0.0, 1.0)
#sample([size])	Return random floats in the half-open interval [0.0, 1.0)
print('sample\n',np.random.random_sample((5,)))
print('sample \n',np.random.random_sample((5,6)))

#choice(a[, size, replace, p])	Generates a random sample from a given 1-D array
print('choice',np.random.choice(5, 3)) #This is equivalent to np.random.randint(0,5,3)
print(np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0]))#Generate a non-uniform random sample from np.arange(5) of size 3:
print(np.random.choice(5, 3, replace=False))#Generate a uniform random sample from np.arange(5) of size 3 without replacement:
#                                         #This is equivalent to np.random.permutation(np.arange(5))[:3]
print(np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0]))#Generate a non-uniform random sample from np.arange(5) of size 3 without replacement:

aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
print(np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3]))

#bytes(length)	Return random bytes.
print('bytes',np.random.bytes(5))
