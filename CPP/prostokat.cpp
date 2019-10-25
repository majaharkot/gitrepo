/*
 * prostokat.cpp
 * 
 * ZADANIE: napisz program, który liczy pole i obwód prostokąta
 * DANE WEJŚCIOWE: liczby całkowite podawane przez użytkownika
 * WYJŚCIE: komkomunikat w terminalu o obliczonym obwodzie i polu
 */


#include <iostream>

using namespace std;

int obwod(int a, int b)
{
    return 2 * a + 2 * b;
}

int pole(int a, int b)
{
    return a * b;
}

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    
    cout << "Podaj długość boku a: ";
    cin >> a;
        
    cout << "Podaj długość boku b: ";
    cin >> b;
    
    cout << a << " " << b << endl;
    
    cout << endl << "Obwód: " << obwod(a, b) << endl;
    cout << "Pole: " << pole(a, b) << endl;
    
	return 0;
}

