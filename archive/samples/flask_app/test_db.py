import sqlite3

conn = sqlite3.connect("data.db")

cursor = conn.cursor()

query_table_users = "CREATE TABLE users (id int, username text, password text)"
query_insert_users = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(query_table_users)

users = [
    (1, "rohit", "rohit"),
    (2, "rohan", "rohan"),
    (3, "vimla", "vimla"),
    (4, "ramesh", "ramesh")
]

cursor.executemany(query_insert_users, users)

conn.commit()
conn.close()