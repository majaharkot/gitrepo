#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#
#Program pobiera trzy liczby od użytkownika,
# a następnie wyświetla liczbę największą.

def maks(a, b, c):
    m = None
    if a > b:
        if a > c:
            m = a
    elif b > c:
            m = b
    print("Największa:", m)
    
    return m;

def main(args):
    
    assert(maks(3, 2, 1) == 3)
    assert(maks(2, 3, 1) == 3)
    assert(maks(1, 2, 3) == 3)
    assert(maks(3, 2, 1) == 3)
    assert(maks(3, 2, 1) == 3)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
