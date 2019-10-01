# -*- coding: utf-8 -*-
"""
更改資料
"""
import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
print("Opened database successfully")
#.execute("UPDATE 是改變原本的資料")
c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit() #一定要提交
print("Total number of rows updated :", conn.total_changes) #把更改的行數print
cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
print("Operation done successfully")
conn.close()














