'''
list
-------
listvar=[]
'''

motocycles=['Honda','Yamaha','Suzuki','TVS']
print(motocycles)
#print(motocycles[0])
#print(motocycles[1])
#print(motocycles[2])
#print(motocycles[3])
#for moto in motocycles:
#print (moto)

'''
i=0
while i<=3:
    print(motocycles[i])
    i+=1
    
    change

motocycles[1]='Hero'
print(motocycles)

motocycles.append('Bazaz')
print(motocycles)
motocycles.insert(2,'Runner')
print(motocycles)
'''
fruits=[]
fruits.append('Mango')
fruits.append('Apple')
fruits.append('Orange')
fruits.append('Grape')
fruits.append('Banana')
fruits.append('Licci')
print(fruits)
fruits.insert(3,'Jackfruit')
print(fruits)
fruits.extend(['Dragon','Bengi','Waterlemon','Apple','Grape'])
print(fruits)

#delete using index
del fruits[8]
print(fruits)

#delte using item name
fruits.remove('Apple')
print(fruits)
fruits.pop()#last in first out _LIFO
print(fruits)
print(dir(fruits))
print(fruits.index('Grape'))
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
print(f'total number of fruits:{len(fruits)}')

#slizing list 
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[0:3])
print(fruits[2:5])
print(fruits[3:])
print(fruits[:4])