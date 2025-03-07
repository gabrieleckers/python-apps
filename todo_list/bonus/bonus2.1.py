password = input('Enter password: ')

while password != 'pass123':
    print('Password is incorrect.')
    password = input('Enter password: ')

print('Password was correct.')