'''
random module :
----------------
'''
from random import*

print('random() :')
#-----------------
for i in range(10):
       print(random())# it genrates in b/w 0 to 1 numbers randomly
       
print("randint() :")
#--------------------
for i in range(10):
       print(randint(1,46))# it genrates int numbers randomly

for i in range(10):
       print(randint(0000,4445))
print('uniform()')
#------------------
for i in range(10):
       print(uniform(1,10))# it generater float number in b/w given numbers

print("randrange(start,stop,step):") #(not opn ,opn end-1,opn)
#-------------------------------------
for i in range(10):
       print(randrange(1,10,2))#work like range but numbers is generate randomly

print("choice()")
#----------------
any_collection_object=["gopi","list",'g','f']

for i in range(10):
       print(choice(any_collection_object))# it return any index object randomly

#--------------------------------------------------
print("to get random aple bits")
for i in range(26):
       print(chr(randint(65,65+25)))

#------------------------------------------------
shuffle(any_collection_object, random=None)
for i in range(10):
       print(choice(any_collection_object))
       
import random
print(dir(random))

print(help(random))

