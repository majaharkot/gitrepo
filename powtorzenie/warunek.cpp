/*
 * warunek.cpp
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a, b, c;
    a = b = c = 0;
    
    cout << "Podaj 1. liczbę  ";
    cin >> a;
    cout << "Podaj 2. liczbę  ";
    cin >> b;
    cout << "Podaj 3. liczbę  ";
    cin >> c;
    
    if (a>b and a>c) cout << "Największą liczbą jest " << a << endl;
    if (b>a and b>c) cout << "Największą liczbą jest " << b << endl;
    else cout << "Największą liczbą jest " << c << endl;
	
	return 0;
}

