#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Harkot_przeszukiwanie.py
#  

import random

def main(args):

    n = 6
    szuk = 4
    tab = [1, 5, 3, 8, 0, 6, None]
    tab[n] = szuk
    i = 0
    
    while tab[i] != szuk:
        i += 1
    
    if i < n:
        print("Znaleziony")
    
    else:
        print("Nie znaleziony")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
