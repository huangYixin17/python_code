# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:22:19 2019

@author: user
"""

import csv

#檔案寫入
def data_w():
    data = []
    with open('socres.csv','w',encoding = 'utf-8') as file:
        w = csv.writer(file)
        while(True):
            name = input("請輸入姓名(輸入完成請離開(E)): ")
            if(name == 'E'):
                break
            c = input("請輸入國文成績: ")
            e = input("請輸入英文成績: ")
            m = input("請輸入數學成績: ")
            data.append([name,c,e,m])
    
        w.writerows(data)
  
#檔案讀出      
def data_r():
    file = open('socres.csv' , newline='', encoding = 'utf-8')
    
    f = csv.reader(file)
    data = []
    
    for row in f:
        while(row != []):
            data.append([row[0],int(row[1]),int(row[2]),int(row[3])])
            break
        
    print("學生姓名  國文  英文  數學  平均")
    print("-----------------------------")
    for i in range(len(data)):
        print("%s %6d %4d %4d %4d" % ( data[i][0] , data[i][1] , data[i][2] , data[i][3] , (data[i][1]+data[i][2]+data[i][3])/3 ))
    
    c = 0 
    e = 0 
    m = 0
    for i in range(0,len(data)):
        c = c+data[i][1]
        e = e+data[i][2]
        m = m+data[i][3]
    print("-----------------------------")
    print("平均 %8d %4d %4d %4d" % (c/len(data),e/len(data),m/len(data),(c+e+m)/(3*len(data))))
        
    file.close()
    
#選擇檔案存取或讀出
choose = int(input("1.檔案寫入 2.檔案存取"))
while(True):
    if(choose == 1):
        data_w()
        break
    elif(choose == 2):
        data_r()
        break
    else:
        choose = int(input("請選擇: 1.檔案寫入 2.檔案存取"))