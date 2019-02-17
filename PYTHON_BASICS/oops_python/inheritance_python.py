# oops

# inheritance
'''
Python allows us to derive a class from several classes at once,
this is known as Multiple Inheritance.'''

class animal:               # baseclass
      def eating(self):     # base class body
            print("eating")

class dog(animal):            #derive class(baseclass)
      def bark(self):          #derive class body
            print('bark')

dog_obj = dog()

dog_obj.eating()
dog_obj.bark()

print('===========================================================================')


class animal:               # baseclass
      def __init__(self,Name):     # base class body
            self.name = Name

class dog(animal):            #derive class(baseclass)
      def dispay(self):          #derive class body
            print(self.name)

dog_obj = dog('babyndog')

dog_obj.dispay()

print('==================Multiple and Multilevel Inheritance==============================')
print(' Multilevel Inheritance')

class A : # base class
      def display(self):
            print('it is super class')
            
class B(A):#derive class 1
      def show(self):
            print("it is base clas ")

class C(B): #derive class 2
      def printing(self):
            print('it is derived class')

print('C_obj :=>>>>>')
C_obj = C()
C_obj.printing()
C_obj.show()
C_obj.display()

print('B_obj :=>>>>>')
B_obj =B()

#B_obj.printing()
B_obj.show()
B_obj.display()

print('Multiple Inheritance')

class A : # base class 1(Father)
      def display(self):
            print('it is base class 1')
            
class B:#base class 2(mother)
      def show(self):
            print("it is base clas 2 ")

class C(A,B): #derive class 1
      def printing(self):
            print('it is derived class')

print('C_obj :=>>>>>')
C_obj = C()
C_obj.printing()
C_obj.show()
C_obj.display()

print('B_obj :=>>>>>')
B_obj =B()

#B_obj.printing()
B_obj.show()
#B_obj.display()




















