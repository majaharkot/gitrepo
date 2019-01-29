#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys


class Plansza():
    """ Plansza gry """

    def __init__(self, szer, wys):
        """ Konstruktor, przygotowanie okna gry """
        self.pow = pygame.display.set_mode((szer, wys), 0, 32)
        pygame.display.set_caption('Gra w życie')

    def rysuj(self, *args):
        """ Rysowanie okna gry """
        # kolor okna gry, składowe RGB podane w tupli
        self.pow.fill((0, 0, 0))
        for obj in args:
            obj.rysuj_na(self.pow)
        pygame.display.update()


class LifeGra():
    """ Kontroler gry """

    def __init__(self, szer, wys, roz=10):
        pygame.init()
        self.plansza = Plansza(szer * roz, wys * roz)
        self.populacja = Populacja(szer, wys, roz)
        self.fpsClock = pygame.time.Clock()

    def uruchom(self):
        """ Główna pętla programu """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN:
                self.populacja.obsluz_mysze()
            if event.type == KEYDOWN and event.key == K_RETURN:
                self.uruchomiona = True

            self.plansza.rysuj(self.populacja)

            if getattr(self, "uruchomiona", None):
                self.populacja.wylicz_generacje()
            self.fpsClock.tick(15)


DEAD = 0
ALIVE = 1


class Populacja():
    """ Populacja komórek """

    def __init__(self, szer, wys, roz=10):
        """ Przygotowuje ustawienia populacji """
        self.roz = roz
        self.wys = wys
        self.szer = szer
        self.generacja = self.utworz_generacje()

    def utworz_generacje(self):
        """ Tworzy i zwraca macierz pustej populacji """
        # wyrażenie listowe tworzące listę, której elementami są inne listy
        return [[DEAD for y in range(self.wys)] for x in range(self.szer)]

    def obsluz_mysze(self):
        przyciski = pygame.mouse.get_pressed()  # stan przycisków myszy
        if not any(przyciski):  # jeżeli żadnego nie naciśnięto
            return  # wychodzimy z metody

        x, y = pygame.mouse.get_pos()  # pozycja kursora na planszy w pikselach
        # wyliczenie indeksów komórki w macierzy
        # współrzędne w pikselach dzielimy przez rozmiar komórki
        x /= self.roz
        y /= self.roz

        # naciśnięcie lewego przycisku ozancza życie, prawego śmierć
        stan = True if przyciski[0] else False
        print(stan)
        # ustaw stan komórki w macierzy
        self.generacja[int(x)][int(y)] = ALIVE if stan else DEAD

    def rysuj_na(self, pow):
        """ Rysuje komórki na planszy """
        for x, y in self.zywe_komorki():
            roz = (self.roz, self.roz)
            pozycja = (x * self.roz, y * self.roz)
            kolor = (255, 255, 255)
            grubosc = 1
            pygame.draw.rect(pow, kolor, Rect(pozycja, roz), grubosc)

    def zywe_komorki(self):
        """ Generator zwracający współrzędne żywych komórek """
        for x in range(len(self.generacja)):
            kolumna = self.generacja[x]
            for y in range(len(kolumna)):
                if kolumna[y] == ALIVE:
                    # jeśli komórka jest żywa zwrócimy jej współrzędne
                    yield x, y

    def zwroc_sasiada(self, x, y):
        """ Generator zwracający sąsiadów komórki """
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue  # pomijamy badaną komórkę
                if i >= self.szer:  # czy nie wyszliśmy poza planszę?
                    i = 0
                elif i < 0:   # czy nie wyszliśmy poza planszę?
                    i = self.szer - 1
                if j >= self.wys:  # czy nie wyszliśmy poza planszę?
                    j = 0
                elif j < 0:  # czy nie wyszliśmy poza planszę?
                    j = self.wys - 1

                # zwracamy komórkę o ustalonych współrzędnych
                yield self.generacja[i][j]

    def wylicz_generacje(self):
        """ Wyliczamy następną generację populacji komórek """
        nowa_gen = self.utworz_generacje()
        for x in range(len(self.generacja)):
            kolumna = self.generacja[x]
            for y in range(len(kolumna)):
                # sumujemy żywych sąsiadów
                ileZywych = sum(self.zwroc_sasiada(x, y))
                if ileZywych == 3:
                    nowa_gen[x][y] = ALIVE  # komórka ożywa
                elif ileZywych == 2:
                    nowa_gen[x][y] = kolumna[y]  # komórka bez zmian
                else:
                    nowa_gen[x][y] = DEAD  # komórka ginie

        # nowa generacja zastępuje starą
        self.generacja = nowa_gen


if __name__ == "__main__":
    gra = LifeGra(80, 40)
    gra.uruchom()
