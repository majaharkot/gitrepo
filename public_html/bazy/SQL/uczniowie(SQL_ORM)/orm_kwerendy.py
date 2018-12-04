#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_kwerendy.py
#  

from orm_modele import *

def kw01():
    
    #obj = Uczen.select().where(Uczen.imie.startswith('G'))
    obj = Uczen.select().where(Uczen.imie == 'Rafał')
    for row in obj:
        print(row.nazwisko, row.imie)
    
def main(args):
    
    baza.connect()
    
    kw01()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
