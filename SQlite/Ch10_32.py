# -*- coding: utf-8 -*-
"""
開啟檔案test.db

"""
import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor() #建立資料庫物件
print("Opened database successfully")
#把c的物件全部存入curcor 此時的c跟curcor是一樣的變數
cursor = c.execute("SELECT id, name, address, salary  from COMPANY") 

for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")
print("Operation done successfully")
conn.close()













