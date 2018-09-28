DROP TABLE IF EXISTS tbUczniowie;
CREATE TABLE tbUczniowie (
	numer_ucznia INTEGER PRIMARY KEY,
	nazwisko TEXT (50) NOT NULL,
	pierwsze_imie TEXT (50) NOT NULL,
    drugie_imie TEXT (50)
);

DROP TABLE IF EXISTS tbDane_os;
CREATE TABLE tbDane_os (
	numer_ucznia REFERENCES tbUczniowie(numer_ucznia),
	dzien_urodzenia INTEGER,
	miesiac_urodzenia INTEGER,
    rok_urodzenia INTEGER,
    miejsce_urodzenia TEXT (50),
    wojewodztwo_urodzenia TEXT (50)
);

DROP TABLE IF EXISTS tbOceny;
CREATE TABLE tbOceny (
	numer_ucznia REFERENCES tbUczniowie(numer_ucznia,
	zachowanie INTEGER,
	religia_etyka INTEGER,
    jpolski INTEGER,
    jangielski INTEGER,
    jniemiecki INTEGER,
    matematyka INTEGER,
    historia INTEGER,
    geografia INTEGER,
    biologia INTEGER,
    fizyka INTEGER,
    chemia INTEGER,
    technika INTEGER,
    informatyka INTEGER,
    plastyka INTEGER,
    po INTEGER,
    wf TEXT (3)
);
