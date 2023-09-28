#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from math import sqrt

#Exercício 3 Parte 2

maxNum = 30
# define functions here ...

def getDiv(value):
    
    dividers = []
    
    
    for i in range(1,int(value/2)):
        if value %i == 0:
            dividers.append(i) 

    return dividers


def isPerfect(value):
    dividers = getDiv(value)

    return value == sum(dividers)



def main():
    print(f"Starting compute perfect numbers up to {maxNum}")

    for i in range(1, maxNum):
        if isPerfect(i):
            print(f"Number {str(i)} is perfecr.")
    

if __name__ == "__main__":
    main()