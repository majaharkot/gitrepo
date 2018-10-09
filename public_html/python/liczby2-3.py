#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby2-3.py
# 


def liczby2(a=10, b=99):
    
    """
    Program drukuje wszystkie liczby dwucyfrowe o niepowtarzających się
    cyfrach oraz zwraca ilość takich liczb
    """
    for liczba in range(10, 99):
        if (liczba % 11) != 0:
            print(liczba)
        print()
			          
        
    
def liczby3(a=100, b=999):
    
    """
    Program drukuje wszystkie liczby trzycyfrowe o niepowtarzających się
    cyfrach oraz zwraca ilość takich liczb
    """

def main(args):
    
    print(liczby2())
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
