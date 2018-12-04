/*
 * fibbonacci.cpp
 */

#include <iostream>

using namespace std;

int fibonacci_it(int n)   //wersja iteracyjna
{
    int a = 0;  //wyraz pierwszy (n-2)
    int b = 1;  //wyraz drugi (n-1)
    
    if (n < 1) return a;
    else if (n < 2) return b;
    
    int wynik = 0;
    
    for (int i = 2; i <= n; i++)
    {
        wynik = a + b;
        a = b;
        b = wynik;
    } 
    return wynik;
}

int fibonacci_rek(int n)   // wersja rekurencyjna
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci_rek(n - 2) + fibonacci_rek(n - 1);
    
}


int main(int argc, char **argv)
{
    int n;
    
    cout << "Podaj numer wyrazu ciągu: ";
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu " << n << ":" << endl;
        
    //cout << "1.Iteracyjnie: " << fibonacci_it(n) << endl;
    //cout << "2.Rekurencyjnie: " << fibonacci_rek(n) << endl;
    
    
    for (int i = 0; i <= n; i++) 
    {
        cout << fibonacci_rek(i) << " ";
        
        if(i < 2) continue;
        else
        {
            cout << (float)fibonacci_rek(i) / (float)fibonacci_rek(i-1) << endl;
        }
    }
	
	return 0;
}

