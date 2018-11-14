/*
 * horner.cpp
 * 
 * w(x) = 2x^3 + 3x^2 + 5x +4 => 6 mnożeń i 3 dodawania
 * w(x) = x (2x^2  + 3x + 5) + 4
 * w(x) = x (x (2x + 3) + 5) + 4 => 3 mnożenia i 3 dodawania 
 */

#include <iostream>

using namespace std;

void drukujw(int stopien, float tbwsp[])
{
    cout << tbwsp[i] << "x" << "^" << stopien    
}

int main(int argc, char **argv)
{
    float x = 0;
    
    int stopien = 0;
    cout << "Podaj stopień wielomianu: ";
    cin >> stopien;
    
    float *tbwsp; //wskaźnik to zmienna, która przechowuje adres komórki w pamięci
    tbwsp = new float [stopien + 1]; //alokacja tablicy dynamicznej
    
    //typ wskaźnika i typ tablicy muszą być takie same
    
    for (int i = 0; i <= stopien; i++)
    {
        cout << "Podaj współczynnik przy potędze " 
             << stopien - i << ": ";
        cin >> tbwsp[i];
    }
    
    cout << "Podaj argument x: ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci ";
    drukujw(stopien, tbwsp);
    cout << "\ndla x = " << x << " wynosi: ";
    cout << endl;
    
	return 0;
}

