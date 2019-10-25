/*
 * szkielet.cpp
 *
 * void - funkcja nie zwracająca wartości
 */

#include <iostream>

using namespace std;

int suma(int a, int b)
{
    return a + b;
}

int roznica(int a, int b)
{
    return a - b;
}

int iloczyn(int a, int b)
{
    return a * b;
}

int iloraz(int a, int b)
{
    return a / b;
}

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
        
    cout << "Podaj liczbę:  ";
    cin >> a;
        
    cout << "Podaj drugą liczbę:  ";
    cin >> b;
    
    cout << a << " " << b << endl;
    
    cout << endl << "Suma: " << suma(a, b) << endl;
    cout << "Różnica: " << roznica(a, b) << endl;
    cout << "Iloczyn: " << iloczyn(a, b) << endl;
    cout << "Iloraz: " << iloraz(a, b) << endl;
    
	return 0;
}

