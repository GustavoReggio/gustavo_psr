#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#Exercício 5 Parte 2


#use imports here
import argparse
import readchar


# define functions here ...


"""def countNumbersUpto(stop_char):
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
    
    print("You pressed on")
    print(type(n_numeric))
    #print('You pressed on' +type(n_numeric) 'numeric keys')"""



#Linha b)

"""def countNumbersUpto(stop_char):
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
    keyNum =[]
    for key in keys:
        if key.isnumeric():
            n_numeric +=1
            keyNum.append(key)
    
    print(f"The numbers that you've pressed are: {str(n_numeric)}")
    print(keyNum)"""


# Linha c)

"""def countNumbersUpto(stop_char):
    print("Enter a letter: ")
    
    keys =[]
    dicio ={}
    n_numeric = 0
    while True:
        key= readchar.readkey()
        keys.append(key)
        print(f"You typed {key}")

        n_numeric +=1
        dicio[n_numeric]=key

        if key == stop_char:
            del dicio[n_numeric]
            break
        
    print(dicio)"""


# Linha d)

"""def countNumbersUpto(stop_char):
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
    keyNum =[]
    for key in keys:
        if key.isnumeric():
            n_numeric +=1
            keyNum.append(key)
    
    print(f"The numbers that you've pressed are: {str(n_numeric)}")
    keyNum.sort()
    print(keyNum)"""


# Linha e)

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
            
    
    print(f"The numbers that you've pressed are: {str(n_numeric)}")

    numKey = [x for x in keys]
    print('Numerical Key: '+ str(numKey))

    dic_keys= {idx:x for idx, x in enumerate(keys)}
    print('Numerical dicionar:'+ str(dic_keys))
    
    

def main():
    countNumbersUpto('x')

if __name__ == "__main__":
    main()