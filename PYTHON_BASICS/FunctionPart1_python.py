'''
Function in py :
---------------
1)user defined function
2)built function
defineing of function: a group staments or set of instions 
----------------------
* function blocks begin with the key def followed by the function name and parentheses ()
* parenthesis consists of any input parameters or arg
* the code block within every function is indented and starts with a coloc : 
* return [expression] is used to exits a function.
calling of function:
--------------------
1) pass by value
2) pass by reference
'''
a=10 # global var(function out side declear var is global var)
b=13
def functionName():     #this is defineing of function
        b=11            #local var
        global a        #if we use/change global var value in inside function we must be use global key
        print('this is function')
        print("value of a inside methode is :",a)
        print("local var value of a inside methode is :",b)
        a=2
        print("value of a inside methode is :",a)
print("value of globlal a is :",a)
functionName()#calling function
print('valuel of global a changes but b ',a,b)

#=============================================================================
def add(num1,num2):              
        sum=num1+num2
        print(num1,' + ',num2,' = ',sum)

# pass by value

add(20,30)  #this is calling of function in pass by value methode

# pass by reference
def fun(c):
        print("valve of c",c)
        c[0]=100
        c[1]=90
        print('updated value',c)

fun([2,3,4]) #this is calling of function in pass by reference methode

#======================================================================================
print('types of parametes') # type of args given to arg
#--------------------

print('\n  positionl 1')
def calc(a,b):
        sum=a+b
        sub=a-b
        mul=a*b
        div=a/b
        rem=a%b
        return sum,sub,mul,div,rem
givenNum=calc(10,300) # (positionl)   --> high priat 1  #positionof var must be same
for x in givenNum:
        print(x)
        
print('\n  keyword arg 2')
givenNum=calc(b=300,a=10) # (keyword arg) --> 2
for x in givenNum:
        print(x)
        
print('\n  defalult arg')
def wish(a,b='default'):# (defalult arg )---> 3   #default arg must be taken in last arg
        sum1=a+1
        mul1=b*1
        return sum1,mul1
defarg=wish(1)
print(defarg)

print('\n var-arg')
def calc1(*var):   #internal *var is a tuple ----> 4
        for x in var:
                result=0
                result=result+x
                print('the sum' ,x,"after add",result)

calc1()
calc1(1,2)
calc1(1,2,3)
calc1(1,2,3,4)

print('\n', 'positionl - var-arg')
def calc1(name,*var):   #in case var-arg methode used in first arg then we must be used in var key word like below 
        for x in var:
                result=0
                result=result+x
                print('the sum' ,x,"after add",result)

calc1('g')
calc1('g',1,2)
calc1('g',1,2,3)
calc1('g',1,2,3,4)
        
print('\n   var-arg - positionl ')
def calc1(*var,name):   # we must be used in var key word 
        for x in var:
                result=0
                result=result+x
                print('the sum' ,x,"after add",result," ",name)

calc1(name='g')
calc1(1,2,name="g")
calc1(1,2,3,name="g")
calc1(1,2,3,4,name="g")

print('\n  key word var args')
#-------------------------
def display (**kwargs): #it key word var args
        print(type(kwargs))
        print('get key and values info')
        for k,v in kwargs.items():
                print(k,'=' ,v)

display(name='gopi',makes=100,age=45,sex='m')
display(name='satya',makes=100,age=50,sex='m')

print('recursive function:') # A function that calls itself recursive functions
#------------------------- ex :factorial(3)= 3*factorial(2)
#                                       3*2*factorial(1)

def factorial(n):
        if n== 0:
                result=1
        else:
                result=n*factorial(n-1)#calling of function repetedly is call recursive
        return result
print(factorial(0))
print(factorial(5))

print('Anonymous functions:')# name less function is called anonymous function
#----------------------------(instant use(only one time usage)
'''
in Normal function:
def squareit(n):
        retuen n*n
squareit(4)
print(squareit)
'''
# but in Anonymous functions:
# lambda input:expression
s=lambda n:n*n #lambda is a Anonymous functions
print('squ',s(4))
# lambda input:expression if conditions
s=lambda a,b:a if a>b else b
print('the biggestm of {} and {}is :{}'.format(10,20,s(10,20))) 

print('call a function as arg')
#------------------------------
print('filter methode')
# syntax: filte(function,sequence) the sequence may be any type like tuple list set etc..
#note: if function return True then consider sequence element if False not consider in sequence
def iseven(x):
        if x%2==0:
                return True  #this code gives True only in even num
        else:
                return False #this code gives False only in odd num
l=[1,2,4,5,3,5,6,8,9,55,77,88,55]
l1=list(filter(iseven,l))
print(l1)

print('lambda methode')
print('above program with filter $ lambda ')
l2=[1,2,4,5,3,5,6,8,9,55,77,88,55]
l3=list(filter(lambda x:x%2==0,l2))
print(l3)

print('map methode')
# syntax: map(function,sequence)
#apply some function in every element in the sequence and produce new vlaue wrt function

def double(x):
        return 2*x # this function double x value and x is seq of list l4
l4=[1,2,4,5,3,5,6,8,9,55,77,88,55]
l5=list(map(double,l4))
print('org list ',l4)
print('map list ',l5)

print('above program with map & lambda ')
l6=list(map(lambda x:2*x,l4))
print(l6)
print('map & lambda in multpul seq')
l7=[10,20,30,40]
l8=[20,30,40,50]
l9=list(map(lambda x,y:x*y,l7,l8))# in multpule seq both list same length other wise not consider exter element
print(l9)




