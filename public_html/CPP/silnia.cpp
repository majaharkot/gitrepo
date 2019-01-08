/*
 * silnia.cpp
 */


#include <iostream>

using namespace std;

int silnia_re(int n)
{
    if (n == 0) return 1;  // 0! = 1
    return silnia_re(n-1) * n;  // n! = (n-1)! * n
}

int silnia_it(int n)
{
    int silnia = 1;
    int i;
    
    for(i = 1; i <= n; i++)
        silnia = silnia * i;
    return silnia;
    
}

int main(int argc, char **argv)
{
    int n;
    
    cout << "Podaj liczbę: "; cin >> n;
    cout << "Wynik: " << silnia_it(n); 
        
	return 0;
}

