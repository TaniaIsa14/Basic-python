'''
Function
--------
def function_name(perameters):
    """doc_string"""
    statements

'''
def welcome():
    """This is a document string"""
    print('Helow Tania, Good night')

welcome()
print(welcome.__doc__)

def welcome1(name):
    """This is a another document string"""
    print(f'Hello {name} , Good night')

welcome1('Tania')
welcome1('Isa')

print(welcome1.__doc__)

def welcome2(name,msg):
    print(f'Hello\t{name} {msg}')
welcome2('Tania','good even')
welcome2('Tania','good morning')

def welcome3(name1,name2,name3,name4):
    print(f'hello {name1}')
    print(f'hello {name2}')
    print(f'hello {name3}')
    print(f'hello {name4}')
welcome3('Tania','Sajib','Gulshan','Banani')


#Python Arbitrary Arguments

def welcome4(*name):
    for x in name:
        print(f'hello {x}')
# calling function    
welcome4('Tania','Sajib','Gulshan','Banani','Shuvo','nazmul')

def welcome5():
    return 'I am from welcome5'
print(welcome5())

#anonymous fuction or also called lambda function 
#syntax of lambda functions
#function name=lambda arguments:expression

'''
def double(x):
    return  x*2
result=double(10)
print(result)
print(double(30))

'''
digun=lambda x:x*2
print(digun(3))
# function with return value
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print(add(10,90))
print(sub(20,9))
print(mul(4,8))
print(div(20,5))

#using arbitrary keyword argument
def build_profile(first,last,**kwargs):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in kwargs.items():
        profile[key]=value
        return profile
print(build_profile('Tania','Isa',loction='Dhaka',field='IT'))

import math
print(math.pi)