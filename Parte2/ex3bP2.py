#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import argparse

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

    parser = argparse.ArgumentParser(description='script to compute numbers.')
    #parser.add_argument('-mn', '--maximum_number' type=int, help='max number.')
    parser.add_argument('-n', '--name', type=str, help= 'A name to print.', required = False, default='Antônio')

    args =vars(parser.parse_args())
    print(args)

    print('tarting to compute perfect numbers up to' + str(args[maxNum]))

    for i in range(1, maxNum):
        if isPerfect(i):
            print(f"Number {str(i)} is perfecr.")



if __name__ == "__main__":
    main()