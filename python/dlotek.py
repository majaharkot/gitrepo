#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = int(input("Podaj ilość typowanych liczb:"))  # integer
    maxliczba = int(input("Podaj maksymalną losowaną liczbę:"))
    print("Wytypuj {} z {} liczb".format(ileliczb, maxliczba))

    # losowanie liczb
    liczby = []  # lista wylosowanych liczb
    for i in range(ileliczb):  # pętla
        liczba = random.randint(1, maxliczba)
        if liczby.count(liczba) == 0:  # sprawdzenie czy wartość jest w liście
            liczby.append(liczba)
    print(liczby)
        # odp = input("Podaj liczbę od 1 do 10:")
        # print("Podałeś liczbę:", odp)

        # if liczba == int(odp):  # porównanie odpowiedzi z liczbą
        #     print("Zgadłeś!")
        #     break  # przerwanie działania pętli
        # else:
        #     print("Spróbuj jeszcze raz!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
