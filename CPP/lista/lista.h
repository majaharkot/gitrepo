typedef struct ELEMENT{

    int value;
    ELEMENT *next;      //*coś <-- wskaźnik
    
}ELEMENT;

typedef struct HEADER{

    ELEMENT *head;
    ELEMENT *tail;

}HEADER;

class Lista{

    private:        //hermetyzacja danych
        HEADER header;      //blok INFO

    public:
        Lista();        //konstruktor
        ~Lista();       //destruktor
        void Dodaj(int);
        bool Wstaw(int, int);
        int Usun();
        bool Usun(int);     //przeciążanie metod
        void Wyswietl();
        bool Pusta();
};
