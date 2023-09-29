#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here
from colorama import Fore, Back, Style
import math 
from collections import namedtuple


# define functions here ...

def addcomplex(x,y):
    real = x.real + y.real
    im = x.imagin + y.imagin
    complextuple = complex(real, im)
    return complextuple

def timescomplex(x, y):
    real = x.real * y.imagin - x.real * y.imagin
    im = x.real * y.imagin + x.real * y.imagin
    complextuple = complex(real, im)
    return complextuple

"""def printcomplex(x):
    real = x.real
    imagin =x.imagin
    print(f"Complex number: {str(real)+{imagin}i}")"""


complex = namedtuple('complex', ['real', 'imagin'])
c1 = complex(5, 3)
c2 = complex(-2, 7)

c3 = addcomplex(c1, c2)
print(c3)
 
c4 = timescomplex(c1, c2)
print(c4)

c5 = addcomplex(c1, c3)
print(c5)
