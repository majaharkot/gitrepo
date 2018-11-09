DROP TABLE IF EXISTS tbOceny;
CREATE TABLE tbOceny (
    IDucznia INTEGER PRIMARY KEY,
    Ocena INTEGER,
	Data DATE,
    IDprzedmiotu INTEGER,
    FOREIGN KEY (IDprzedmiotu) REFERENCES tbPrzedmioty(IDprzedmiotu)
);

DROP TABLE IF EXISTS tbUczniowie;
CREATE TABLE tbUczniowie (
	IDucznia INTEGER,
	nazwisko TEXT (50) NOT NULL,
	imie TEXT (50) NOT NULL,
    ulica TEXT (50),
    dom INTEGER,
    IDklasy TEXT,
    FOREIGN KEY (IDucznia) REFERENCES tbUczniowie(IDucznia)
);

DROP TABLE IF EXISTS tbPrzedmioty;
CREATE TABLE tbPrzedmioty (
	IDprzedmiotu INTEGER PRIMARY KEY,
	NazwaPrzedmiotu TEXT (50) NOT NULL,
	Nazwisko_naucz TEXT (50) NOT NULL,
	Imie_naucz TEXT (50) NOT NULL
);


