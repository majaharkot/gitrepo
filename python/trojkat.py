#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py

def trojkat(a, b, c):
    """
    funkcja przyjmuje trzy liczby - długości boków
            sprawdza, czy da się z nich zbudować trójkąt
            zwraca True jeśli się da, False w przeciwnym razie 
    """
    
    wynik = False
    
    if a + b > c and a + c > b and b + c > a:
        wynik = True
    
    return wynik

def main(args):
    assert(trojkat(3, 6, 8) == True)
    assert(trojkat(3, 5, 9) == False)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
