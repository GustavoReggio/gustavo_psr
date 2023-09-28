#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
import argparse
import readchar

#from colorama import Fore, Back, Style


# define functions here ...
#def printAllCharsUpto():
  #  print("Press a Key to read a char")
   # key = readchar.readkey()
   # print(f"User Presed {key}.")

    #number = ord(key)
    #print(f"Correspondin number is {str(number)}")

    #char_to_print = []
   # for i in range(32, number):
    #    print(chr(i), end="")
        #ou podemos criar uma lista:
        #char_to_print.append(char(i))
        #print(join(char_to_print))  ## isso deixará a lista sem separação e sem as chavetas indicativas de lista


# liinha b)
#def readAllUpTo(stop_char):
 #   chars = []
  #  while True:
   #     chars.append(readchar.readchar())
   #     print(chars[-1])
    #    if chars[-1]==stop_char:
    #        break


# linha c)  

def countNumbersUpto(stop_char):
    print("Enter a letter: ")
    
    keys =[]
    while True:
        key= readchar.readkey()
        keys.append(key)
        print(f"You typed {key}")

        if key == stop_char:
            break
        
    print(keys)

    n_numeric = 0
    for key in keys:
        if key.isnumeric():
            n_numeric +=1
    
    print(f"You pressed on {str(n_numeric)} numeric keys")


def main():
    #printAllCharsUpto()
    countNumbersUpto('x')
    
    print()
    

if __name__ == "__main__":
    main()