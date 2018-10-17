/*
 * figury.cpp
 */


#include <iostream>

using namespace std;

//void prostokat(int a, int b, char znak)
// można zainicjować inne znaki niz w main ze względu na osobną funkcję
void prostokat(int x, int y, char z) 
{
    for (int i = 0; i < x; i++){
        for (int j = 0; j < y; j++)
            if (j == 0 || j == y-1 || i == 0 || i == x-1)
                cout << z;
            else
                cout << " ";
        cout << endl;
    }
}

int main(int argc, char **argv)
{
	int a, b;  //deklaracja
    a = b = 0;  //inicjacja
    
    cout << "Podaj długość boku a: ";
    cin >> a;
        
    cout << "Podaj długość boku b: ";
    cin >> b;
    
    char znak;
    
    cout << "Podaj znak, którym chcesz rysować: ";
    cin >> znak;
    
    prostokat(a, b, znak);
    
    /* 
     * cout << "Podaj długości boków prostokąta: ";
     * cin >> a >> b
     */
    
	return 0;
}

