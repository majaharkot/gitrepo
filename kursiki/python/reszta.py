#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reszta.py
#  


def pobierzNominaly():
    
    nominaly = set([200, 100, 50, 20, 10, 5, 2, 1])
    n = int(input('Podaj nominał lub 0 aby zakończyć: '))
    listaNm = []
    
    while n > 0:
        if n in nominaly:
            listaNm.append(n)
        else:
            print('Błąd')
            
        n = int(input('Podaj nominał lub 0 aby zakończyć: '))
        
    listaNm.sort(reverse = True)  # sortowanie malejące
    
    return listaNm


def wydajR1(r, l):
    
    i = 0  # indeks nominału
    
    while r > 0:
        if r >= l[i]:
            ileNm = int(r / l[i])
            r -= ileNm * l[i]
            print("{} x {} zł".format(ileNm, l[i]))
        i += 1
        
        
def wydajR2(reszta, listaNm):
    i = 0 # indeks nominału
    liczbaNm = len(listaNm)  # liczba nominałów
    
    while reszta > 0 and i < liczbaNm:
        while i < liczbaNm and reszta < listaNm[i]:
            i+= 1
        if i < liczbaNm and reszta >= listaNm[i]:
            nominal = listaNm[i]
            ileNm = int(reszta / nominal)
            if ileNm > listaNm.count(nominal):
                ileNm = listaNm.count(nominal)
            reszta -= ileNm * nominal
            
            for j in range(ileNm):
                listaNm.remove(nominal)
                liczbaNm -= 1
            i = 0
            print("{} X {}".format(ileNm, nominal))
            
    if reszta > 0:
        print("Brak nominałów do wydania {} zł".format(reszta))


def main(args):
    
    #listaNm = [20, 10, 2, 1]
    listaNm = pobierzNominaly()
    
    reszta = int(input('Podaj resztę: '))
    
    #wydajR1(reszta, listaNm)
    wydajR2(reszta, listaNm)
    
    return 0
    
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
