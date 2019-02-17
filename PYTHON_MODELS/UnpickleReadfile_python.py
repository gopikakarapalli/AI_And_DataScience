'''
pickleing Unpickle project:
--------------------------
project file name    :PickleProject_python
Data write file name :PickleWritefile_python
Data read file name  :UnpickleReadfile_python  
o/p file .dat        :pickleData_python.dat
'''
#Data read file name  :UnpickleReadfile_python :
#one of the person read the  all employees data on in this file with loading of pickleData_python.dat

import PickleProject_python as emp
import pickle
f=open("pickleData_python.dat","rb")
while True:
      try:
            obj=pickle.load(f)
            obj.display()
            print()
      except EOFError:
            print("all emp completed")
            break
f.close()
