#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py


def main(args):
    
    a = int(input("Podaj liczbę początkową zakresu: "))
    b = int(input("Podaj liczbę końcową zakresu: "))
    
    if a < b:
        for liczba in range(a, b + 1):
            #if liczba % 2 == 0:
            if not liczba % 2:
                print(liczba)
    else:
        print("Pierwsza liczba musi być mniejsza od drugiej :)")
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
