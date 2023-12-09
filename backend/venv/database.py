import sqlite3

connection = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
               id INTGET PRIMARY KEY AUTOINCREMENT, 
               username VARCHAR(255) NOT NULL, 
               password VARCHAR(255) NOT NULL
)''')

connection.commit()
connection.close()