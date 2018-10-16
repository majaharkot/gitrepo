#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nwd_euklides.py
#  

def nwd_klasyczny(a,b):
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return a
    
def main(args):
    
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    
    print(nwd_klasyczny(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
