#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kodmorsea.py
#  

kod = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..','e':'.', 
       'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---',
       'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---',
       'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
       'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-','y':'-.--',
       'z':'--..', 'ą':'.-.-', 'ć':'-.-..', 'ę':'..-..', 'ch':'----',
       'ł':'.-..-', 'ń':'--.--', 'ó':'---.', 'ś':'...-...',
       'ż':'--..-.', 'ź':'--..-', ' ':' '
      }

def koduj():
    
    tekst = input('Podaj tekst: ').lower()
    
    print("".join([kod[litera] for litera in tekst]))
    
    # ~for litera in tekst:
        # ~if litera != ' ':
            # ~print(kod[litera])
            

def dekoduj():
    tekst = []
    litery = list(kod.keys())
    litera = ' '
    while litera > '':
        litera = input('Podaj literę w kodzie Morsea: ')
        tekst.append(litera)
    print(tekst)

    print(litery[tekst.indeks(tekst))

def main(args):
    
    koduj()
    
    dekoduj()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
