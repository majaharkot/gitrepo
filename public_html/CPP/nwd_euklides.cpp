/*
 * nwd_euklides.cpp
 */


#include <iostream>

using namespace std;

int nwd_optymalny(int a, int b)
{   
    int licznik = 0;
    
    while (a > 0) 
    {
        a = a % b;
        b = b - a;
        licznik++;
    }
    
    cout << "Liczba powtórzeń: " << licznik << endl;
    
    return b;
}

int nwd_klasyczny(int a, int b)
{
    int licznik = 0;
    
    while(a!=b)
	{
		if (a > b)
        {
			a = a - b;
            licznik++;
		}
        else
        {
			b = b - a;
            licznik++;
        }
    }
    
    cout << "Liczba powtórzeń: " << licznik << endl;
    
    return a;
}

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    
    cout << "Podaj liczbę: ";
    cin >> a;
            
    cout << "Podaj drugą liczbę: ";
    cin >> b;

    cout << nwd_klasyczny(a, b) << endl;
    cout << nwd_optymalny(a, b);

	return 0;
}

