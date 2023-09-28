#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

from colorama import Fore, Back, Style

# define functions here ...

max_num = int(input("Enter the amount of number: "))

def isPrime(value):

    for i in range(2, value):
        if value%i == 0:
            #print(f"The number {str(value)} is not prime, because we divided by {str(i)}")
            return False
        
    return True




def main():
    print(f"Starting to compute prime numbers up to {str(max_num)}.")

    for i in range(0, max_num):

        if isPrime(i):
            print(f"Number {Fore.RED+str(i)} is prime {Style.RESET_ALL}")
    else:
        print(f"Number {str(i)} is not prime")



if __name__ == "__main__":
    main()

# Ex2 é introduzir no terminal: ./ex1.py | grep "is prime" | wc -l
# Desta forma sabe-se quantos números primos existem no valor introduzido. Nota= sabendo que max_num tem que ser uma constante

#Ex3 é imprtar biblioteca de cores já pré existentes!