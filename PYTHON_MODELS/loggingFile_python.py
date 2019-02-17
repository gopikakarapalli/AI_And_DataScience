'''
Logging : to note the all the actives in a file
---------
adv :1)dy using log files we can dedugging
     2)like no.of requrests

logging levels:
---------------
1. CRITICAL --50    -->HIGH LEVELS
2. ERROR --  40
3. WARNING --30
4. INFO  --20
5. DEBUG --10
6.NOTSET --0

dedugging: the process of fixing dug is call dedugging
----------
defect/bug:mismatch b/w expected result and original result
----------
'''
import logging
import time
dt=time.ctime()
print(dt)
logging.basicConfig(filename="logging_python.txt",level=logging.ERROR)
#it proveds required levels of logging configction(filename=name,level=req leve)

print("write logging by python")

logging.debug("debug message %s"%time.ctime())
logging.info("info message:%s"%time.ctime())
logging.warning("warning message %s"%time.ctime())
logging.error("error message %s"%time.ctime())
logging.critical("critical message %s"%time.ctime())
#-------------------------------------------------------------


print('----------logging exception-----------------')

logging.basicConfig(filename="logging_python.txt",level=logging.INFO)

logging.info("A new logging exception request came %s"%time.ctime())
try:
      x=int(input("enter first number"))
      y=int(input("enter second number"))
      print(x/y)
except ZeroDivisionError as msg:
      print("can't divide with zero")
      logging.exception(msg)
except ValueError as msg:
      print("enter only int values")
      logging.exception(msg)

logging.info(" request completed  %s"%time.ctime())






