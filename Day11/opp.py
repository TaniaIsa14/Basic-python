'''
# A class is a blueprint for the object 
# An object has two characteristics
# A.Attributes
# B.Behavior
class ClassName(object):
    --snip--
Making and instance/object from a class
objectName=ClassName(arguments)
'''

class Calculator(object):
    def addition(self,x,y):
       return x+y
    def subtraction(self,x,y):
       return x-y
    def multipiction(self,x,y):
      return x*y
    def division(self,x,y):
      return x/y
c1=Calculator()
print(c1.addition(2,6))
print(c1.subtraction(45,20))
print(c1.multipiction(30,4))
print(c1.division(45,5))