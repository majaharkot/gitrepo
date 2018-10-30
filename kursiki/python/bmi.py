#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bmi.py
#  

def main(args):
    
    masa = float(input("Podaj swoją wagę w kilogramach: "))
    wzrost = int(input("Podaj swój wzrost w centymetrach: "))
    
    bmi = masa / ((wzrost/100)**2)
    print("BMI ={:.1f}".format(bmi))
    
    if bmi < 18.5:
        print("Niedowaga")
    elif bmi < 24.9:
        print("Norma")
    elif bmi < 30:
        print("Nadwaga")
    else:
        print("Otyłość")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
