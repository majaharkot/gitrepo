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
    
        if (tekst[i] == ' ')
		{ 
			kod -= klucz;
		}
		else if(kod > 122)
		{
        kod -= 26;
		}
		tekst[i] = char(kod);
		cout << tekst[i];
		i++;
	}
}


int main(int argc, char **argv)
{    
    char tekst[MAKS];
    int klucz = 0;
    
    cout << "Wprowadź tekst do szyfrowania: ";
    cin.getline(tekst, MAKS);
    
    cout << "Podaj klucz: ";
    cin >> klucz;
    
    szyfruj(tekst,klucz);
	
	return 0;
}

