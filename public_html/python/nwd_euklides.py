#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nwd_euklides.py
#  

def nwd_klasyczny(a,b):
    
    licznik = 0
    
    while a != b:
        if a > b:
            a = a - b
            licznik += 1
        else:
            b = b - a
            licznik += 1
            
    print("Liczba powtórzeń: ", licznik)
    
    return a
    
def main(args):
    
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    
    print(nwd_klasyczny(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
