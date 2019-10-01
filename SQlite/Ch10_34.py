# -*- coding: utf-8 -*-
"""
刪除資料
"""
import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
print("Opened database successfully")
c.execute("DELETE from COMPANY where ID=2;")    #.execute("DELETE")以ID為標籤,刪除2
conn.commit() #提交
c.execute("DELETE from COMPANY where ID=3;")    #.execute("DELETE")以ID為標籤,刪除2
conn.commit()   #提交
print("Total number of rows deleted :", conn.total_changes) #把更改的行數print
cursor = conn.execute("SELECT id, name, address, salary  from COMPANY") #為了輸出
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
print("Operation done successfully")
conn.close()















