"""
    1)python is a general purpose high level programming language.
    2) guido van rossam @ 1989
    3)c,java --> statically typed programming
      python -->dynamically typed programming
    4)Python REPL tool   REPL ----> read evaluate print loop
    5) gating in py
       a)functional programming from c
       b)oop from c++
       c)scripting langauges features form perl and shell script
       d)modular programming features from modula-3
    6) area used in py
        a)desktop application
        b)web application
        c)database application
        d)N\W Application
        e) games
        F)data analysis
        g)machine learning
        h)AI
        i)IOT applications...
 py Tokens :identifiers
 -----------------------
 key words.
 identifiers :identifiers are the name used to identify a var,function,class and object.
 literals(int,float,etc...),
 operators.
 rules for identifiers
 ----------------------
    1)only upper and lower case alphabets and it is case sensitive
           digits(0 TO 9)
           UNDERSCORE (_)
    2)Identifer should not start with digit
    3)Identifer should not use key words.
    4) _Var ==> private
       __Var ==> strongly private
       __name__  ==>language spe identifers
       __add__   ==>language spe identifers
"""
import keyword             #to print total key words
print(keyword.kwlist)
#and.iskeyword          
#total key words 33

''' o/p these Identifer should not be use key words
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
# built-in function print in module builtins:
num=10
help(print)                 #to get any help for py                      
type(num)                   #to get data type
print(num)                  #to print any thinking
id(num)                     #to get the id of object

                #------------ DATA TYPES -------------#
         #  -----------------------------------------------#
i=10                  # int                   --> immutable(non-changable)---> immutable only at 0 to 256 ranges'
f=10.345              # float                 --> immutable
com=10+23J            # complex               --> immutable
b= True               #bool                   --> immutable
s='gopikakarapalli'   # str                   --> immutable
                      #range                  --> immutable
                      #bytes and bytearray    --> immutable & mutable
                      #list[] and tuple()     -->mutable & immutable
                      #set{} and frozenset    -->mutable & immutable
                       #dictionary ==>dict{K:V}-->mutable 
                       #None
print("'''''''''''''''''''''''''''''''''''''''''''''''''''")                      
print(type(num),type(i),id(num),id(i)) # adv of  immutable
print("'''''''''''''''''''''''''''''''''''''''''''''''''''") 
                   
print('# int data type ---->int immutable only at 0 to 256 ranges')
#--------------------

i,j=10,20
d=11           #Decimal form
B=0B111        #Binary form
b=0b111
O=0O111        #Octtal form
o=0o111
H=0X111        #hexa decimal
h=0x111
print('dec:'+ str(d),
      '\nbin:'+ str(B),'   ',str(b),
      '\noct:'+ str(O),'   ',str(o),
      '\nHex:'+ str(H),'   ',str(h))   # all o\p are in decimal form olny
print(type(b))   # <class 'int'>

print('---------------------base conversions--------------------')
bin(d)
oct(d)
hex(d)
print("bin:"+bin(d)+"\t oct:"+oct(d)+"\thex:"+hex(d))
print(d+d)
print(B+b)
print(B+O)    #any type we can add ,sub,mul,DIVED & and or nor etc..,
print(B*O)
print(H or o)

print("# float data type ----->immutable")
#-----------------------

f=10.01234
print(type(f))         #<class 'float'>
#fb=0b011      #systaxerror : invalid syntex (not workes in bin,oct,hex
ex=10.2e100
print('float:'+str(f) +'   exponential form:'+str(ex))

print("# complex data type  ----> immutable")
#----------------------------------------------

comi=10+10j             # a+bj
comf=1.03+0.34J         # a=real & b=imaginary    j^2=-1
com_if=10+0.445j
com_fi=1.3+10J    
print('com i:'+str(comi)+'com f:'+str(comf)+
      'com if:'+ str(com_if)+'com fi:'+str(com_fi))

print(type(comi))
print(complex(4,4.0))
print(com_if.real)
print(com_if.imag)
print(comi+comf)
print(comi-comf)
print(comi*comf)
print(comi/comf)
print(-comi+comf)
print(comi and comf)
print(comi.real+comf.imag)

print("bool data type    ---> immutable")
#-----------------------------------------

boo1=True            #only True , False
boo2=False            #internaly True= non zero (1,25); False= zero(0)
print(boo1)
print (type(boo1))
print('internaly True=',int(True),'-->non zero;    False=', int(False))
print(10>9)

print('# string data type  ---> immutable')
#--------------------------------------------

s1='gopi kakarapalli'                 #Single quotes --->str
s2="SIVA KAKARAPALLI"                 #double quotes ---->string
s3='Anusha\
Kakarapalli'
s4="""chakrapani kakarapalli      
  krishnarao kakarapalli"""           #triple quotes""" or '''---> multi lines
s5="siva 'anusha'kakarapalli"         #to print ' " ---> \' or \"
s6="siva \'anusha\'kakarapalli"
s7='g\v o\v p\v i \v\t kakarapalli'   # to get v & H(tab)---> \v ,\t
print(s1 +'\n',s2 +'\n',s3 +'\n',s4 +'\n',s5 +'\n',s6 +'\n'+s7)
print(s5==s6)

print(type(s1))

###strings add , mult

print('##strings add , mult')
print(s1+s2)
print(s1*3)

print('---------------------strings opration  with index----------------------')

print(s1)                                # s1=     [g o p i   k a k a r a p a l l i]
print('s1 fw index 0 element:'+s1[0])    #FW index:[0 1 2 3 4 5 6 7 8 9 10.........] start at 0
print('s1 RW index 0 element:'+s1[-4])   #rw index:[...... ...-10-9-8-7-6-5-4-3-2-1] start at -1    
s1_indx=s1[3]
print(s1_indx)
#print(s1[20])         #IndexError: string index out of range
print(type(s1_indx))
##slice operator
print('##slice operator')
print('1--'+s1[::])         #  s1[start index:end-1 index : no steps]
print('2--'+s1[5:14:2])     # default slice oprator[ 0:end index: 1]
print('3--'+s1[::-1])
print('4--'+s1[3:0:-1])
print('5--'+s1[-1:-10:-1])
print('6--'+s1[10:1:-1])


print('1--'+s1[:])
print('2--'+s1[:10])
print('3--'+s1[4:])
print('4--'+s1[:-1])
print('5--'+s1[-10:-1])

## string function__
print('-----------------## string function ##-----------------------')
print('--------------------------split-----------------------------')
print('with out spli str s1;  ',s1)
f1=s1.split()         #default split : spe " "
print('default split with " "--->',f1)
f2='go,pi,kakarapalli'          
print(f2)
f3=f2.split(',')                   # split with , ;  . / - etc..,---> enter(,)
print('split with (,)-----> ',f3)
print('--------------------join ------------------------------------')
print('join at end of each',' '.join(s1))# join str at end of the str
print('join--->','@'.join(s1))
print('str f1;-->',f1)                    #Note : in join end -1 is not joined
print('spli &join--->',' $  '.join(f1))
print('str f3;-->',f3)
print('spli &join---> ','27'.join(f3))
se1='elephant is an animal'
ss=se1.split("an")
print('split---',ss)
print('join---->','an'.join(ss))
print('-----------------------replace-------------------------------')
print('replace---> : ',s1.replace('g','G'))   #(org str,replace str)
print('-----------------------sorted-------------------------------')
print('sorted like abcd..---> :',sorted(s1)) #to sorted the string 
print('--------------------case conversion--------------------------')
print('string s1--> ',s1)
print('string s2--> ',s2)
print('string s2--> ',s3)

print('to convert loewr case to upper case -->  ',s1.upper())
print('to convert upper case to lower case --> ',s2.lower())
print('each word state with uper case --> ',s1.title())
print('only stating leter is uppercase-->', s1.capitalize())
print('to convert upper to lower & lower to upper-->',s3.swapcase())
print('ALL UPPER THEN GIVES LOWER OR \
all lower then gives lower other wise it gives lower --> ',s3.casefold())

print('--------------------checking string -----------------------------')
s1='gopikakarapalli'
s2='GOPI'
num="1283410567"
s3=' gopi kakarapalli  '
s4="--gopi apparao--"

print('2---> : ',s1.count('ka'))     #to returns the no patens count matched .coun('patens')
print('3---> : ',s1.startswith('gopi'))#returns given satarting patens are T/F
print('4---> : ',s1.endswith('lli'))    #returns given ending patens are T/F
print('5---> : ',s1.find('k'))          #returns the index value of given paten
print('5 a-> : ',s1.rfind('k'))         #returns the index value of given paten in right side
print('6---> : ',s1.index('a'))         #returns the index value of given paten
print('6 a-> : ',s1.rindex('a'))        #returns the index value of given paten in right side
print('7---> : ',len(s1))               #returns the length of string

print('8---> : ',s1.isalpha())          #returns all are alpha are not T/F
print('9---> : ',num.isalnum())         # returns all are num are not T/F
print('10---> : ',s1.isalnum())
print('11---> : ',num.isdecimal())      # returns all are decimal are not T/F
print('12---> : ',s1.isdigit())         # returns all are digitare not T/F
print('13---> : ',s1.islower())         # returns all lower case are not T/F
print('14---> : ',s2.isupper())         # returns all uper case are not T/F
print('15---> : ',s1.isspace())         # returns all space are present not T/F
print('16 a---> : ',s3.lstrip())        #it removes are trim the left hand side of string space or(' or /..etc)
print('16 b---> : ',s3.rstrip())        #it removes are trim the right hand side of string space or(' or /..etc)
print('16 c---> : ',s3.strip())         #it removes are trim the both side of string space or(' or /..etc)
print('16 x---> : ',s4.strip("-"))      # strip any place with ('it is any symble but default is space')

print('to get unicode of this valve',chr(97))

print('to get ordenal of the unicode',ord('a'))
#--------------- type casting or type coersion  -------------
print('------------type casting or type coersion ------------')
'''int()
float()
complex()
bool()
str()'''
# int__
print(int(10.567),'__a__',int(True),'__b__',int('10'),'_c_',int(0b011))
#print(int("10.5"))    #ValueError: invalid literal for int() with base 10: '10.5'
#print(int(10+2.3j))   #TypeError: can't convert complex to int
#print(int('ten'))     #ValueError:could not convert string to int: 'ten''

#float___

print(float(10),'__a__',float(True),'__b__',float('10'),'_c_',
      float("10.5"),'_d_',float(0b011))
#print(float(10+2.3j))   #TypeError: can't convert complex to float
#print(float('ten'))     #ValueError: could not convert string to float: 'ten'
#print(float('ob11'))    #ValueError: could not convert string to float: 'ob11'

#complex____
print(complex(4),'_a_',complex(4.89),'_b__',complex(4,4.0),'_c_',
complex(True),'_d_',complex('10'),'_e_',complex('10.5'),'_f_',complex(0b111))
#print(complex('ten'))    #ValueError: complex() arg is a malformed string
#print(complex('0b111'))  #ValueError: complex() arg is a malformed string
#print(complex('10','23'))#TypeError: complex() can't take second arg if first is a string

# bool___
print(bool(0),'__1__',bool(10),  '_2___',bool(10.3),'__3_',bool(10+2j), '_4_',
bool(0b111),  '__5_',bool(10+2j),'__6_',bool(0+0j), '__7__',bool('10'),'__8__',
bool("10.5"), '__9_',bool(''),   '__10_',bool('strin'))
#string__(str)
print(str(10),'__a__',str(10.333),'__b__',str(True),'_c_',
str(10+15j),'_d_',str(0b011))

print('#######################################################################')


# range()   ---> immutable : 
#--------------------------
print('# range()  ---> inmutable--------------------------------------------')

'''range data type represent a sequencence of valves '''
# form 1:- 
r=range(10)   #range(end-1)
print(type(r))
print(r)
for i in r:print(i)

# form 2:- 
r=range(5,10,2)   #range(end,end-1,step) default valves (int 0 ,int x, int 1
print(type(r))
print(r)
for i in r:print(i)

print(r[2])
print(r[2:5])
print(r[::-1])
#r[0]=23      # TypeError: 'range' object does not support item assignment
#r=range(10.5) #TypeError: 'float' object cannot be interpreted as an integer


###bytes-->(immutable) anb bytesarry-->(mutable) -----------------------------------   
print('###bytes-->(immutable) anb bytesarry-->(mutable): ')

print('##bytes-->(immutable)')   
l=[99,59,5,47,46]              #bytes type data use only in 0 to 256 only
by=bytes(l)
print(type(by))
print(by[0])
print(by[-1])
print(by[:10:2])   # o\p--> b'c\x05.' so to print byte data in loop
for x in by:
       print('bytes data index',x)
       
l1=[100,256,257]                #erroe because of 256 is out of rang in bytes
#for x in l1:print(bytes(l1))   #o/p  -->ValueError: bytes must be in range(0, 256)

print('##bytearray-->(mutable)')

l=[99,59,5,47,56]              #bytearray type data use only in 0 to 256 only
by=bytearray(l)
print(type(by))
print(by[0])
print(by[-1])

print(by[:10:2])   # o\p--> bytearray(b'c\x05.')' so to print byte data in loop
for x in by:
      print('bytearray data index',x)
by[4]=46      
for x in by:
      print('bytearray data index',x)
       
#l1= [100,256,257]                  #erroe because of 256 is out of rang in bytes
#for x in l1:print(bytearray(l1))   #o/p  -->ValueError: bytes must be in range(0, 256)

#  list and tuple  :      -->mutable & immutable
#-----------------------------------------------
print('# list and tuple     -->mutable & immutable-----------------------------------')

print('##list')
#---------------
'''mutable,insertion order is preserved & Duplicates are allowed'''
l=list()            # ro #
l1=[]
l1=[1, 2,2.3,4,'a','b',True]
l2=[2,3,2,4,5,0]
print(type(l))
print('before append-->',l)

l.append(00)
l.append(99)
l.append('59')                  #add element at end of the list
l.append('go')
l.append(True)

print('after append lisst l   ',l)
l.insert(2,'K')                 #Insert element at index place in list--->(inset inx , add element)
print('after inset lisst l   ',l)
l2=l.copy()                        #copy the list ie .,l2=l
print('copy ===>',l2)
l.extend(l1)                       #to add two list ie.l=l+l1
print('extend-->',l)
l[0]=91                            #to replace the element
print('replace-->',l)
l.reverse()                        #returns reverse of given list
print('reverse-->',l)
print('count-->',l.count('go'))      #return the no times repeted in given elements
print('inx-->',l.index('59'))        #returns index of given element in the list     
print('len-->',len(l))               #returns the length of list
print('pop-->',l.pop())     #returns and remove the last element of list
#print('pop-->',l.pop(2)
l1.remove(4)                # remove the given element in the list
print('remove-->',l1)
l.clear()                   #clear the list
print('clr of l-->',l) 

print('-----------slice & index--------')
print(l1[1])
print(l1[:-1])
print(l1[5::-1])

print('l1*2---->',l1*2)
print('l2+l1---->',l2+l1)
print(l1==l2)
      
print('-----------sort of list-----------')
l3=[1,2,3,5,1,2,9,6,3]
print('list  ',l3)
print('sorted -->',sorted(l3))   # to sort the list(reverse=T\F)
print('sorted in reverse-->',sorted(l3,reverse=True) ) # (if reverse= True then DESNDING ORDER)

print('------------nested list----------')

nestted=[[10,2,3,4,5],12,30,45]
print('nestted list  : \n',nestted)
print(nestted[0])
print(nestted[0][2])
print(nestted[0][1])
print(nestted[2])

m=[[12,34,2,],[12,34,00,22],[23,67,88]]
print('elements in matrix formate :')
for row in range(len(m)):
       for col in range(len(m[row])):
              print(m[row][col],end=' ')
       print()
print('----------list comprehension -----')
# list=[expression for x in sequence] it is  comprehension  
# list=[expression for x in sequence if condtion]--> if we required any condition
l=[]
for x in range(1,11):
      l.append(x*x)
print(l)
# Ex 1
print('it is same as above but it is list comprehension form')
L=[x*x for x in range(1,11)]
print(L)
# Ex 2
L1=[x for x in L if x%2==0]
print(L1)

print('#tuple        --> immutable')
#-----------------------------------
t=()
print(type(t))
t=(1,2,2,'d',4,'gopi',True)
t1=(1,2,3,6,3,2,4)
print('length of t  ',len(t))
print(t.index(2))
print(t.count(2))
print('min',min(t1))
print('max',max(t1))
print('slic-->',t[1:3])
print('slic with step-->',t[3:1:-1])
t2=t[1:4]
print('slic-->',t2)
print('*-->',t2*3)
T=(10,30,43)
T1=(10,23,11)
print('- >  -',T>T1)
#t1[0]=10      #TypeError: 'tuple' object does not support item assignment

print("----sorting------")# tuple is no sort funcation
print(t1)
l=sorted(t1) # tuple is immutable so if we sort tuple first convert in list form and sort
print('tuple ',t1)
print('list  ',l)

print('----tuple packing & unpacking------')
a=12
b=2
c=3
t=a,b,c
print('tuple packing-->',t)
t=(12,12,3,4)
a,b,c,d=t
print('tuple unpacking  a= ',a,' b= ' ,b,' c= ',c,' d= ',d)
l=[1,2,3,4]
q,w,e,r=l
print('tuple unpacking  list a= ',q,' b= ' ,w,' c= ',e,' d= ',r)# any type can be unpack string,like set,list,fs,t,d

print('----------tuple comprehension -----')#this methode is not thre in tuple but it works due to some internal genrators
# tuple=(expression for x in sequence) it is  comprehension  
# tuple=(expression for x in sequence if condtion)--> if we required any condition
t=(x*x for x in range(1,11))
for x in t:
       print(x)
print('type of t   ',type(t))# o/p is not tuple 

print('# set{} and frozenset    -->mutable & immutable--------------------')
#---------------------------------------------------------------------------
print('### set{}    --->mutable')
#--------------------------------
'''
    1)insertion order not preversed
    2)duplicates not allowed
    3)index opration & slicing oprator are not working
'''
s=set({})                   # to cerat set with valevs like set({1,2,e,4,5})
print(type(s))
s=set()                       # to cerat set without any valevs
s.add('a')
s.add('d')
s.add(1)
s.add(5)
print('insertion order not preversed-->',s)

s1={2,2,2,3,'gopi',3,True}     # it is set={any elements} it show set data type
print('set s1==> ',s1)
s1.add('kakarapalli gopi')   #add/remove elements after cereat set with elements only
s1.remove('gopi')
print('after add & remove',s1)
l=[1,2,3,4]
s1.update(l,range(0,4,1),'g')#to add group of elements to the set (arg is any type & any no.of arg like set,list,element)
print('after update :',s1) # IN case elements updata must be  more then one element
#s1.update(5)#(only one object is not updated because it squ updata)TypeError: 'int' object is not iterable
print('pop :',s1.pop())# remove and return some random elemment
print('set  ',s1)
s1.remove('g')#to remove the element
print('remove  ',s1)
s1.clear()
print('clear  ',s1)

s=set([1,2,3,4])#convert list into set
s1=set('asdfgghj')#convert string into set
print('convert list & string into set \n',s,'\n',s1)
#s[0]=3    #TypeError: 'set' object does not support item assignment
#s[1:2:3]   #TypeError: 'set' object is not subscriptable

print ('--------mathematical operations in set---------------')

s1={10,20,30,40}
s2={30,40,50,60}
print('union  :',s1.union(s2)) # OR
print('s1|s2  :',s1|s2)
print('intersection  :',s1.intersection(s2)) # AND
print('s1|s2  :',s1&s2)
print('difference :',s1.difference(s2)) #s1-s2 the ele present in s1 but not in s2
print('symmetric difference :',s1.symmetric_difference(s2)) #the ele present in s1 or s2 but not in both  
print('symmetric difference (s1^s2):',(s1^s2))
s1=set('gopi')
print('memder shipe ' ,'g' in s1)

print('--------------set comprehension ---------------------')

# set={expression for x in sequence} it is  comprehension  
# set={expression for x in sequence if condtion}--> if we required any condition
s={x*x for x in range(1,11)}
print(s)

print('### frozenset    --->immutable')
#----------------------------------------
'''
    1)insertion order not preversed
    2)duplicates not allowed
    3)index opration & slicing oprator are not working
'''
fs=frozenset(s)
print(type(fs))
print('frozenset fs---> ',fs)
#fs.add(0)    #AttributeError: 'frozenset' object has no attribute 'add'
#fs.remove(1)  #AttributeError: 'frozenset' object has no attribute 'remove'
#print(fs[0])   #TypeError: 'frozenset' object does not support


#dictionary      ==> dict{K:V}           --> mutable
#----------------------------------------------------
print('# dictionary ==>dict{Key:Value}      --> mutable')

'''1)insertion order preversed
    2)duplicates not allowed in key but in value can alows any type of obj
    like (int str lis set....,)
    3)index opration & slicing oprator are not working
'''
d={}
print(type(d))
d={0:27,1:'g',2:'o',3:'p',4:'i',5:'--'}
D={'a':'g','b':'o','c':'p','d':'i'}
print(d)
d[5]=9959054746 #to add a element d[key]=vave
d[0]='K'        #to replace a element=> d[replace key]=vave
del d[5]   # to delete the element wrt key del var[key]
#del d[10] # in case key is not in the dic we will get KeyError: 10, so beforce delete we moust be check key is present are not
print('after add, replace,delete ope  :\n',d)
d.clear()  # to clear all element in dic
print('after clear ope-->',d)
#del d #to deleted dic d so it go's to Gc (NameError: name 'd' is not defined)
#print(d)
d[1]=[(11,34),{1,2,3},5]
print('dic d',d)
print(D['a'])# to print each valve wrt key

d=dict([(100,'gopi'),(200,'chakrapani')]) # list or set or tuple of tuples of internal par must be tuple
print('with lish of tuples  :',d)
d=dict(((100,'gopi'),(200,'chakrapani'))) 
print('with tuples of tuples  :',d)
d=dict({(100,'gopi'),(200,'chakrapani'),(1,'e'),(2,'2')}) 
print('with SET of tuples  :',d)
#d=dict({[100,'gopi'],[200,'chakrapani']}) #TypeError: unhashable type: 'list'
#print('with lish of tuples  :',d)
print('len  ',len(d)) # to get length of dict
print('writ wrt key valve ',d.get(100))# to get the valve wrt key
print('key valve not in dict ',d.get(500))# if key is not present then returns you default valve None/you default valve 
print('key valve not in dict & default ',d.get(500,'enter you default valve'))
print('pop ele in dict',d.pop(100))#remove &return wrt key
print('after pop dict ele ',d)
print('popitem ele in dict',d.popitem())#remove some element
print('after popitem dict ele ',d)
print('all keys',d.keys())#it returns all keys
print('all values',d.values())#it returns all values
print('all items',d.items())#it returns all items in form [(k,V),(k,v)]
for k,v in d.items():# to get each key & value 
       print('each key & value ',k,'.....',v)
d1=d.copy()# to copy one dict into anther dict
print('copy   ',d1)
print('set def',d.setdefault(100,'gopi'))#if key is not present then add value & return, if key is present we con't perform any opration &return key value
print('set def',d.setdefault(200,'xxxxx'))#key is present so not peform any opration(key,value)
print('dict d after set def',d)
d1={4:'r',6:'e'}
print('dict  d+',d,'\n d1=',d1)
d.update(d1)# to add one dict into anther dict but arg dict type or key value sque & onlyone args
print('after updata d',d)

print('--------------dict comprehension ---------------------')

# dict={key : expression for x in sequence} it is  comprehension  
# dict={key : expression for x in sequence if condtion}--> if we required any condition
d={x:x*x for x in range(1,11)}
print(d)

# None data type :
#----------------
print('####None data type ')


 #o/p==> None   if no value
 # if not doing any thinking ==>pass key word
'''
def f1():
        a=10
def f2():print('hi')
print(f1)
print(f2)
'''
print('###############################################################################')

# Escape chracters:

'''1)\n   ->  now line
   2)\t   -->  tab
   3)\r   --->  carr is return ie.,go to fistto cures
   4)\v   ---->  vet space
   5)\b   ------>  back space
   6)\f   -------->  form feed ie.,page down
   7)\'  or   \" ------>neglating ' or "
   8)\\
'''   




