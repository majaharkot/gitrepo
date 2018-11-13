#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  car.py
#  

#napisz definicję obiektu samochód z następująccymi argumentami:
# marka, np.Fiat
# model, np.Tipo
# rok produkcji, np. 2005
# nadwozie, np. sedan

#metody obiektu:
# wiek() - zwraca wiek auta w latach

from datetime import date

class Auto():
    
    def __init__(self, marka, model, rokP, nadwozie):
        self.marka = marka
        self.model = model
        self.rokP = rokP
        self.nadwozie = nadwozie
        
    def wiek(self):
        return date.today().year - self.rokP
        
fiacik = Auto('Fiat', 'Tipo', '2005', 'sedan')

print(fiacik.wiek())
