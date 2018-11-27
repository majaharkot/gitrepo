##!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  onp.py

from stos_obj import Stos

def czy_poprawne(onp):
    for z in onp:
        if z.isalpha():
            return False
    return True

def main(args):
    stos = Stos()
    onp = input("Podaj wyr. ONP, oddzielając operandy i operatory spacjami:\n")
    if not czy_poprawne(onp):
        print("Błąd wyrażenia!")
        return 0
    # 3 3 7 + *
    onp = onp.split(" ")
    
    for el in onp:
       if el.isdigit():
           stos.push(el)
       else:
           a = stos.pop()
           b = stos.pop()
           stos.push(eval(str(b) + el + str(a)))

    print("Wynik: ", stos.pop())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
