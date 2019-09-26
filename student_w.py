# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:59:39 2019

@author: user
"""
"""
輸入成績,存入cocres
與student_score並用

"""


import csv

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
        
    
