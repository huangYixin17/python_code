# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:20:51 2019
project:按照成績排名次
@author: user
"""



num=[1,3,5,2,8]
rank=num
rank_l=[1,3,5,2,8]
rank_ll=[1,3,5,2,8]
for b in range(0,len(num)):  
    for a in range(0,len(num)):
        if((a+1)>=len(num)):
            break
        if((num[a])<(num[a+1])):          
            change=rank[a]         
            rank[a]=rank[a+1]         
            rank[a+1]=change          
print(num)
print(rank)
print(rank_l)

num=rank_l           
print(num)
for c in range(0,len(num)):
    for d in range(0,len(num)):
        num=rank_ll
        if( (rank[c]) == (num[d]) ):
            print("rank[c]= " ,c,"  ",rank[c] ,"   ","rank[d]= ", d,"   ",(num[d]))
            rank_l[d]=c+1
            print("rank_l[d]= ",rank_l,"\n")
print(rank_l)

