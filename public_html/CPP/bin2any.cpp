/*
 * bin2any.cpp
 */


#include <iostream>

using namespace std;

void dectoany (int liczba, int podstawa, int tab[])
 {
        int i = 0;
    do {
       tab[i] = liczba % podstawa;
       liczba = liczba / podstawa;
       i++; 
    }while ( liczba != 0);
    return i-1;
}


void bin_licz(int tab[]) 
{
    int wynik = 0;
    int potega = 1;
    for (int x = 0; x <= 8; x++) {
        potega = potega * 2;
        if (x == 0) potega = 1;
        wynik = wynik + (potega * tab[x]);
    }
    cout <<"\nWynik: " << wynik << endl;
}


void wyswietl(int tab[], int roz) 
{
    for(int i = 0; i < roz; i++) 
    {
        cout<< tab[i] << " ";
    }
    cout << endl;
}


void wyswietl_poprawnie(int tab[], int roz) 
{
    cout << "Poprawny zapis binarny: " << endl;
    for(int i = roz - 1; i >= 0; i--) 
    {
        cout<< tab[i] << " ";
    }
}


int main(int argc, char **argv)
{
    int a = 0;
    int rozmiar = 8;
    int tab[rozmiar];
    cout << "Podaj liczbę: ";
    cin >> a;
    wyswietl(tab, rozmiar);
    wyswietl_poprawnie(tab, rozmiar);
    bin_licz(tab);
    return 0;
}
