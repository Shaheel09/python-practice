userEnter = int(input('Enter a number: '))

sum1 = 0

for num in str(userEnter):
    print(num)
    sum1 += int(num)

print('Sum of digits:', sum1)