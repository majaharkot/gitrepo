DROP TABLE IF EXISTS tbZamowienia;
CREATE TABLE tbZamowienia (
	numer_zamowienia INTEGER PRIMARY KEY AUTOINCREMENT,
	id_klient INTEGER REFERENCES tbKlienci(id_klient) ON DELETE CASCADE,
	data_zamowienia DATE,
    wartosc_netto DECIMAL,
    vat
);

DROP TABLE IF EXISTS tbKlienci;
CREATE TABLE tbKlienci (
    id_klient INTEGER PRIMARY KEY AUTOINCREMENT,
	nazwa_klienta TEXT (60),
	adres TEXT (100),
	kod_pocztowy TEXT (10),
	miasto TEXT (40),
    wojewodztwo TEXT (30)
);

DROP TABLE IF EXISTS tbDetale_zamowienia;
CREATE TABLE tbDetale_zamowienia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	liczba_mieszkancow INTEGER,
	liczba_kobiet INTEGER,
	grupa_wiekowa TEXT (40),
    data_aktualizacji DATE,
    id_miasta INTEGER REFERENCES tbMiasta(id_miasta) ON DELETE CASCADE
);
