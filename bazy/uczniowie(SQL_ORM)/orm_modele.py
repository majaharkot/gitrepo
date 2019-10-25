#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_modele.py
#  

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
    plec = IntegerField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    

class Przedmiot(BazaModel):
    
    nazwa = CharField(null=False)
    imienaucz = CharField(null=False)
    nazwiskonaucz = CharField(null=False)
    plecnaucz = IntegerField()
    
    
class Ocena(BazaModel):
    
    datad = DateField(null=False)
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    ocena = DecimalField(null=False)
