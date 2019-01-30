/*
 * dec2bin.cpp
 * 
 * Program zamienia liczbę dziesiętną podaną przez użytkownika na binarną
 */


#include <iostream>
using namespace std;

int dec2bin(int l)
{
    int lbin = 0;
    int i = 1;
    
    while (l > 0)
    {
        lbin += (l%2)*i;
        l = l/2;
        i *= 10;
    }
    return lbin;
}

int dectobin(int l)
{
    int i = 0;
    int tab[8];
    
    while (l
}

int main(int argc, char **argv)
{
    int l = 0;
	cout << "Podaj dowolną liczbę dziesiętną: ";
    cin >> l;
    
    cout << "liczba binarna: " << dec2bin(l) << endl;
	return 0;
}

