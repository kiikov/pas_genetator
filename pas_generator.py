# Libraries import
import random # For generate a password
from colored import Fore # Just for the beauty text :)

# Set 'work' to 'True' to make our loop (line 98) work
work=True

# Create the function 'longgg' to ask for the password length
def longgg():
    global long
    while long<8:
        try:
            long=int(input(f'{Fore.white}Password length(min 8 characters, max 64): '))
            if long<8:
                print(f'{Fore.red}No less than 8 characters!!!')
            elif long>64:
                print(f'{Fore.red}No more than 64 characters!!!')
                long=0 # Set the value 'long' in 0 to start the cycle again
        except ValueError:
            print(f'{Fore.red}Enter a number!!!')

# Create a 'choice' function that will ask the user for possible options
def choice():
    global az, AZ, num, sym
    while az==None:
        try:
            az_inp=int(input(f'{Fore.white}Use lowercase letters (a-z)?\n 1. {Fore.green}Yes{Fore.white}\n 2. {Fore.red}No{Fore.white}\nEnter a number: '))
            if az_inp==1:
                az="abcdefghigklmnopqrstuvyxwz"
            elif az_inp==2:
                az=''
            else:
                print(f'{Fore.red}Enter numbers from the suggested!!!{Fore.white}')
        except ValueError:
            print(f'{Fore.red}Enter a number!!!{Fore.white}')
    
    while AZ==None:
        try:
            AZ_inp=int(input(f'Use the capital letters (A-Z)?\n 1. {Fore.green}Yes{Fore.white}\n 2. {Fore.red}No{Fore.white}\nEnter a number: '))
            if AZ_inp==1:
                AZ="ABCDEFGHIGKLMNOPQRSTUVYXWZ"
            elif AZ_inp==2:
                AZ=''
            else:
                print(f'{Fore.red}Enter numbers from the suggested!!!{Fore.white}')
        except ValueError:
            print(f'{Fore.red}Enter a number!!!{Fore.white}')

    while num==None:
        try:
            num_inp=int(input(f'Use the numbers (0-9)?\n 1. {Fore.green}Yes{Fore.white}\n 2. {Fore.red}No{Fore.white}\nEnter a number: '))
            if num_inp==1:
                num="1234567890"
            elif num_inp==2:
                num=''
            else:
                print(f'{Fore.red}Enter numbers from the suggested!!!{Fore.white}')
        except ValueError:
            print(f'{Fore.red}Enter a number!!!{Fore.white}')

    while sym==None:
        try:
            sym_inp=int(input(f'Use special symbols(e.g. !, @, #, $, %)?\n 1. {Fore.green}Yes{Fore.white}\n 2. {Fore.red}No{Fore.white}\nEnter a number: '))
            if sym_inp==1:
                sym="!@#$%&№"
            elif sym_inp==2:
                sym=''
            else:
                print(f'{Fore.red}Enter numbers from the suggested!!!{Fore.white}')
        except ValueError:
            print(f'{Fore.red}Enter a number!!!{Fore.white}')

# And here it is, the 'rand' function to generate the password
def rand():
    global long, az, AZ, num, sym, pas
    try:
        for i in range(long): 
            pas=pas+random.choice(az+AZ+num+sym) # Sum the variables whose values we defined in the 'choice' function (line 23)
        print(f'{Fore.white}Your password: ', pas)
    except IndexError:
        print(f'{Fore.red}Unable to generate a password as all options are disabled!{Fore.white}')

# The 'end' function to ask the user whether to continue the program
def end():
    global work
    try:
        end_inp=int(input(f'{Fore.white}Continue working?\n 1. {Fore.green}Yes{Fore.white}\n 2. {Fore.red}No(exit){Fore.white}\nEnter a number: '))
        if end_inp==1:
            work=True
        elif end_inp==2:
            work=False
            print(f'{Fore.green}Thanks for using!{Fore.white}')
        else:
            print(f'{Fore.red}Enter numbers from the suggested!!!{Fore.white}')
    except ValueError:
        print(f'{Fore.red}Enter a number!!!{Fore.white}')

while work:         # Cycle, all functions are in strict sequence
    long=0          # Set all variables to 'None' to reuse the code in the future
    az=None
    AZ=None
    num=None
    sym=None
    pas = ''
    longgg()
    choice()
    rand()
    end()