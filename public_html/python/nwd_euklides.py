#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nwd_euklides.py
#  

def nwd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
    
def main(args):
    
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj liczbę: "))
    
    print("NWD {} i {} jest {} ". format(a, b, nwd(a, b)), end='')
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
