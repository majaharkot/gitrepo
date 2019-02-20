/*
 * szyfr_przestawieniowy.cpp
 */


#include <iostream>
#include <string.h>
using namespace std;

#define MAKS 100

int szyfruj(char tekst[], int klucz)
{
    int ile = strlen(tekst);
    int reszta = ile % klucz;
    int szyfr = 0;
    
    if(reszta > 0)
    {
       for
       
       tekst[i]
    }
    
    for (int i = 0; i < klucz; i++)
    {
        for (int j = 0; j < ile/klucz; j++)
        {
            szyfr +=  tekst[i+klucz];
        };
    }
    return szyfr;
}


int main(int argc, char **argv)
{    
    char tekst[MAKS];
    int klucz = 0;
    
    cout << "Wprowadź tekst do szyfrowania: ";
    cin.getline(tekst, MAKS);
    
    cout << "Podaj klucz: ";
    cin >> klucz;
    
    cout << szyfruj(tekst,klucz);
	
	return 0;
}

