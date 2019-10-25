DROP TABLE IF EXISTS kraje;
CREATE TABLE kraje (
    id_kraju INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa VARCHAR(30)
);

DROP TABLE IF EXISTS uzytkownicy;
CREATE TABLE uzytkownicy (
    id_uzytkownika INTEGER PRIMARY KEY AUTOINCREMENT,
    imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
    nazwisko VARCHAR(30) NOT NULL CHECK (nazwisko <> ''),
    id_kraju INTEGER,
    plec CHAR(1),
    FOREIGN KEY (id_kraju) REFERENCES kraje (id_kraju)
    ON DELETE CASCADE
);

DROP TABLE IF EXISTS znajomosci;
CREATE TABLE znajomosci (
    znajomy_1 INTEGER NOT NULL REFERENCES uzytkownicy (id_uzytkownika)
    ON DELETE CASCADE,
    znajomy_2 INTEGER NOT NULL REFERENCES uzytkownicy (id_uzytkownika)
    ON DELETE CASCADE,
    data DATE,
    PRIMARY KEY (znajomy_1,znajomy_2)
);

DROP TABLE IF EXISTS zdjecia;
CREATE TABLE zdjecia (
    id_zdjecia INTEGER PRIMARY KEY AUTOINCREMENT,
    data_dodania DATE NOT NULL,
    id_uzytkownika INTEGER,
    szerokosc INTEGER,
    wysokosc INTEGER,
    FOREIGN KEY (id_uzytkownika) REFERENCES uzytkownicy (id_uzytkownika)
    ON DELETE CASCADE
);
