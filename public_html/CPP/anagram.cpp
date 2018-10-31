/*
 * anagram.cpp
 * 
 * Ala ma kota, a kot ma Alę!
 * alA am atok, a tok am ęlA!
 */
// wyrazy() 

#include <iostream>

using namespace std;

int zlicz(char tb[])
{
    int i = 0;
    
    while(tb[i] != '\0') i++;
    
    return i;
}

void wyswietl(char tekst[], int roz)
{
    for (int i = 0; i < roz; i++)
    {
        cout << tekst[i];
    }
}

void anagram(char tekst[], int roz)
{
    for (int i= roz - 1; i >= 0; i--)

    
}

int main(int argc, char **argv)
{
    const int rozmiar = 50;
    char tekst[rozmiar];
    
    cin.getline(tekst, rozmiar);
    
    wyswietl(tekst, zlicz(tekst));

    
	return 0;
}

