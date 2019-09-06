#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wej_wyj.py
#  

def main(args):
    
    imie = input("Jak masz na imię?     ")
    nazwisko = input("Jak masz na nazwisko?     ")
    
    print("Witaj", imie, nazwisko, "!")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
