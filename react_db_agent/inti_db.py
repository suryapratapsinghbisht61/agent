import sqlite3
import os 
import sys


conn=sqlite3.connect("sDB/Sales.db")

cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Sales 
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT, price REAL, 
quantity INTEGER)
""")

cursor.execute("""
INSERT INTO Sales (name, price, quantity) VALUES
('Apple', 10, 5),
('Banana', 20, 10),
('Orange', 30, 15),
('Mango', 40, 20),
('Pineapple', 50, 25),
('Grapes', 60, 30),
('Watermelon', 70, 35),
('Strawberry', 80, 40),
('Blueberry', 90, 45),
('Raspberry', 100, 50)
""")

conn.commit()
conn.close()