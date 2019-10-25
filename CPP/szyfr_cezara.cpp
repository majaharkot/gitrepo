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
        kod = (int)tekst[i];
    
        if (tekst[i] == ' ')
		{ 
			;
		}
		else if(kod < 91) 
        {
            kod += klucz;
            if(kod > 90) kod -= 26;
        }
        else
        {
            kod += klucz;
            if(kod > 122) kod -= 26;            
        }
        cout << (char)kod;
		tekst[i] = (char)kod;
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

