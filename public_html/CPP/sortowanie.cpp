/*
 * sortowanie.cpp
 */


#include <iostream>

using namespace std;

void wypelnij_losowe(int tab[], int roz)
{   
    srand(time(NULL));  // inicjacja generatora pseudolosowych
    
    for (int i = 0; i < roz; i++)
    {
        tab[i] = rand() % 101;  
    }
}

void drukuj(int tab[], int roz)
{    
    for (int i = 0; i < roz; i++)
    {
        cout << tab[i] << ' ';
    }
}

void zamien(int a, int b)
{
    
    
}

void sort_bubble(int tab[], int n)
{
    cout << "\nSortowanie bąbelkowe:\n"
    
    for(int j = n-1; j > 0 ; j--)
    {
        for(int i = 0, i < j; i++)
        {
            if(tab[i]>tab[i+1])
                zamien(tab[i], tab[i+1])
        }
    }   
    
}

int main(int argc, char **argv)
{
    int rozmiar = 20;
    int tablica[rozmiar]; //statyczna deklaracja tablicy
    
    wypelnij_losowe(tablica, rozmiar);
    drukuj(tablica, rozmiar);
        
	return 0;
}

