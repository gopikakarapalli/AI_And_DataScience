'''
operators 
----------
1)Arithmetic Operators
2)Comparison (Relational) Operators
3)Assignment Operators
4)Logical Operators
4)Bitwise Operators
5)Membership Operators
6)Identity Operators

'''''''''''''''''''''''''
1)Arithmetic Operators
'''''''''''''''''''''''''
+ --> addition
- --> Subtraction
* --> Multiplication 
/ --> Division          # it alwayes returns the float data typr result only
% --> Modulo (remainder)

// --> Floor division   # # it alwayes returns the chiled data type only
** --> Exponent or power (n^2)
'''
print('1)Arithmetic Operators')
print("a"*20)
#print("gopi"+10) #-->TypeError: can only concatenate str (not "int") to str
print(1+2)
#print(10/0)#-->ZeroDivisionError: division by zero 
#print(10%0)#-->ZeroDivisionError: integer division or modulo by zero
#print(10//0)#-->ZeroDivisionError: integer division or modulo by zero

'''''''''''''''''''''''''''''''''''
2)Comparison (Relational) Operators
Relational
>,<, >=,<=
Equality operators
==  --> contain comparison
!= --> NOT equal
Chaining of relation oprators 
'''''''''''''''''''''''''''''''''''
print('2)Comparison (Relational) Operators')

print('Relational')
a='gopi'             # uni code of A==>65 & a==65 
b='gopi'
print('a>b is', a>b) #comperison is based on alfbit (like A to Z & a to z)
print('1<4 is', 1<4) #comperison is based on number order
print('T>F is', True>False)
print('##equality operators')
print(10==20)
print('gopi'=='gopi')
print(10==10.0)
print(10!=20)
print('a'==20) #non comperbul type alwayes gives False
print('chaining of relation oprators')
print(10<5<30<50)    #this is called chaining of relation oprators
print(10==5+5==2*5)


'''''''''''''''''''''''''''
3)Assignment Operators(=):

'''''''''''''''''''''''''''
print('3)Assignment Operators(=)')

a=10
b='gopi'
c=True
d=2+34j
print(a,b,c,d)
a,b,c,d=10,'gopi',True,2+34j #this called compound assignment
print(a,b,c,d)
a+=10 #(also use +=,-+,*+,/+,%=,//=,**=,&=,|=,^=,>>=,<<=)
print(a)
#a++ and a-- inc and dec not there in python

#Ternary operator
#----------------
#x=firstvalue if condition else secondvalve   ---> it is python stx
x=30 if 10<20 else 40
print('ternary--->',x)
y=10 if 20>10 else 40 if 50<60 else 70 #nessting of if
print('neesting of if-->',y)
#x=(condition)?firstvalue:secondvalve----> in java
#x=(10>20)?30:40
print('givening input to the system')

'''''''''''''''''''''
4)Logical Operators:
and,or,not
boolean type:
-------------
and --> if both arg are True then only True
or ---> if atlest one  arg are True then only True
not ---> Give True get Fales
Non-boolean type:
-----------------
0  means False
non-zero means true
empty string true
X and Y
-------
if x evaluates to false then result is x  otherwise returns y
X or Y
-------
if x evaluates to true then result is x  otherwise returns y
'''''''''''''''''''''
print('4)Logical Operators:')
print(True and False)
print("and--->",10 and 20)
print("and--->",0 and 20)
print("and--->",1 and 'gopi')
print("or --->",10 or 20)
print("or --->",0 or 20)
print('not--->',not 0)
print('not--->',not 1)

'''''''''''''''''''''
4)Bitwise Operators:
& --> and
| -->  or
~ --> not (complmant)
^ --> x-OR if both bits arg  
<< --> lift shift oprator
>> --> right shift oprator

Notr : applicable only for int and boolran
'''''''''''''''''''''
print('&-->',1&2)
print('&-->',True&True)
print('|-->',True|True)
print('^-->',True^True)
print('|-->',True|True)
print('~-->',~4)
print('<<-->',10<<2)
print('>>-->',10>>2)
#print('|-->',10.3&10.5)#TypeError: unsupported operand type(s) for &: 'float' and 'float'
#print('|-->',''|'True')#TypeError: unsupported operand type(s) for |: 'str' and 'str'


print('special operators:')
''''''''''''''''''''''
special operators:
5)Membership Operators
6)Identity Operators:
------------------
5)Membership Operators
in--> it is use to check it is member are not
not in--->

'''''''''''''''''''''''    
g='gopi kakarapalli'
print('gopi in-->','gopi'in g)
print('g in g-->','g'in g)
print('x in g-->','x'in g)
print('not in -->','kj'not in g)
a=[1,2,3,4,5,7,6]
print('2 in a list-->',1 in a)
'''''''''''''''''''''''
6)Identity Operators:
is  --> it is use to address comparsion
is not

'''''''''''''''''''''''

a=10
b=10
c=30

print('a is b  ',a is b)   # a & b pointing to same obj then it returns Trun 
print('a is not b  ',a is not b)   # a & b not pointing to same obj then it returns Trun
print('a is b  ',a is c)    
print(id(a))
print(id(b))
print(id(c))
print(a==b) #it is used to contant comparsion




###operator precedence

'''
unary operators            -->high precedance
binary
ternary operators
Assignment Operators       -->low precedance



() ==> paranther           -->high precedance
** ==> power 
~(bit),- unary operators  
*,/,%.//-->binary operator
+,-
<<,<<                               |
&                                   |
^
|
>,>=,<,<=,==.!=
=,+=,-=,*=.....                     |
is,isnot
in,not in                           |
not
and
or                           -->low precedance


'''


















