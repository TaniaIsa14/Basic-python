'''
For loop
------------
for vaiable in collection:
    statement
'''

data = list(range(20))
print(data)

y=list(range(1,11,3))
print(y)

for x in range(100):
    print(x,end='\t')

print('\n')
print('-'*50)

for x in range(10,80+1):
    if x % 2==0:
        print (x,end='\t' )
print('\n')       
print('-'*50)        
for x in range(10,80+1):
    if x %2 !=0:
         print(x,end='\t')

print('\n')       
print('-'*50)    

sum=0
for x in range(1,5):
    sum=sum+x
    print('\b =',sum)

print('\n')       
print('-'*50)    

'''
A-Z=65-90
a-z=96-122
back space=8
space bar=32
tab=9
0-9=48-56
'''



for x in range(65,91):
    print(chr(x),end='\t')

print('\n')
print('-'*50)

for x in range(96,122):
    print(chr(x),end='\t')

print('\n')

c= input('Enter a character value:')
print(f'ASCII Value of {c} is {ord(c)}')
print('\n')
d= int(input('Enter a value:'))
print(f'charcter Value of {d} is {chr(d)}')