DROP TABLE IF EXISTS tbFilmy;
CREATE TABLE tbFilmy (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    genre TEXT DEFAULT '',
    year INTEGER,
    imdb_rating DECIMAL
  );

