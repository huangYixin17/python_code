# -*- coding: utf-8 -*-
"""
開啟檔案test.db
把內容加入檔案中
"""
import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor() #建立資料庫物件

print("Opened database successfully")
#這裡語法是insert into company
#把資料寫入到資料庫裡
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (1, 'Paul', 32, 'California', 20000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
 VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
conn.commit() #提交
print("Records created successfully")
conn.close()    #關閉














