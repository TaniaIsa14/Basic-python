username=input('Enter the username:')
password=input('Enter the password:')
if username.upper()=='admin'.upper():
    if password =='tania':
         print(f'Welcome Ms.{username}')
    else:
        print('invalid password')
else:
    print('sorry invalid user')
