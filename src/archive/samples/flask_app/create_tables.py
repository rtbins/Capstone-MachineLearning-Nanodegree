import sqlite3

conn = sqlite3.Connection("data.db")

cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name TEXT, price REAL)"

cursor.execute(query)

conn.commit()

conn.close()