DROP TABLE IF EXISTS tbMiasta;
CREATE TABLE tbMiasta (
	id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
	nazwa_miasta TEXT (30),
	wojewodztwo TEXT (30)
);

DROP TABLE IF EXISTS tbPowierzchnie;
CREATE TABLE tbPowierzchnie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	powierzchnia_miasta DECIMAL,
	powierzchnia_terenów_zielonych DECIMAL,
	data_aktualizacji DATE,
	id_miasta INTEGER REFERENCES tbMiasta(id_miasta) ON DELETE CASCADE
);

DROP TABLE IF EXISTS tbDane_gus;
CREATE TABLE tbDane_gus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	liczba_mieszkancow INTEGER,
	liczba_kobiet INTEGER,
	grupa_wiekowa TEXT (40),
    data_aktualizacji DATE,
    id_miasta INTEGER REFERENCES tbMiasta(id_miasta) ON DELETE CASCADE
);
