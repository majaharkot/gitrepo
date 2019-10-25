#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  algorytmy1.py

def wersja1():
    
    n = int(input("Podaj dowolną liczbę: "))
    
    for i in range(1, n, 2):
        print(i)

def wersja2():
    
    #algorytm częściowo poprawny
    #algorytm skończony
    #algorytm o złożoności liniowej 0(n)
    
    n = int(input("Podaj dowolną liczbę: "))
    i = 1
    
    while i < n:
        print(i)
        i +=2
    
def main(args):
    
    wersja2()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
