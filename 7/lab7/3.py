import sqlite3

conn = sqlite3.connect('new.db')
c = conn.cursor()
new_group = 5
student_name = "Alex"
c.execute('UPDATE student SET "group" = ? WHERE name = ?', (new_group, student_name))
conn.commit()
c.execute('''SELECT * FROM student''')
print(c.fetchall())
