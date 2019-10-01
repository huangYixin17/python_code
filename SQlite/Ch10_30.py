# -*- coding: utf-8 -*-
"""
開啟資料夾,如原本沒有檔案的話,會新建一個資料庫檔(.db)

"""
import sqlite3  #import資料庫
conn = sqlite3.connect('test.db')   #開啟資料庫
print("Opened database successfully") 
c = conn.cursor()   #建立資料庫物件
#執行資料庫語法
#如果已經創立過company就不能再創立,程式會發生錯誤
#.execute內是指創立一個名稱為 :company
#內容有id,name,age,address,salary
c.execute('''CREATE TABLE COMPANY
  (ID INT PRIMARY KEY NOT NULL,
  NAME TEXT    NOT NULL,
  AGE  INT NOT NULL,
  ADDRESS   CHAR(50),
  SALARY    REAL);''')
print("Table created successfully")
conn.commit()  #提交
conn.close()    #關閉












