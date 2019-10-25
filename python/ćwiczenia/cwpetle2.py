#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cwpetla2.py
#  

def main(args):
    
    n = int(input("Podaj liczbę początkową zakresu: "))
    m = int(input("Podaj liczbę końcową zakresu: "))
    

    for liczba in range(n, m + 1):
        print(liczba, end = ' ')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
