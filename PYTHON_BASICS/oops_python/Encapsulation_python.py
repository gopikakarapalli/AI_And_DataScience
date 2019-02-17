#  Encapsulation

class car:
      __maxspeed = 0 #pravit var
      def __init__(self): 
            self.__maxspeed = 200
            self.__updatesoftware()
      def   drive(self):
            print("driving")
            print('maxspeed after set :',self.__maxspeed)
      def __updatesoftware(self):# pravit function
            print("updating software")

      def setspeed(self,speed):
            self.__maxspeed = speed
            print('maxspeed after set :',self.__maxspeed)


car_obj = car()

car_obj.drive()
car_obj.setspeed(100)
car_obj.__maxspeed = 10 #note : speed is not change
car_obj.drive()
#car_obj.updatasoftware() #we can't call out side the class __pravit methode are var
