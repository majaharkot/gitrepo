#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwadraty.py

import turtle

def rysujKwadrat(zolw, bok, ile):  # ile do wersji rekurencyjnej
    
    ### REKURENCJA 
    zolw.forward(bok)
    zolw.right(90)
    
    if ile > 0:
        rysujKwadrat(zolw, bok, ile-1)
    
    ### INTERACJA
    #for i in range(4):
    #    zolw.forward(bok)
    #    zolw.right(90)
    
    #zolw.forward(bok)
    #zolw.right(90)
    #zolw.forward(bok)
    #zolw.right(90)
    #zolw.forward(bok)
    #zolw.right(90)
    #zolw.forward(bok)
    #zolw.right(90)

def rysujKwadrat2(zolw, bok):
    
    for i in range(4):
        zolw.forward(bok)
        zolw.right(90)
        
    if bok > 0:
        rysujKwadrat2(zolw, bok - 10)

def rysuj(zolw, bok, kat, warunek):
    
    zolw.forward(bok)
    zolw.right(kat)
    
    if kat < warunek:
        rysuj(zolw, bok, kat, warunek)
    
def main(args):
    
    turtle.title("Kwadraciki")
    turtle.setup(1000, 800)
    
    zolw = turtle.Turtle()
    zolw.color('green', 'lime')
    zolw.pensize(2)
    zolw.speed(10)
    
    #rysujKwadrat(zolw, 100, 4)
    zolw.begin_fill()
    #rysujKwadrat2(zolw, 100)
    rysuj(zolw, 50, 60, 180)
    zolw.end_fill() 
    
    turtle.done()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
