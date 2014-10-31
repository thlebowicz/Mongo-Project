import sqlite3

conn = sqlite3.connect("itsudemo.db")
curs = conn.cursor()
query = "CREATE TABLE accounts(username text, password text)"
result = curs.execute(query)
conn.commit();
conn.close();
