'''
Inheritance
-------------
class BaseClass:
    body of BaseClass
class DerivedClass(BaseClass):
    body of DerivedClass

'''

class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def walk(self):
        print(self.name.title()+ ' '+ 'is now walking.')

    def run(self):
        print(self.name.title()+ ' '+ 'is now running.')
    
    def show(self):
        s=self.name + ' '  + str(self.age)
        print(s)
        #return s.title( )

class Student(Person):        
    def __init__(self, name, age,fees) -> None:

        super().__init__(name, age)
        self.fees=fees

# creatinga a instance\object of student class

stud1=Student('Tania' ,24,2000)
stud1.run()
stud1.walk()
print(stud1.show())

    