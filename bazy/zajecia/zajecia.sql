DROP TABLE IF EXISTS osoby;
CREATE TABLE osoby (
    id_osoby INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwisko VARCHAR(30) NOT NULL CHECK (nazwisko <> ''),
    imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
    plec CHAR(1)
);

DROP TABLE IF EXISTS obiekty;
CREATE TABLE obiekty (
    id_obiektu INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa VARCHAR(30)
);

DROP TABLE IF EXISTS zajecia;
CREATE TABLE zajecia (
    id_zajec INTEGER PRIMARY KEY AUTOINCREMENT,
    id_obiektu INTEGER,
    zajecia VARCHAR(30),
    cena DECIMAL(2),
    FOREIGN KEY (id_obiektu) REFERENCES obiektu (id_obiektu)
);

DROP TABLE IF EXISTS wejscia;
CREATE TABLE wejscia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_osoby INTEGER,
    data DATE NOT NULL,
    id_zajec INTEGER,
    FOREIGN KEY (id_osoby) REFERENCES osoby (id_osoby)
    ON DELETE CASCADE,
    FOREIGN KEY (id_zajec) REFERENCES zajecia (id_zajec)
    ON DELETE CASCADE
);
