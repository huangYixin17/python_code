# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:53:51 2019

@author: user
"""
"""
建立資料庫
寫入資料到資料庫(.db)
"""

import sqlite3  #import資料庫
conn = sqlite3.connect('student.db')
print("Opened database successfully")
c = conn.cursor() #建立資料庫物件
"""  這裡以下可以另外寫一個檔案.py , 這裡是創立資料庫的
c.execute('''CREATE TABLE student
  (NAME REAL,
  score_c   REAL,
  score_e   REAL,
  score_m   REAL);''')

conn.commit()  #提交
"""
def student_date():
    while(True):
        name1 = input("請輸入姓名: ")
        score_c = input("請輸入國文成績")
        score_e = input("請輸入英文成績")
        score_m = input("請輸入數學成績")
        c.execute("INSERT INTO student (NAME,score_c,score_e,score_m) \
         VALUES ('%s', %s, %s, %s )" % (name1,score_c,score_e,score_m));
                  
        conn.commit() #提交
        exit = input("離開(Y/N)")
        if(exit == "Y"):
            break

student_date()

cursor = c.execute("SELECT name, score_c, score_e, score_m  from student") 

for row in cursor:
   print("name = ", row[0])
   print("國文 = ", row[1])
   print("英文 = ", row[2])
   print("數學 = ", row[3], "\n")
print("Operation done successfully")
conn.close()        
          
          
