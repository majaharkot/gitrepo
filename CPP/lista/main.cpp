/*
 * main.cpp
 */

#include <iostream>
#include "lista.h"

using namespace std;

int main(int argc, char **argv)
{
    Lista lista;
    lista.Dodaj(1);
    lista.Dodaj(2);
    lista.Dodaj(3);
    lista.Dodaj(4);
    cout << lista.Usun() << endl;
    cout << lista.Usun() << endl;
    lista.Wyswietl();

    return 0;
}

