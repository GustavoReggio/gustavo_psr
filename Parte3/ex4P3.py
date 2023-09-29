#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from collections import namedtuple



# define functions here ...

class complex:
    def __init__(self, r, i) :
        self.r = r
        self.i = i
    
    def add(self, y):
        real = self.r + y.r
        im = self.i + y.i
        complextuple = complex(real, im)
        return complextuple
    
    def mult(self, y):
        real = self.r * y.i - self.r * y.i
        im = self.r * y.i + self.r * y.i
        complextuple = complex(real, im)
        return complextuple
    
    def __str__(self):
        if self.i > 0:
            return str(self.r) + "+" + str(self.i) + "i"
        else:
            return str(self.r) + "-" + str(self.i) + "i"


def main():
    c1 = complex(3,5)
    c2 = complex(-2, 7) 

    print(f"c1= {str(c1)}")

    c3 = c1.add(c2)
    print(f"c1 +c2 = {str(c3)}")

    c4 = c1.mult(c2)
    print(f"c1 x c2 = {str(c4)}")
    

if __name__ == "__main__":
    main()