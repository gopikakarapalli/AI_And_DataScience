import time

t=time.time() #returns time stam
print(t)

print(time.localtime(time.time()))
print(time.ctime())
print(time.asctime())


mytuple=(2018,4,4,12,23,15,0,0,0)
tf=time.mktime(mytuple)
print(tf)

print(time.localtime(time.mktime(mytuple)))
s=time.ctime()
time.sleep(10)
e=time.ctime()
print(s-e)

