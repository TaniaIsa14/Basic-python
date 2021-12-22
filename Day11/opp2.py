class Person(object):

    def __init__(self,n='GULSHAN',a=16) -> None:
        self.name=n
        self.age=a

    def __str__(self) -> str:
        return self.name
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def setName(self,x):
        self.name=x
    def setAge(self,y):
        self.age=y

p1=Person()
#p1.setName('Rupu')
#p1.setAge(14)
print(p1.getName())
print(p1.getAge())
