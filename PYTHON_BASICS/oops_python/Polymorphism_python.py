#Polymorphism
'''
 Polymorphism means the ability to take various forms.In Python,
 Polymorphism allows us to define methods in the child class with the same
 name as defined in their parent class
'''
class dog:
      def sound(self):
            print('bow bow')

class cat:
      def sound(self):
            print("meow")
            
def makesound(animaltype):
      animaltype.sound()

catobj = cat()
dogobj = dog()

makesound(catobj)
makesound(dogobj)
