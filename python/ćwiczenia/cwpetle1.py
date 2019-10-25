#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cwpetle1.py
#  

def main(args):

    wynik = 0
    liczba = int(input("Podaj liczbę: "))
	
    while wynik <= 75:
        wynik = wynik + liczba
    print("Suma: ", wynik)

        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
