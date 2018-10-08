#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cwpetle3.py
#  

def main(args):
    
    wynik = 0
    
    a = int(input("Podaj liczbę końcową zakresu: "))
    
    for liczba in range(0, a + 1):
		wynik = liczba * liczba
		print(wynik)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
