#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LIFO - Last In First Out  <- stos
# FIFO - First In First Out  <- kolejka

stos = []  #stos jako lista 
SP = 0

def push(rozmiar, dane):

    global stos, SP

    if SP < rozmiar:
        stos[SP] = dane
        SP += 1
    else:
        print("Stack overflow!")


def pop():

    global stos, SP
    
    SP -=1
    if SP > -1:
        print(stos[SP])
        stos[SP] = None
    else:
        print("Index out of range!")
        SP = 0


def main(args):

    global stos, SP
    rozmiar = int(input("Podaj rozmiar stosu: "))
    stos = [None] * rozmiar
    push(rozmiar, 5)
    push(rozmiar, 9)
    push(rozmiar, 11)
    print("Wskaźnik ", SP)
    pop()
    pop()
    pop()
    pop()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
