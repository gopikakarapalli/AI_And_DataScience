'''
flow control:
...............
1)conditional statements/selection statements:
----------------------------------------------
if
if-else
if-elif-else

2)iterative statments:
-----------------------
for loop
while
3)transfer statements:
----------------------
break
continue
pass
'''
print('1)conditional statements/selection statements:')#........................
print('-----------------------------------------------------------------------')
print()
print('if')
con=1
if con==1:                                        
        print('i am under if statement area')
print('i am not in if statement area')
print('...................................')
####........................................
print('if-else')
if con==1:
        print('i am under if statement area')
else:                                             
        print('i am under else statement area')
print('i am not in if-else statement area')
print('....................................')
#####.......................................
print('if-elif-else')

if con==1:                              #if can be use any no.of times
        print('i am under if statement area')
elif con==2:                            # elif is alwaya optional & use any no.of times
        print('i am under elif statement area')
else:                                    # else is alwaya optional
        print('i am under else statement area')
print('i am not in if-elif-else statement area')

# NOTE : else is alwaya used anyevey in python like
#       for-else
#       while-else
#       try - except-else-finally, etc...
print('.......................................')
####............................................
print('Nested if')
if con==1:                                        
        print('i am under if statement area')
        if con==1:                                        
                print('i am under Nested if statement area')
        elif con==2:                                             
                print('i am under Nested elif statement area')
        else:                                             
                print('i am under Nested else statement area')
elif con==2:
        print('i am under elif statement area')
else:                                             
        print('i am under else statement area')
print('i am not in if elif else  (or) Nested if elie else statement area')
print('...............................................................')

print()

print('2)iterative statments:')#----------------------------------------------
print('------------------------------------------------------------------------')
print()
#####................................................
print('for loop :')    # we know no.fo iterative go for for loop
count=0
index=0
s="gopi kakakarapalli"
for x in s:
        count+=1
        print('for loop count: ',count,'  index:',index, 'element: ',x)
        index+=1
print('i am under for loop area')
#..............................................

for x in range (10):
        if x%2==0:                            
                print('even number: ',x)  
        if x%2!=0:
                print('odd number : ',x)
        else:
                print('it is not even or odd')
#####...........................................

print('nested for loop')
for i in range(2):
        for j in range(3):
                print('i= {} and j={} '.format( i,j ))

print('print a table n x n\ ')
'''
n=int(input('enter the no.of rows:'))
for i in range(1,n+1):
        print('#'* i )
'''
#.....................................
'''
n=int(input('enter the no.of rows:'))
for i in range(1,n+1):
        for j in range(1,i+1):
              print('*',end=" ")
        print()
'''
#....................................
print('print a table n x n ')
'''
n=int(input('enter the no.of rows:'))
for i in range(n):
        print('#'* n )
'''
#....................................
'''
n=int(input('enter the no.of rows:'))
for i in range(n):             # no .of rows
        for j in range(n):     # no.col
              print('*',end=" ")
        print()
'''

print('........................................')
#####...........................................
print('while')     # we don't  no.fo iterative go for while loop

x=0
while x<6:
        print(x)
        x+=1
print('i am under while loop area')
'''
n=int(input('enter number'))
sum=0
i=1
while i<=n:
      sum=sum+i
      i+=1
print('total; ',sum)
'''
'''
while True :
        print('I am infinite loop ')
'''

print('.............................................')


print('3)transfer statements:')#------------------------------------------------
print('------------------------------------------------------------------------')
print('break')

loops=0
while 1 :
        print('am infinite loop stop with break')
        loops+=1
        if loops==10:
                break

print('...........................................')
####..............................................
print('continue')  #it is used to sikep some line of code

for i in range(10):              #-----1
        if i%2==0:
                continue         #----this loop go to 1 
        print('it is odd numder : ',i)
#.......................................................
numbers = [10,0,12,34,5,6,78,98,0,45,44,0.0]
for n in numbers:
        if n==0:
                print('100/0 error {}:inf'.format(n))
                continue
        print('100/{}={}'.format(n,100/n))
####.....................................................
print('for-else')
car=[10,2,3,23,45,10]
for item in car:
        if item>100:
                print('we  cannot process this item..',item,'insurence must be requency')
        print('processing item',item)
        break
else:    #else is related to for loop and it is exitutedd only when without break exituted
        print('congrats..all items processed successfully')
              
print('............................................')
####................................................
print('pass')   # it is akeyword in py

if 1:
        pass
else:
        print('it is passed through else')
#.............................................

def f1():
        print('hi')
def f2():
        pass
#..............................................
f1()
f2()

class p:
        def m1():pass
class c(p):
        def m1():
                print('it is chiled class')
                
print('------------------------------------------------------------------')
####........................................................................
print('del statement:')  # # it is akeyword in py & used to delete the var
x=10
print(x)
del x     # to deleted the var x
# print(x)  # o/p is NameError: name 'x' is not defined
a=10
b=20
del a,b
#print(a,b) #NameError: name 'a' is not defined
#print(id(a)) #NameError: name 'a' is not defined
a=10
print(a)
a=None
print(a)
# iterating multiple lists at the some time
print('---------------------------   zip    -------------------------')

l1=[list(range(0,10))]
l2=[list(range(10,20))]
print(l1)

for x,y in zip(l1,l2):
    print(l1)
    print(l2)











