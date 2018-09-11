/*
 * szkielet.cpp
 * 
 * "\n" - new line - przejście do nowej lini
 * endl - end of line /
 * " " - wyświetl spacje
 */

#include <iostream>

using namespace std; // zamiast std::

int main(int argc, char **argv)
{
	int liczba; // deklaracja zmiennej liczba typu całkowitego (integer)
    liczba = 12;
   // std::cout << liczba; // w pythonie print(liczba)
    cout << liczba;
   
    int a, b, c, d; // deklaracja zmiennych
    a = b = c = 0; //inicjalizacja zmiennych MUY IMPORTANTE
    a = 12; // przypisanie
    b = 2 * a; //mnożenie
    c = b + a; //dodawanie
    d = a / b; //dzielenie
    
    cout << "\n" << a << " " << b << "" << (b - a);
    cout << " " << d;
    
	return 0;
}

