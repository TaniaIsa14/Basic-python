#prime number

s=int(input('Enter the Value:'))
i=2
while i<s:
    if s%i==0:
       print('This not prime number')
       break
       i+=1
    else:
        print('This prime number')
        break
