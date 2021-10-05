'''
example of nested if
'''
username=input('Enter user name:')
password=input('enter password:')
if  username.upper()=='Admin'.upper() and password=='tania':
    print(f'Wlcome Mr.{username}')
elif username.upper() =='Admin'.upper() and password !='tania':
    print('invalid Username')
elif username.upper() !='Admin'.upper() and password !='tania':
    print('invalid password')    
else:
    print('username and password both are wrong')