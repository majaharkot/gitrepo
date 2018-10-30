#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  

from math import sqrt

def main(args):
    
    a, b, c = eval(input("Podaj boki trójkąta oddzielone przecinkami: "))
    print("Podano boki: {}, {}, {}".format(a, b, c))
    
    trojkat = False
    
    if a + b > c and \
       a + c > b and \
       b + c > a:
        trojkat = True
                
    if trojkat:
        print("Da się zbudować trójkąt!")
        
        if a**2 + b**2 == c**2 or \
           a**2 + c**2 == b**2 or \
           c**2 + b**2 == a**2:
            print("W dodatku prostokątny!")
        else:
            print("Ale nie prostokątny!")
            
        p = (a + b + c) / 2
        pole = sqrt(p * (p - a) * (p - b) * (p - c))
        print("Pole {:.2f}".format(pole))
        
    else:
        print("Nie da się zbudować trójkąta!")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
