import sqlite3

conn=sqlite3.connect("sDB/Sales.db")

cursor=conn.cursor()

cursor.execute('''SELECT * FROM Sales''')
rows=cursor.fetchall()
for row in rows:
    print(row)

conn.close()

