def collatz(number): #collatz function with the parameter named number
    if number % 2 == 0:
        print(number//2)
        return number //2
    elif number % 2== 1:
        print(3* number + 1)
        return 3* number + 1



newValue = int(input('Enter a number : \n'))
userType = collatz(newValue)

while userType != 1:
    if userType % 2 == 0:
        userType = userType // 2
        print(userType)
    else:
        userType = 3 * userType + 1
        print(userType)
    
    
