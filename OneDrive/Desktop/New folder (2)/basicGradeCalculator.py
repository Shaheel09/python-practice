# print('This program is use for Basic Grade Calculator')

# def gradeCalculator():
#     yourScore = int(input('Enter your percentage(%): '))

#     if yourScore >= 0 and yourScore <= 49:
#         print('Your score is \'F\' and it is Unacceptable')
#     elif yourScore >= 50 and yourScore <= 59:
#         print('Your score is \'D\' and it is Barely acceptable')
#     elif yourScore >= 60 and yourScore <= 69:
#         print('Your score is \'C\' and it is Satisfactory')
#     elif yourScore >= 70 and yourScore <= 79:
#         print('Your score is \'B\' and it is Good')
#     elif yourScore >= 80 and yourScore <= 89:
#         print('Your score is \'A\' and it is Excellent')
#     elif yourScore >= 90 and yourScore <= 100:
#         print('Your score is \'A+\' and it is Exceptional')
#     else:
#         print('Please Enter the correct percentage between 0 - 100')

# gradeCalculator()  THIS IS MY PROGRAM


print("This program is used for a Basic Grade Calculator") #THIS IS CHATGPT PROGRAM

def gradeCalculator():
    try:
        yourScore = int(input("Enter your percentage (%): "))

        if yourScore < 0 or yourScore > 100:
            print("❗ Please enter a percentage between 0 and 100.")
        elif yourScore >= 90:
            print("Your grade is 'A+' — Exceptional")
        elif yourScore >= 80:
            print("Your grade is 'A' — Excellent")
        elif yourScore >= 70:
            print("Your grade is 'B' — Good")
        elif yourScore >= 60:
            print("Your grade is 'C' — Satisfactory")
        elif yourScore >= 50:
            print("Your grade is 'D' — Barely acceptable")
        else:
            print("Your grade is 'F' — Unacceptable")
    except ValueError:
        print("❗ Please enter a valid number.")

gradeCalculator()
