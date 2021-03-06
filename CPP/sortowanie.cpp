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


void zamien(int &a, int &b)
{
    int tmp; //zmienna pomocnicza
    tmp = a;
    a = b;
    b = tmp;
}

void zamien2(int tab[], int i)
{
    int tmp = tab[i];
    tab[i] = tab[i+1];
    tab[i+1] = tmp;
}

void bubble_sort(int tab[],int n)
{
    cout << "\nSortowanie bąbelkowe\n";
    
    int licznik = 0;
    
    for(int j = n - 1; j > 0; j--)
    {
        for(int i = 0; i <  j; i++) //pętla wewnętrzna
        {
            if(tab[i] > tab[i+1])
            {
                //zamiana miejscami
                zamien2(tab, i);
            }
            licznik++;
        }
    }
    cout << "Powtórzenia: " << licznik << endl;
}

void insert_sort(int tab[], int n)
{
    cout << "\nSortowanie przez wstawianie:\n";

    int i, j, tmp;
     
    for(i = 1; i < n; i++)
    {
        tmp = tab[i];
        j = i - 1;
        while (j >= 0 && tab[j] > tmp)
        {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
}

void select_sort(int tab[], int n)
{
    cout << "\nSortowanie przez wybór:\n";
    
    int licznik = 0;
    
    int k;
    for(int i = 0; i < n; i++)
    {
        k = i;
        for(int j = i + 1; j <n; j++)
        {
            if(tab[j]<tab[k])
            {
                k = j;
                zamien2(tab, j);
            }
           licznik++; 
        }
    }
    cout << "Powtórzenia: " << licznik << endl;
}

int main(int argc, char **argv)
{
    int rozmiar = 10;
    int tablica[rozmiar]; //statyczna deklaracja tablicy
    
    wypelnij_losowe(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    cout << endl;
    bubble_sort(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    insert_sort(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    select_sort(tablica, rozmiar);
    drukuj(tablica, rozmiar);
        
	return 0;
}

