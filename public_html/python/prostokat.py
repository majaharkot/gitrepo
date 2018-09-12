#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat.py
#  
# ZADANIE: napisz program, który liczy pole i obwód prostokąta
# DANE WEJŚCIOWE: liczby całkowite podawane przez użytkownika
# WYJŚCIE: komkomunikat w terminalu o obliczonym obwodzie i polu
#  

def obwod(a, b):
    return 2 * a + 2 * b
    
def pole(a, b):
    return a * b

def main(args):
    
    a = int(input("Podaj długość boku a: "))
    print(a)
    b = int(input("Podaj długość boku b: "))
    print(b)
    
    print("Obwód: ", obwod(a, b))
    print("Pole: ", pole(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
