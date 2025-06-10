from colorama import Fore, Style, init

init(autoreset=True)

def fizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(Fore.MAGENTA + 'Fizz')
        elif i % 3 == 0:
            print(Fore.GREEN + 'Buzz')
        elif i % 5 == 0:
            print(Fore.CYAN + 'fizzBuzz')
        else:
            print(Fore.YELLOW + str(i))

fizzBuzz()