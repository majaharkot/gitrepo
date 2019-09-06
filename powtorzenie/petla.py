#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla.py
#  

import random

def main(args):
	
	lista = []
    
	for i in range(5):
		liczba = random.randint(1, 31)
		if lista.count(liczba) == 0:
			lista.append(liczba)
		
	print(lista)
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
