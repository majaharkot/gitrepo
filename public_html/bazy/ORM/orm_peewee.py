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

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
