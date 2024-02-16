import sqlite3

conn = sqlite3.connect('new.db')
c = conn.cursor()
c.execute('''SELECT * FROM student''')
print(c.fetchall())
