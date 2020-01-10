/*
 * lista.cpp
 */


#include <iostream>
#include "lista.h"

using namespace std;

Lista::Lista() {

    header.head = NULL;
    header.tail = NULL;

}

Lista::~Lista() {

    while(header.head != NULL)
        Usun();

}

void Lista::Dodaj(int value) {

    ELEMENT *el = new ELEMENT;
    el -> value = value;
    el -> next = NULL;

    if (header.head == NULL) {
        head = el;
        tail = el;
    } else {
        header.tail -> next = el;  //łączenie elementów listy
        header.tail = el;
    }

}

void Lista::Wyswietl() {

    ELEMENT *el = header.head;
    
    while (el != NULL) {
        cout << el -> value << endl;
        el = el -> next;
    }
    cout << endl;
}


