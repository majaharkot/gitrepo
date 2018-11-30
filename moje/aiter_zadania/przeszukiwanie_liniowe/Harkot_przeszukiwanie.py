#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Harkot_przeszukiwanie.py
#  

import random

def main(args):

    a = int(input("Podaj liczbę: "))

    
    liczby = []
    
    for i in range(10):
        liczby.append(random.randint(1, 50))
    
    print(liczby)
    
    for liczba in range (len(liczby)):
        if liczby.cout(a) == 0 or a > 50:
            print("Nie ma takiej liczby w liście")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
