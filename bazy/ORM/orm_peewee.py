#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
#
# DOKUMENTACJA:
#   http://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table
#

import os
from peewee import *

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik) #określanie instancji bazy


### MODELE DANYCH ###

class BazaModel(Model):

    class Meta :
        database = baza


class Klasa(BazaModel): #nazwa classy zawsze z dużej litery

    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)


class Uczen(BazaModel):

    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    
# RELATED_NAME TO NAZWA DODATKOWEGO POLA W KTÓRYM BĘDĄ ZAWARTE INFORMACJE 
# W TYM WYPADKU O WSZYSTKICH UCZNIACH W DANEJ KLASIE


class Wynik(BazaModel):

    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')

# RELATED_NAME TO NAZWA DODATKOWEGO POLA W KTÓRYM BĘDĄ ZAWARTE INFORMACJE 
# W TYM WYPADKU O WSZYSTKICH WYNIKACH DANEGO UCZNIA


def main(args):
    
    if os.path.exists(baza_plik):
        os.remove(baza_plik)

    baza.connect() #połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])

    #dodawanie danych
    kl2a = Klasa(nazwa="2A", roknaboru=2010, rokmatury=2013)
    kl2a.save()
    
    kl1a = Klasa(nazwa="1A", roknaboru=2009, rokmatury=2012)
    kl1a.save()
    
    u1 = Uczen(imie="Jakub", nazwisko="Kowalski", plec=False, klasa=kl2a)
    u1.save()
    
    u2 = Uczen(imie="Anna", nazwisko="Gacek", plec=True, klasa=kl1a)
    u2.save()
    
    u3 = Uczen(imie="Roman", nazwisko="Polek", plec=False, klasa=kl1a)
    u3.save()

    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.nazwisko, uczen.klasa.nazwa)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
