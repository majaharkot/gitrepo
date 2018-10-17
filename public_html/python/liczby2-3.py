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
    ile = 0
    
    for d in range(1, 10):  # pętla dziesiątek
        for j in range(0, 10):  # pętla jedności
            if d != j:
                print("{}{} ".format(d, j), end="")
                ile += 1
    
    return ile         
        
        
def liczby3(a=100, b=999):
    
    """
    Program drukuje wszystkie liczby trzycyfrowe o niepowtarzających się
    cyfrach oraz zwraca ilość takich liczb
    """
    ile=0
    
    for s in range(1, 10):
        for d in range(0, 10):
            for j in range(0, 10):
                if s != d and s != j and d != j:
                    print("{}{}{} ".format(s, d, j), end='')
                    ile += 1
    return ile


def main(args):
    
    print(liczby2())
    print(liczby3())
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
