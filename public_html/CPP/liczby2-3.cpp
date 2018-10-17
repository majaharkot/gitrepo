/*
 * liczby2-3.cpp
 */


#include <iostream>

using namespace std;

int liczby2()
{
    int ile = 0;  //deklaracja + inicjacja
    
    for (int d = 1; d < 10; d++)
    {
        for (int j = 0; j < 10; j++)
        {   
            if (d != j)
            {
                cout << d << j << " ";
                ile++;
            }
        }
    }
    
    return ile;
}

int liczby3()
{
    int ile = 0;  //deklaracja + inicjacja
    
    for (int s = 1; s < 10; s++)
    {
        for (int d = 0; d < 10; d++)
        {   
            for (int j = 0; j < 10; j++)
            {   
                if (s != d && s != j && d != j)
                {
                    cout << s << d << j << " ";
                    ile++;
                }
            }
        }
    }
    
    return ile;
}

int main(int argc, char **argv)
{
	int ile = liczby2();
    
    cout << "\n\nLiczb 2-cyfrowych: " <<  ile << endl;
    
    ile = liczby3();
    
    cout << "\n\nLiczb 3-cyfrowych: " <<  ile << endl;
    
	return 0;
}

