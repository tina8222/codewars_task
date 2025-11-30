import sqlite3

conn = sqlite3.connect("movies.db")        
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS MOVIES (
    id INTEGER PRIMARY KEY,
    Name TEXT,
    Year INTEGER,
    Rating INTEGER
)
""")

cur.execute("INSERT INTO MOVIES (Name, Year, Rating) VALUES (?, ?, ?)",
            ("Rise of the planet of the apes", 2011, 77))


conn.commit()

conn.close()