'''
shallow copy vs Deep copy:
--------------------------
shallow: if the original object contains any references (nest list etc)to mutable objects,
-------
just duplicate reference variables will be created pointing to old
contained objects,but not duplicate object creation
Deep copy: contained objects compltely duplicate object creation if nest list contained or not
----------
-->if orignal object does not contain any nested objects then we should
go for shalllow cioning
-->if orignal object  contain any nested objects then we should
go for deep coning

'''
import copy

#shallow copy:
print("shallow copy")
l1 =[10,20,[30,40],50]#[30,40] is nested list
l2=copy.copy(l1) #shallow copy also l1=l2 or copy()
l1[0]=11
l1[2][0]=888 #we are changes in nest list data  original object contains is also changes
print(l1)
print(l2)
print("id of l1[2][0]",id(l1[2][0]))#old id
print("id of l2[2][0]",id(l2[2][0]))#new id = old id ref after copying
print('but')
print("id of l1",id(l1))# but both object or differnt object
print("id of l2",id(l2))

#deep copy
print('deep copy')
l1 =[10,20,[30,40],50]#[30,40] is nested list
l2=copy.deepcopy(l1) #deep copy 
l1[2][0]=888 #we are changes in nest list data  original object contains not change
l1[0]=11
print(l1)
print(l2)
print("id of l1[2][0]",id(l1[2][0]))#old id
print("id of l2[2][0]",id(l2[2][0]))#new id =! old id is not ref after copying
print('but')
print("id of l1",id(l1))# but both object or differnt object
print("id of l2",id(l2))




#shallow copy:
print("shallow copy case no nested list")
l1 =[10,20,30,40,50]#in case no nested list
l2=copy.copy(l1) #shallow copy also l1=l2 or copy()
l1[0]=11
l1[2]=888 #we are changes in  list data  original object contains not changes
print(l1)
print(l2)
print("id of l1[2]",id(l1[2]))#old id
print("id of l2[2]",id(l2[2]))#new id = old id ref after copying
print('but')
print("id of l1",id(l1))# but both object or differnt object
print("id of l2",id(l2))

#

