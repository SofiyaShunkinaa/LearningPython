import sqlite3

conn = sqlite3.connect('new.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS student 
(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date_of_birth DATE, faculty TEXT, 
course INTEGER, "group" INTEGER)''')
conn.commit()
user_data1 = (1, 'Sofi', '16.02.2024', 'IT', 3, 9 )
c.execute('INSERT INTO student VALUES (?,?,?,?,?,?)', user_data1)
user_data2 = (2, 'Alex', '17.02.2024', 'IT', 4, 4)
c.execute('INSERT INTO student VALUES (?,?,?,?,?,?)', user_data2)
conn.commit()
conn.close()