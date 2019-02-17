'''
classes and objects
classes in python
inheritance
adstract class
-> class is the blueprint from which specific objects are created.
   elements  in class:
      1) class variable:a var that is shared by all instances of class
      2)instance var: instance var unique to each instance
      3)method: the function that we define inside a class
      
'''

class student:         #class_is_key_word className
        pass
std_1 = student()     # instvarName = className
std_2 = student()

std_1.first = 'gopi'   # instvarName.objectName
std_1.last = 'k'
std_1.email = 'gopi@gmail.com'
std_1.marks = 55

std_2.first = 'satya'   # instvarName.objectName
std_2.last = 'k'
std_2.email = 'satya@gmail.com'
std_2.marks = 99

print(std_1.email)
print(std_2.email)
print(std_1.first)
print(std_2.first)

print("-----------------------------------------------------------")
'''
instace var: value of var is varied from object to object
-----------
self.name is instance var#in general inside constructor we have to declare with self key
but inside methode declare instance var with self key,outside class also cerate
how to access :with in the class by using self ie.self.var
but outside of class by useing reference var only
static var :the valve changes from object to object and it is a class leve var
-----------
declare :at class ,at constructor,instance methode & statis methodes, outside of classwith class name,at classmethode by using cls var OR CLASSNAME
how to access :with class name or reference object var
if change in one object valve change will be effect all object in static var
if we can change static var valve with class name only
local var:with in the loop or instance use only not access  in out side
----------
'''
class student:
      collName='praghti eng'# static var at class declare
      def __init__(self,Name,Rollno,Marks):# constructor  name must be __init__(self,......)
            self.name=Name# self.name is instance var at constructor declare
            self.rollno=Rollno 
            self.marks=Marks
            student.city='kkd'#static at constructor declare

      def display(self):# instance methodes'''(self) will call all current object var'''
            print('student name:',self.name)
            print('student name:',self.rollno)#instance var access with in the class by using self
            print('student name:',self.marks)
            self.d=400#inside methode declare instance var with self
            student.state="ap"#instance methode with class name DECLARE OF STATIC VAR

      @classmethod#it reffers classmethod
      def classmethName(cls):#(cls) it can take any name
                cls.dist='EG'#static var declare at class methode

      @staticmethod#it reffers static methode
      def staticmethName():#() with any var passing it is a static methode
                student.pin=533005 #static var declare at static methode
s1=student('gopi',101,90)#constructor calling & s1 is ref of constructor
s2=student('kavya',102,95)
s3=student('don',102,90)
s1.display()#methode calling
s2.display()
s3.display()
print(s1.name)#instance var access outside of class by useing reference var only

ss=student("inst",12,12)
ss1=student("in",12,12)#calling instance methode
student.classmethName()#calling class methode
student.staticmethName()#calling static methode
student.outsideStaticVar=1000#declaring static var outside of class
print(ss.collName,ss.name)#access static var with reffernce
print(student.collName,ss.name)#access static var with class name

student.collName='kites cl '#if change in one object valve change will be effect all object in static var
ss.name='sri'
print("ss: ",ss.collName,ss.name)
print("ss1:",ss1.collName,ss1.name)



print('print in the  dict formate with object ref')
#-----------------------------------------------
s1=student('gopi',101,90)
print(s1.__dict__)#objectreferrence.__dict__#all var object
print(student.__dict__)# get all static var we call with class name


























            
















            
            
