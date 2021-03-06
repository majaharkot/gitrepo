#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rysuj_prostokat.py
#  
# DANE WEJŚCIOWE: boki a i b prostokąta
# DANE WYJŚCIOWE: prostokąt narysowany gwiazdkami w terminalu o rozmiarach
#                 podanych przez użytkownika
# EXTRA: znak, którym rysowany jest prostokąt, można pobrać od użytkownika
#

def main(args):
        
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    znak = input("Podaj znak, którym chcesz rysować: ")
    
    i = 0
    j = 0
    
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b-1 or i == 0 or i == a-1:
                print(znak, end='')
            else:
                print(" ", end='')
    
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
