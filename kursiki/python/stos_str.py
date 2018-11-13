#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stos_str.py
#  wersja strukturalna
#  

stos = []  # definicja pustej listy o zasięgu globalnym
SP = 0  # wskaźnik wierzchołka


def push(rozmiar, dane):
    
    global stos, SP
    
    if SP < rozmiar:
        stos[SP] = dane
        SP += 1  # inkrementacja
    else:
        print("Stack overflow!")

def pop()

            
def main(args):
    
    global stos, SP
    rozmiar = int(input("Podaj rozmiar stosu: "))
    
    stos = [None] * rozmiar
    push(rozmiar, 2)
    print(SP)
    push(rozmiar, 5)
    print(SP)
    push(rozmiar, 8)
    print(SP)
    push(rozmiar, 3)
    print(SP)
    
    print(stos)
        
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
