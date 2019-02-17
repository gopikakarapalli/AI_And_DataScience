'''
try
except
finally

control-flow in try-except-finally
nested try except finally
'''
try:
       print('outer try block')
       try:
              print("inner try block")
              print(10/0)
       except ZeroDivisionError:
              print("inner except block")
       finally:
              print("inner finally block")
except:
       print("outer except block")
finally:
       print("outer finally block")
print('-------------------------------------------------------------------')

#else :
#-----

try:
       print("risky cody")
       print(10/0)
except:
       print('willl be executed if exception in try')

else:
       print("willl be executed if no exception in try")
finally:
       print('''will be executed always exception raised or not raised and
       handled or not handled''')

print('---------------------------------------------------------------------')
'''
Exception :
-----------
types of exceptions:
1) predefinednexception/in built exceptions
             automatically raised by python
              ex : print(10/0) ZeroDivisionError
2)user Defined exceptions/customized Exceptions
'''
#user Defined exceptions/customized Exceptions:
#------------------------------------------------

class TooyoungException(Exception):
      def __init__(self,arg):
            self.msg=arg
class toooldException(Exception):
      def __init__(self,arg): 
            self.msg=arg

age=int(input("enter youre age"))
if age>60:
      raise TooyoungException( "your age already crossed")
elif age<18:
      raise toooldException("plZ wait some more time")
else:
      print("Thanks for registration...")


