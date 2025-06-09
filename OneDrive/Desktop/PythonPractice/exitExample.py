'''import sys

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
        print('You typed ' + response + '.')

'''


'''spam = int(input())

if spam == 1:
    print("hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings")
    
'''

'''for i in range(1,11):
    print(i)

i = 1;
while i < 11:
    print(i)
    i = i + 1
'''

print('Please Enter Two numbers ')
firstNumber = int(input('Please enter \'First\' number :' ))

secondNumber = int(input('Please enter \'Second\' number : '))

chooseOperator = (input('Please choose the operator between + - * / : '))

if chooseOperator == "+":
    print(firstNumber + secondNumber)
elif chooseOperator == "-":
    print(firstNumber - secondNumber)
elif chooseOperator == "*":
    print(firstNumber * secondNumber)
elif chooseOperator == "/":
    print(firstNumber / secondNumber)
else:
    print('Please Enter the correct Operator. Thank You!!')
