import sqlite3

conn = sqlite3.connect('new.db')
c = conn.cursor()
conn.commit()
# user_data1 = (3, 'Ann', '11.02.2024', 'IT', 2, 5 )
# c.execute('INSERT INTO student VALUES (?,?,?,?,?,?)', user_data1)
# user_data2 = (4, 'Mary', '05.02.2024', 'IT', 2, 5 )
# c.execute('INSERT INTO student VALUES (?,?,?,?,?,?)', user_data2)
# user_data3 = (5, 'Max', '02.02.2024', 'IT', 4, 1 )
# c.execute('INSERT INTO student VALUES (?,?,?,?,?,?)', user_data3)
# conn.commit()
c.execute('''SELECT * FROM student''')
print(c.fetchall())
date = '10.02.2024'
course = 2
group = 5
c.execute('DELETE FROM student WHERE date_of_birth < ? '
          'OR course = ? AND "group" = ?', (date, course, group))
conn.commit()
c.execute('''SELECT * FROM student''')
print(c.fetchall())
