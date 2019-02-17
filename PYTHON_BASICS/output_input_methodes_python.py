print('###############################################################################')
  
######## print_methodes:

a=9959054746
b= 'gopikakarapalli'
print()
# method 1                         no sapce b/w two sring
print("hello"+b)
print("hello"+str(a))
print("---------------------------------")

# method 2                          sapce b/wtwo sring and output defaulr speration is space
print("hello",b)
print("hello",a)
print("---------------------------------")

# method 3                       output speration is space  baaed on sep="req symble"

print("hello",b,sep='_')
print("hello",a,sep="    ")
print("---------------------------------")

# method 4                   to print multplu print lines in single line and
                             #output speration is space  baaed on end="req symble"

print("hello",end=" ")
print("gopi\
       kakarapalli  \n,\t whatapp")   # next line also print in same line due to \,
                                      #\n--> new line,\t---> tab
print("---------------------------------")


# method 5
f=1.22
print("hello %s "%b)            #%s--> string,%d,%i-->ind,--->float
print("hello %d"%a)              
print("hello a=%d,b=%s"%(a,b))
print("---------------------------------")

# method 6
print("hello a= {}    b={}".format(a,b))     #order is impartant
print("hello b={1}    a={0},".format(a,b))   #order is based on {index}
print("hello a={A}    b={B}".format(A=a,B=b))#order is based on {wrt format(var=x)}
print("---------------------------------")


print("####################################################################")
#### input methodes:
print('input methodes')
'''
i=input("if u r requered lable : ")   #the o/p is only str type
print(type(i))
i=int(input("if gives int type o/p data only : ")) #type cast is req for other type
print('int-- ' ,type(i))
i=float(input("if gives float type o/p data only : "))
print('f---' ,type(i))
i=bool(input("if gives bool type o/p data only : "))      
print('b--',type(i))

#read multipule values from the keyboard in single line
a,b,c=[int(x)for x in input("enter 3 number:").split()]
print(a,b,c)

a,b,c=[int(x)for x in input("enter date formate DD/MM/YYYY:").split("/")]
print(a,b,c)
a,b,c=[float(x)for x in input("enter 3 number formate a,b,c:").split(',')]
print(a,b,c)

###evall():it is used of automatic type casting type casting depends on input data type only
#---------#data tyep we are giveing ing get o/p int ,are give list give list

x=eval('10+20+30')
print('eval--->',type(x))

ee=input('enter any expression')
result=eval(ee)
print(result)


ei=eval(input('enter any data'))
print('eval--->',type(ei))
for x in ei:
        print(x)


a,b,c=[eval(x)for x in input("enter 3 number:").split()]
print(a,b,c)
print('eval--->',type(a),type(b),type(c))
'''

#commanad line arguments:
#----------------------------
'''
py test.py
argv -----command arg python it is list type and it is present in "sys modual"
args ---- in java it is array
'''
from sys import argv
print('argv sis   ',type(argv))  #enter in commanad promt fileName.py 10 20 30 ..
print(argv)                      #o/p [test.py,10,20,30]
print(argv[2])                   #o/p [20]



















                                        


