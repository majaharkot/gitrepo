#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa01.py
#  

class Osoba():
    """ Prosta klasa opisująca osobę """
    
    def __init__(self, imie, nazwisko, hp):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ustawPlec(imie)
        self.hp = hp
        
    def ustawPlec(self, imie):
        if imie[-1] == "a":
            self.plec = "k"
            self.atak = 3
            self.blok = 1
        else:
            self.plec = "m"
            self.atak = 5
            self.blok = 2
            
    def atakuj(self, osoba):
        #osoba.hp -= self.atak
        osoba.blokuj(self.atak)
        
    def blokuj(self, atak):
        self.hp -= (atak - self.blok)
        if self.hp < 1:
            print("I'm dead :)")
        else:
            print("I'm still standing! Hit me baby one more time!") 
        
jakub = Osoba('Kuba', 'Gwizd', 10)
print(jakub.nazwisko, jakub.plec, jakub.hp)
michal = Osoba('Michał', 'Świst', 10)
print(michal.nazwisko, michal.plec, michal.hp)


print("Combat: ")
jakub.atakuj(michal)
jakub.atakuj(michal)
jakub.atakuj(michal)
jakub.atakuj(michal)
jakub.atakuj(michal)
jakub.atakuj(michal)
jakub.atakuj(michal)
jakub.atakuj(michal)
jakub.atakuj(michal)
jakub.atakuj(michal)

michal.atakuj(jakub)
michal.atakuj(jakub)
michal.atakuj(jakub)

print(jakub.hp, michal.hp)
