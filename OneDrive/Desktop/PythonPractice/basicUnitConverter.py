# def kmToMiles():
#     miles = float(input("Enter a Kilometer to convert into Miles: "))
#     kmToM = miles * 0.621371
#     print(kmToM) 

#     km = float(input("Enter a Miles to convert into Kilometer: "))
#     mToKm = km * 1.60934
#     print(mToKm)

# def poundsToKM():
#     pounds = float(input('Enter a pounds to convert into Kilograms: '))
#     pToKm = pounds/2.20462
#     print(pToKm)

#     kg = float(input('Enter a Kilogram to convert into Pounds: '))
#     kgToPounds = kg * 2.205
#     print(kgToPounds)

# def inchesToCm():
#     inches = float(input('Enter a inches to convert into Centimeter: '))
#     iToCm = inches * 2.54
#     print(iToCm)

#     cm = float(input('Enter a Centimeter to convert into Inches: '))
#     cmToI = cm / 2.54
#     print(cmToI)

# kmToMiles()
# poundsToKM()
# inchesToCm()

def kmToMiles():
    km = float(input("Enter kilometers to convert into miles: "))
    miles = km * 0.621371
    print(f"{km} kilometers = {round(miles, 3)} miles")

    miles = float(input("Enter miles to convert into kilometers: "))
    km = miles * 1.60934
    print(f"{miles} miles = {round(km, 3)} kilometers")

def poundsToKG():
    pounds = float(input("Enter pounds to convert into kilograms: "))
    kg = pounds / 2.20462
    print(f"{pounds} pounds = {round(kg, 3)} kilograms")

    kg = float(input("Enter kilograms to convert into pounds: "))
    pounds = kg * 2.20462
    print(f"{kg} kilograms = {round(pounds, 3)} pounds")

def inchesToCm():
    inches = float(input("Enter inches to convert into centimeters: "))
    cm = inches * 2.54
    print(f"{inches} inches = {round(cm, 3)} cm")

    cm = float(input("Enter centimeters to convert into inches: "))
    inches = cm / 2.54
    print(f"{cm} cm = {round(inches, 3)} inches")

# Call the functions
kmToMiles()
poundsToKG()
inchesToCm()
