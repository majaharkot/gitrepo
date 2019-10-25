/*
 * szkielet.cpp
 *
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
        
    cout << "Podaj liczbę:  ";
    cin >> a;
        
    cout << "Podaj drugą liczbę:  ";
    cin >> b;
    
    cout << a << " " << b << endl;
    
    cout << endl << "Suma: " << a + b << endl;
    cout << "Różnica: " << a - b << endl;
    cout << "Iloczyn: " << a * b << endl;
    cout << "Iloraz: " << a / b << endl;
    
	return 0;
}

