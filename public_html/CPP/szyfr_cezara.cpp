/*
 * szyfr_cezara.cpp
 */


#include <iostream>
using namespace std;

#define MAKS 100

void szyfruj(char tekst[], int klucz)
{
    klucz = klucz % 26;
    
    int i = 0;
    int kod = 0;
    while(tekst[i] != '\0')
    {
        kod = (int)tekst[i] + klucz;
        cout  << (char)kod;
        i++;
    }
    
    

    
}


int main(int argc, char **argv)
{
    
    char tekst[100];
    int klucz = 0;
    
    cout << "Wprowadź tekst do szyfrowania: ";
    cin.getline(tekst, MAKS);
    
    cout << "Podaj klucz: ";
    cin >> klucz;
    
    szyfruj(tekst,klucz);
	
	return 0;
}

