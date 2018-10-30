#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reszta.py
#  

def wydaj1(r, l):
    
    i = 0  # indeks nominału
    
    while r > 0:
        if r >= l[i]:
            ileNm = int(r / l[i])
            r -= ileNm * l[i]
            print("{} x {} zł".format(ileNm, l[i]))
        i += 1
        

def main(args):
    
    listaNm = [200, 100, 20, 10, 5, 2, 1]
    reszta = int(input("Podaj resztę do wydania: ")
    wydaj1(reszta, listaNm)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
