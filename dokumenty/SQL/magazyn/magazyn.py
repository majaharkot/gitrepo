#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def kwerenda_1(cur):
    cur.execute("""
        SELECT * FROM tbApps
    """)

    wyniki = cur.fetchall()  # pobranie wyszystkich rekordów na raz
    for row in wyniki:  # odczytywanie kolejnych rekordów
        print(tuple(row))  # drukowanie pól


def main(args):
    con = sqlite3.connect('magazyn.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('magazyn.sql', 'r') as plik:
       cur.executescript(plik.read())

    # dodawanie danych do tabeli
    dane = dane_z_pliku('dane_customers.txt')
    print(dane)
    dane.pop(0)  # usówanie pierwszego rekordu z listy
    cur.executemany('INSERT INTO tbCustomers VALUES(?, ?, ?)', dane)
    
    dane = dane_z_pliku('dane_orders.txt')
    print(dane)
    dane.pop(0)  # usówanie pierwszego rekordu z listy
    cur.executemany('INSERT INTO tbOrders VALUES(?, ?, ?, ?)', dane)

    dane = dane_z_pliku('dane_subscriptions.txt')
    print(dane)
    dane.pop(0)  # usówanie pierwszego rekordu z listy
    cur.executemany('INSERT INTO tbSubscription VALUES(?, ?, ?, ?)', dane)


    # przykład zapytania (kwerendy)
    # kwerenda_1(cur)

    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
