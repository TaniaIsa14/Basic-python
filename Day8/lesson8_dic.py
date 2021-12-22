'''
Dictionary
----------
variable{'key':vlalue}
'''
'''
Dictionary
----------
variable{}
'''
person1={'ID':1,'Name':'Tania Isa','Phone':'+088937569696'}
print(person1)
print(person1['ID'])
print(person1['Name'])
print(person1['Phone'])
person2=person1.copy()
print(person2)

#use a update method
person2.update({'Name':'Rupu'})
person2.update({'Age':19})
print(person2)

#delete by key
del person2['Age']
print(person2)

print(type(person2))
print(dir(person2))

person2.clear()
print(person2)

print(person1.items())
print(list(person1.items()))
print('Display only keys:')
print(person1.keys())

for k in person1.keys():
    print(k)
for v in person1.values():
    print(v)
for N in person1.keys():
    print(f'{N}={person1[N]}')
personkey= list(person1.keys())
print(personkey)

personkey.sort(reverse=True)
print(personkey)

for key in personkey:
    print(f'{key}={person1[key]}')

students={}
students['Id']=1
students['Name']='Topu'
students['Age']=12

print(students)
print(students.get('Name'))
print(students.get('Phone'))
print(students.get('phone','No phone found'))
#print(students['phone'])