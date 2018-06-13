DROP TABLE IF EXISTS tbApps;
CREATE TABLE tbApps (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT DEFAULT '',
    downloads INTEGER,
    price DECIMAL DEFAULT NULL
  );
