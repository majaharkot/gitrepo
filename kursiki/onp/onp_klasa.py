#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  onp_klasa.py

from stos_obj import Stos


class ONPKlasa(Stos):
    
    def __init__(self, onp_str='', a_str=''):  # przesłonienie konstruktora rodzica
        super().__init__(10)  # wywołanie konstruktora rodzica
        if not self.czy_poprawne(onp_str):
            print("Błąd wyrażenia!")
            onp_str = ''
        self.onp_str = onp_str
        self.a_str = a_str
        self.log = []
        self.wynik = None
        
    def czy_poprawne(self, onp):
        for z in onp:
            if z.isalpha():
                return False
        return True

    def oblicz_onp(self):
        onp = self.onp_str.strip().split(" ")
    
        for el in onp:
           if el.isdigit():
               self.push(el)
           else:
               a = self.pop()
               b = self.pop()
               self.log.append(str(b) + el + str(a))
               self.push(eval(str(b) + el + str(a)))
        
        self.wynik = self.pop()

    def p(self, operator):
        if operator == '(':
            return 0
        if operator == '+' or operator == '-':
            return 1
        if operator == '*' or operator == '/':
            return 2
        if operator == '**':
            return 3

    def a2onp(self):
        operatory = set(['+', '-', '*', '/', '**'])
        for znak in self.a_str:
            print("Badany znak:", znak)
            if znak == " ":
                continue
            elif znak == '(':
                self.push(znak)
            elif znak == ')':
                while self.peek() != '(':
                    self.onp_str += self.pop() + ' '
                self.pop()  # usunięcie nawaisu otwierającego ze stosu
            elif znak in operatory:
                while not self.isEmpty():
                    if self.p(znak) == 3 or self.p(znak) > self.p(self.peek()):
                        break
                    self.onp_str += self.pop()
                self.push(znak)
            else:
                self.onp_str += znak + ' '
        while self.peek():
            self.onp_str += self.pop() + ' '
        self.onp_str.strip()

def main(args):
    #onp = input("Podaj wyr. ONP, oddzielając operandy i operatory spacjami:\n")
    #o1 = ONPKlasa(onp)
    #o1.oblicz_onp()
    
    o2 = ONPKlasa(a_str='(4 + 5) * 6')
    o2.a2onp()
    print(o2.onp_str)
    o2.oblicz_onp()
    print("Obliczenia: ", o2.log)
    print("Wynik: ", o2.wynik)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
