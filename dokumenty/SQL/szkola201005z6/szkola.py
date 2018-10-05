#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szkola.py
#  

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=';')
        for rekord in tresc:
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane

def main(args):
    con = sqlite3.connect('szkola.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('szkola.sql', 'r') as plik:
       cur.executescript(plik.read())

    # dodawanie danych do tabeli
    dane = dane_z_pliku('szkoła_z6pr052010_oceny.txt')
    print(dane)
    dane.pop(0)  # usówanie pierwszego rekordu z listy
    cur.executemany('INSERT INTO tbOceny VALUES(?, ?, ?, ?)', dane)
    
    dane = dane_z_pliku('szkoła_z6pr052010_przedmioty.txt')
    print(dane)
    dane.pop(0)  # usówanie pierwszego rekordu z listy
    cur.executemany('INSERT INTO tbPrzedmioty VALUES(?, ?, ?, ?)', dane)

    dane = dane_z_pliku('szkoła_z6pr052010_uczniowie.txt')
    print(dane)
    dane.pop(0)  # usówanie pierwszego rekordu z listy
    cur.executemany('INSERT INTO tbUczniowie VALUES(?, ?, ?, ?, ?, ?)', dane)

    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
