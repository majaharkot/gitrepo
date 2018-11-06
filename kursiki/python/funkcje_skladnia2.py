#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje_skladnia2.py
#

def mnoz(a, b):
    print(a*b)

def mnoz2(*args):  # zmienna lista argumentów
# funkcja liczy silnię :) 
    wynik = 1
     
    for liczba in args:
         wynik *= liczba 
    print(wynik)

def wylicz(imie1='Adam', imie2='Ewa', **kwargs):

    print(imie1)
    print(imie2)
    
    for k, v in kwargs.items():
        print('{} {}'.format(k,v))

# typy argumentów w funkcjach:
##### pozycyjne (wymagane)
##### nazwane (wymagane)
##### domyślne (niewymagane)
##### zmiennej długości: listy, słowniki

def main(args):
    
    #mnoz(4, 6)
    
    #mnoz2(4, 6, 8, 9, 3)
    
    wylicz(imie2='Ola', imie3='Piotr', imie4='Alfons')
    
    return 0
    
if __name__ == '__main__':
    # skrypt został uruchomiony a nie zainportowany
    import sys
    sys.exit(main(sys.argv))
