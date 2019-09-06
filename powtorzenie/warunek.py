#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunek.py
# 
 
def najwieksza(a, b, c):
    
    maks = a 
    
    if b > maks:
        maks = b
        
    if c > maks:
        maks = c
        
    return maks

def main(args):
    
    a = int(input("Podaj 1. liczbę: "))
    b = int(input("Podaj 2. liczbę: "))
    c = int(input("Podaj 3. liczbę: "))
    
    maks = najwieksza(a, b, c)
    
    print("Najwiekszą liczbą jest ", maks)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
