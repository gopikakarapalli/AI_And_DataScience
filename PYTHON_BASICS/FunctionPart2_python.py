print('Nested functions:')
#=========================
def fun():
        def nestedfun():
                pass
#f1=outer() // function call
#f1=outer // for outer function we are giveing another name
#-----------------------------------------------------------------------------
def outer():
        def inner(a,b):
                print("the sum:  ",a+b)
                print("the avg: ",(a+b)/2)
                print()
        inner(10,20)
        inner(10,27)
        inner(10,28)
        inner(10,200)

outer()

print("A function can return's another function" )
#================================================
def outer1():
        print("outer function started")
        def inner1():
                print("inner function execution")
        print("outer function returning inner function")
        return inner1
f1=outer1()  #outer function call's inner function
f1()  #directcly call inner function
print()

print('function Decorators')
#==========================
'''
==>i/p function ===> decorator function ===> o/p function with extended functionlity
==>decorators help to make our code shorter(more pythonic)
==>decorators ae use to extend functionaly ie to add exter functions
==> @ link the function and decorators function
'''
def decorVar(func):
        def inner3(name):
                if name=='xyz':
                        print('==> hello xyz bad morning')
                else:
                        func(name)
        return inner3

@decorVar #==> decorVarfunction=decorVar(wish)

def wish(name):
        print('hi',name ,'good morning')
wish('chakrapani')
wish('gopi')
wish('siva')
wish('anu')
wish('xyz')

print('decorators required some times not req in  same times')

def decorVar(func):
        def inner3(name):
                if name=='xyz':
                        print('==> hello xyz bad morning')
                else:
                        func(name)
        return inner3
      
def wish(name):
        print('hi',name ,'good morning')
        
decorVarfunction=decorVar(wish) 

wish('chakrapani')
wish('gopi')
decorVarfunction('gopi')
wish('xyz')
decorVarfunction('xyz')

print('---------------------------------------------------------------')
def smartdivision(funs):
        def inner(a,b):
                if b==0:
                        print("zero is not div")
                        return
                else:
                        return funs(a,b)
        return inner
@smartdivision
def division(a,b):
        return a/b
print(division(10,2))
print(division(10,0))






























                
      
