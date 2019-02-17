'''
pickleing Unpickle project:
--------------------------
project file name    :PickleProject_python
Data write file name :PickleWritefile_python
Data read file name  :UnpickleReadfile_python  
o/p file .txt        :pickleData_python

'''
# project file name    :PickleProject_python
#this is the code for employee data to write many to many ie .it act as employee data module
import pickle
class employee:
      def __init__(self,eno,ename,esal,eaddr):
            self.eno=eno
            self.ename=ename
            self.esal=esal
            self.eaddr=eaddr
      def display(self):
            print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
