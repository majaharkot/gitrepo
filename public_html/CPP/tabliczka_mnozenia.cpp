/*
 * tabliczka_mnozenia.cpp
 * 
 */


#include <iostream>
#include <iomanip>

using namespace std;

void tabliczka(int a, int b)
{
    
    //int kolumna, wiersz;
    
    for (int i = 1; i <= a; i++)
    {
        for (int j = 1; j <= b; j++)
        {   
            cout << setw(4) << i * j;
        }
        
        cout << endl;
    }
}

int main(int argc, char **argv)
{   
    int a, b;  //deklaracja
    a = b = 0;  //inicjacja
    
    cout << "Podaj zakres liczb w kolumnie: ";
    cin >> a;
        
    cout << "Podaj zakres liczb w wierszu: ";
    cin >> b;
    
    tabliczka(a, b);
    	
	return 0;
}

