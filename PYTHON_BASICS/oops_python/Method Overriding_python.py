#Method Overriding
class A:
      def show(self):
            print("it is a class A")

class B(A):
      #pass
      def show(self):
            print("it is a class B")

print('a_obj =>>>')
b_obj = B()
b_obj.show()

print('a_obj =>>>')
a_obj = A()
a_obj.show()
