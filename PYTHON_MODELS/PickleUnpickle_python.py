'''
pickling:the process writeing a state of object
--------
unpickling:the process reading a state of object
----------
import pickle
pickle.dump(object,file)
pickle.load(file)
'''
import pickle
class employee:
      def __init__(self,eno,ename,esal,eaddr):
            self.eno=eno
            self.ename=ename
            self.esal=esal
            self.eaddr=eaddr
      def display(self):
            print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
#pickleing:
with open("PickleUnpickle_python.dat",'wb') as f:
      e=employee(100,'gopi',10000,"kkd")
      pickle.dump(e,f)
      print("pickling of emp obj completed....")
      
#unpickleing:

with open("PickleUnpickle_python.dat",'rb') as f:
      obj=pickle.load(f)
      print("emplyee info after unpickleing...")
      obj.display()# to print the object data


      
#ALSO USE JOBLIB INSAME FUNCTIONS
