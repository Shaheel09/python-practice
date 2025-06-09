print('This program can convert Celsius into Fahrenheit or Fahrenheit into Celsius')


def fToCConverter():
    fahrenheitTemp = float(input('Enter a Fahrenheit Temperature: '))
    celsiusTemp = (fahrenheitTemp - 32) * 5/9
    print('Your converted celsius temperature is ', celsiusTemp)

def cToFConverter():
    cTemp = float(input('Enter a Celsius Temperature: '))
    fTemp = (cTemp * 9/5) +32
    print('Your converted fahrenheit temperature is', fTemp)

#Let user choose the type of conversion
                  
choice = input("Type 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ").upper()

if choice == 'C':
    cToFConverter()
elif choice == 'F':
    fToCConverter()
else:
    print("Invalid input. Please enter 'C' or 'F'.")
