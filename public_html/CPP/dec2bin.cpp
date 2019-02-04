/*
 * dec2bin.cpp
 * 
 * Program zamienia liczbę dziesiętną podaną przez użytkownika na binarną
 */


#include <iostream>
using namespace std;

int dec2bin(int ld)
{
    int lbin = 0;
    int i = 1;
    
    while (ld > 0)
    {
        lbin += (ld%2)*i;
        ld /= 2;
        i *= 10;
    }
    return lbin;
}

void dectobin(int ld)
{
    int i = 0;
    int tab[8];

	while(ld > 0)
	{
		tab[i++]=ld%2;
		ld/=2;
	}

	for(int j=i-1;j>=0;j--)
		cout<<tab[j];
}

int bin2dec(int lb)
{ 
    int ldec = 0;
    int i = 1; 
    
    while (lb > 0) 
    {
        ldec += (lb%10)*i; 
        i = i*2; 
        lb /= 10;
    } 
    return ldec; 
} 

int main(int argc, char **argv)
{
    int ld = 0;
	cout << "Podaj dowolną liczbę dziesiętną: ";
    cin >> ld;
    
    int lb = 0;
	cout << "Podaj dowolną liczbę binarną: ";
    cin >> lb;
        
    cout << ld << " w systemie binarnym (dec2bin): " << dec2bin(ld) << endl;
    cout << ld << " w systemie binarnym (dectobin): ";
	dectobin(ld);
	cout << endl;
	cout << lb << " w systemie dziesiątkowym (bin2dec): " << dec2bin(lb) << endl; 
	return 0;
}

