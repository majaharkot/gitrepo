#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py


def main(args):
    
    a = int(input("Podaj liczbę początkową zakresu: "))
    b = int(input("Podaj liczbę końcową zakresu: "))
    
    while a >= b:
        b = int(input("Podaj większą liczbę końcową niż początkową zakresu: "))

    for liczba in range(a, b + 1):
        if not liczba % 2:
            print(liczba)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
