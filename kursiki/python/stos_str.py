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


def pop(rozmiar):
    
    global stos, SP
    
    SP -= 1  # dekrementacja
    
    if SP >= 0:
        print(stos[SP])
        stos[SP] = None
    else:
        print("Stack overflow!")

            
def main(args):
    
    global stos, SP
    rozmiar = int(input("Podaj rozmiar stosu: "))
    
    stos = [None] * rozmiar
    push(rozmiar, 2)
    push(rozmiar, 5)
    pop(rozmiar)
    push(rozmiar, 3)
    pop(rozmiar)
    pop(rozmiar)
    pop(rozmiar)
 
    print(SP)
    print(stos)
        
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
