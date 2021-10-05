x=int(input('Enter Value for x:'))
y=int(input('Enter value for y:'))
z=int(input('Enter value for z:'))
w=int(input('Enter value for w:'))
if x>y and x>z and x>w:
    print(f'{x} is biggest')
elif y>x and y>z and y>w:
    print(f'{y} is biggest')
elif z>x and z>y and z>w:
    print(f'{z}is biggest')
elif w>x and w>y and w>z :
    print(f'{w} is biggest')

elif x ==y==z==w:
    print('Both are equal')
else:
    print('value is small')
