def timeUntil100():
    userName = input('Enter your Name: ')
    userAge = int(input('Enter your Age: '))

    if userAge < 100:
        print(f'Hello, {userName}! Your age is {userAge} and This many years which is {100 - userAge} Years left until you become 100 years old.')
    else:
        print(f'If your age is {userAge} then you\'ve already crossed 100 years. Congratulations.')

timeUntil100()


# def timeUntil100():
#     userName = input("Enter your name: ")
#     userAge = int(input("Enter your age: "))

#     if userAge < 100:
#         years_left = 100 - userAge
#         print(f"Hello, {userName}! You have {years_left} years left until you turn 100.")
#     elif userAge == 100:
#         print(f"Wow, {userName}! You are exactly 100 years old. Congratulations!")
#     else:
#         years_over = userAge - 100
#         print(f"{userName}, you've already crossed 100 by {years_over} years. Amazing!")

# timeUntil100()