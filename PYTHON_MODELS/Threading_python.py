'''
multi threading:executing several tasks simultaneously is the concept of mult tasking
----------------
types of mult tasking:
----------------------
1)process based multi tasking:executing several tasks simultaneously where each
      task is a seperate independent process..EX: os
2)thread based multi tasking:executing several tasks simultaneously where each 
      task is a seperate independent part of same program .. and each independent
       part is called a thread.
-->the main object of mult threading is to reduce the executing time of program.
creating thread in py:
----------------------
      1)creating a thread without using any class
      2)creating a thread by extending thread class
      3)creating a thread without extending thread class
'''
#creating a thread without using any class :-
'''
from threading import*
def display():
      for i in range(5):
            print("this code executed by child thread :",
                  current_thread().getName())#it returns the current thread name

t=Thread(target=display)#mainthread creates child thread object
t.start()#main thread starts child thread
for j in range(5):
      print("this code executed by main thread:",current_thread().getName())

'''

#creating a thread by extending thread class
'''
from threading import*

class mythread(Thread):
      def run(self):
            for i in range(5):
                  print("this code executed by child thread :",
                        current_thread().getName())#it returns the current thread name

t=mythread()#mainthread creates child thread object
t.start()#main thread starts child thread
for i in range(5):
      print("this code executed by main thread:",current_thread().getName())
'''
#creating a thread without extending thread class
'''
from threading import*
class test:
      def display(self):
            for i in range(5):
                  print("this code executed by child thread :",
                        current_thread().getName())#it returns the current thread name
obj=test()
t=Thread(target=obj.display)#mainthread creates child thread object
t.start()#main thread starts child thread
t1=Thread(target=obj.display)
t1.start()
for j in range(5):
      print("this code executed by main thread:",current_thread().getName())

'''

#get and set name of a thread:
from threading import *
print(current_thread().getName())#or# getname --> to get current thread 
current_thread().setName("ThreadNameChange")#to change current thread name
print(current_thread().getName())


#with out threading time:
import time
def doubles(num):
      for n in num:
            time.sleep(1)
            print("double:",2*n)
def squares(num):
      for n in num:
            time.sleep(1)
            print("square:",n*n)

num=[1,2,3,4,5,6]
starttime=time.time()
doubles(num)
squares(num)
endtime=time.time()
print('with out threading time :',endtime-starttime)

#with threading time:
from threading import *
import time
def doubles(num):
      for n in num:
            time.sleep(1)
            print("double:",2*n)
def squares(num):
      for n in num:
            time.sleep(1)
            print("square:",n*n)

num=[1,2,3,4,5,6]
starttime=time.time()
t1=Thread(target=doubles,args=(num,))
t2=Thread(target=squares,args=(num,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print('with threading time :',endtime-starttime)



      
            






      
