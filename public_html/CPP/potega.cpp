/*
 * potega.cpp
 */


#include <iostream>

using namespace std;

float potega_re(float x, int n)
{
    if (n == 0) return 1;   // x^0 = 1 dla x <> 0
    return potega_re(x, n-1) * x;  //x^n = x(n-1)*x dla n = N+
    
    
}

int main(int argc, char **argv)
{
	float podstawa;
    int wykladnik;
    
    cout << "Podstawa potęgi: "; cin >> podstawa;
    cout << "Wykładnik potęgi: "; cin >> wykladnik;
    cout << "Wynik: " << potega_re(podstawa, wykladnik); 
        
	return 0;
}

