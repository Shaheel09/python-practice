while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')

while True:
    print('Select a new password (letters and numbers only): ')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letter and numbers')

print('Your age is ',age)
print('Your password is ',password)