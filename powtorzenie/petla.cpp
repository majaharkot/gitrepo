/*
 * petla.cpp
 * 
 */


#include <iostream>
//#include <cstdlib>

using namespace std;

void wypelnij_losowe(int tab[], int roz)
{   
    srand(time(NULL));
    
    for (int i = 0; i < roz; i++)
    {
        tab[i] = rand() % 31;  
    }
}

void drukuj(int tab[], int roz)
{    
    for (int i = 0; i < roz; i++)
    {
        cout << tab[i] << ' ';
    }
}

int main(int argc, char **argv)
{
    int rozmiar = 5;
    int tablica[rozmiar];
    
	wypelnij_losowe(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    
	return 0;
}

