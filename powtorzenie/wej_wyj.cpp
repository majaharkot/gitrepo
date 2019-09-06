/*
 * wej_wyj.cpp
 *
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    char imie[10], nazwisko[20];
        
    cout << "Jak masz na imię?     ";
    cin >> imie;
        
    cout << "Jak masz na nazwisko?     ";
    cin >> nazwisko;
    
    cout << "Witaj" << " " << imie << " " << nazwisko << "!" << endl;

	return 0;
}

