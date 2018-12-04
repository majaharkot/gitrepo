/*
 * Harkot_l.pierwsza.roz.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int n;
    
    cout << "Podaj liczbę: ";
    cin >> n;
    
    for(int i=2; i*i <= n; i++)
    {
        if(n % i == 0)
        {
            cout << "Jest to liczba złożona." << endl;
            break;
        }
        else
            cout << "Jest to liczba pierwsza." << endl;
    };
}

