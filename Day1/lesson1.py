'''
author :Tania

Lesson1:Variable
date:21 sept 21
'''
print('I love my country')
name='Tania isa'
age=12
salary=20000.00
print(name)
print(age)
print(salary)

#display variable datatype
print(type(name))
print(type(age))
print(type(salary))
print(name,age,salary)
#way 0
print('Name:'+name+'\tAge:'+str(age)+'\tSalary:'+str(salary))
print('Name:'+name+'\nAge:'+str(age)+'\nSalary:'+str(salary))
#1
print('Name:{0}\n Age:{1} \n Salary:{2}\n'.format(name,age,salary))
#2
print('Name:{}\n Age:{} \n Salary:{}\n'.format(name,age,salary))
#3
print(f'Name:{name}\n Age:{age} \n Salary:{salary}\n')
#4
print('Name:%s\n Age:%s \n Salary:%s \n'%(name,age,salary))

