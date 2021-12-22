'''
Python recursion
----------------
A function that calla itself.
recurtion is the process of defining something in trems of itself
Hw--->fabonic number using recurtion
'''
#Factorial using loop
#3!=3X2X1
fact=1
num=int(input('Enter a value for factorial:'))
for i in  range(1,num+1):
    fact= fact*i
print(f'The factorial of {num} is {fact}')

#Factorial using recursion method

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)




'''
Factoeial(4)
    4*factorial(4-1)
     4*3*factorial(3-1)
     4*3*2*factorial(2-1)
     4*3*2*1factorial(1-1)
      4*3*2*1
'''
print(f'The factorial of {num} is {factorial(num)}')
print(factorial(7))