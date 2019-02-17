'''
pickleing Unpickle project:
--------------------------
project file name    :PickleProject_python
Data write file name :PickleWritefile_python
Data read file name  :UnpickleReadfile_python
o/p file .txt        :pickleData_python.dat
'''

#Data write file name :PickleWritefile_python
#one of the person write the  all employees data on in this file and save in pickleData_python.txt

import PickleProject_python #this code file
import pickle

f=open("pickleData_python.dat","wb")
no_of_emp=int(input("enter number of employees"))
for i in range(no_of_emp):
      eno=int(input("enter employrrs number  :"))
      ename=input("enter employrrs name  :")
      esal=float(input("enter employrrs salary  :"))
      eaddr=input("enter employrrs address  :")
      e=PickleProject_python.employee(eno,ename,esal,eaddr)
      pickle.dump(e,f)


