'''

'''
while True:
    print('Main menu')
    print('1.Addition')
    print('2.subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Modulus')
    print('6.Exponent')
    print('7.Exit')
    print('Enter your selection:',end='')
    choice=int(input())
    if choice==1:
        a=int(input('enter value for a:'))
        b=int(input('enter value for b:'))
        print('Additon is %s'%(a+b))
        break
    elif choice==2:
        a=int(input('enter value for a:'))
        b=int(input('enter value for b:'))
        print('Subtraction is %s'%(a-b))
        break
    elif choice==3:
        a=int(input('enter value for a:'))
        b=int(input('enter value for b:'))
        print('Multiplication is %s'%(a*b))
        break
    elif choice==4:
        a=int(input('enter value for a:'))
        b=int(input('enter value for b:'))
        print('Division is %s'%(a/b))
        break
    elif choice==5:
        a=int(input('enter value for a:'))
        b=int(input('enter value for b:'))
        print('Modulus is %s'%(a%b))
        break
    elif choice==6:
        a=int(input('enter value for a:'))
        b=int(input('enter value for b:'))
        print('Exponent is %s'%(a**b))
        break
    elif choice==7:
        print('Thank you')
        break
else:
    print('Sorry invalid selection')