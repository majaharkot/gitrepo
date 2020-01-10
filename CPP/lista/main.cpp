/*
 * main.cpp
 */

#include <iostream>
#include "lista.h"

int main(int argc, char **argv)
{
    Lista lista;
    lista.Dodaj(1);
    lista.Dodaj(2);
    lista.Dodaj(3);
    lista.Dodaj(4);
    lista.Wyswietl();

    return 0;
}

