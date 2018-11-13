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
            self.__plec = "k"
            self.__atak = 3
            self.__blok = 1  # __ właściwości ukryte nie można jej odczytać
        else:
            self.__plec = "m"
            self.__atak = 5
            self.__blok = 2
            
    def atakuj(self, osoba):
        #osoba.hp -= self.atak
        osoba.blokuj(self.__atak)
        
    def blokuj(self, atak):
        self.hp -= (atak - self.__blok)
        if self.hp < 1:
            print("I'm dead :)")
        else:
            print("I'm still standing! Hit me baby one more time!") 
        
jakub = Osoba('Kuba', 'Gwizd', 10)
jakub.wzrost = 170
print(jakub.__dict__)

exit()

jakub.__plec = "m"

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
