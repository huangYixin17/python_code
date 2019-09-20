# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:38:11 2019

project:輸入學生姓名，成績，並幫他們排名次，以及輸出格式整齊，程式要加註解

@author: 黃羿欣
"""


def Avg(chin,eng,math):   #計算學生平均成績
    sum=chin+eng+math   #將學生的各科成績加總
    avg=float(sum/3)    #總成績除(/)3
    return avg          #回傳平均值



def rank(q):        #按成績排名次,q=平均值(avg)
    num=avg_l       
    rank=num
    rank_l=q        #這行是為了把num導回avg,因為到後面num會在城市進行中,被改為名次
            
    for b in range(0,len(num)):       #將平均值依大到小排列
        for a in range(0,len(num)):
            if((a+1)>=len(num)):
                break
            if((num[a])<(num[a+1])):          
                change=rank[a]         
                rank[a]=rank[a+1]         
                rank[a+1]=change     
                
    num=rank_l         #將num設定為平均值
    
    for c in range(0,len(num)):         #每個人的成績,算出他的排名
        for d in range(0,len(num)):
            num=q
            if( (rank[c]) == (num[d]) ):
                rank_l[d]=c+1
                break
    return rank_l
     
            
        
  

students=[] #每個學生名字的陣列
eng_l=[]    #學生英文成績
math_l=[]   #學生數學成績
chinese_l=[]    #學生國文成績
avg_l=[]    #平均成績
avg_n=[]    #拿去給函式計算的平均值
avg_p=[]    #最後輸出的平均成績
rank_l=[]  #名次的陣列
while(True): #輸入學生姓名及成績

    name=input("請輸入姓名: ")  #輸入學生姓名
    if( name =="exit"):   
        break        #如果輸入完成,可輸入exit結束while迴圈
    eng=float(input("請輸入英文成績: "))  
    math=float(input("請輸入數學成績: "))
    chinese=float(input("請輸入國文成績: "))
    avg_r=Avg(chinese,eng,math)  #呼叫Avg函式
    
    students.append(name)  #將輸入的姓名新增到students的集合 
    eng_l.append(eng)
    chinese_l.append(chinese)
    math_l.append(math)
    avg_l.append(avg_r)
    avg_n.append(avg_r)
    avg_p.append(avg_r)
rank_l=rank(avg_n)
print("  姓 名  國文  英文  數學   平均  名次")
print("----------------------------------------")   
for p in range(0,len(students)):  #print所有學生的姓名及成績
    print("%5s  %.1f  %.1f  %.1f  %.1f     %d" % (students[p],chinese_l[p],eng_l[p],math_l[p],avg_p[p],rank_l[p]))
