'''
libraries : a group of module
-----------
modules: A  group of functions and variables saved to a file
--------
adv modules : code reusability
              length of the code will de reduced and readability
              maintainability
import module1
import module1,madule2,....
from modulel import functionname

import module1 as m1 --> give shortcut name
from modulel import functionname as mf
'''
print("reload the module")  
#--------------------------
import time
from imp import reload #imp lid are use to reload the module 
import module2A_python # saved py file
print("program entering into sleeping satae")
time.sleep(20)
reload(module2A_python)#reload the module 
print("this is last line of program")
 
print("finding memders of a module")
#---------------------------------
x=10
y=10
def f1():
       print('hello')
print('Current module memders :\n',dir())#it returnslist of Current module memders
print('time module :\n',dir(time))#it returns list of (required modul) memders

#special variable __name__ :
#----------------------------
'''
__name__ == __main__ ==> the code executed directly by this program
__name__ == __any ther name__ ==> the code executed indirectl by some other program

'''












