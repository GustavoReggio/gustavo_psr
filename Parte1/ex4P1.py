#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python



## Eercício 4 parte 1

#use imports here

# define functions here ...

max_num =int(input("Enter a number: "))

def isPerfect(value):
    cumsum = 0
    for i in range(1, value):
        if value%i == 0:
            cumsum += i
    
    if cumsum == value: # pode ser substituido por: return cumsum ==  value

        return True
    else:
        return False

    
    return False

def main():
    print(f"Starting to compute perfect numbers up to {str(max_num)}")

    for i in range(1, max_num):
        if isPerfect(i):
            print(f"Number {str(i)} is perfect")
    

if __name__ == "__main__":
    main()