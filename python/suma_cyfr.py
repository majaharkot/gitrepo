#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_cyfr.py
#
# Dane wejściowe: liczba l2 co najmniej dwucyfrowa podawana przez użytkownika
# Dane wyjściowe: suma cufr liczby l2 wydrukowana w terminalu

def suma_cyfr(l2):
    
    suma = 0
    
    while l2 > 0:
        suma += l2 % 10
        l2 = int(l2 / 10)
        
    return suma

def main(args):
    
#    l2 = int(input("Podaj liczbę dwucyfrową: "))
#    
#    while l2 < 10:
#        l2 = int(input("Podaj liczbę dwucyfrową: "))
    
    assert(suma_cyfr(568) == 19)
    assert(suma_cyfr(9632) == 20)
    assert(suma_cyfr(18) == 9)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
