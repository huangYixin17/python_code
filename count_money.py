# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:10:19 2019

@author: user
"""
fruit={"香蕉":10,"芒果":20,"蘋果":30}  #建立字典
fruit2=fruit.copy()         #把字典fruit複製
customer=list(fruit2)       #將字典的(香蕉,芒果,蘋果)存入customer
customer_buynum=[]        #建立空串列
n=[]                        
def customer_data():
    while(True):
        for i in range(0,len(customer)):  #將fruit2的值設定為0
            fruit2[customer[i]] = 0
        print("顧客%d請購買: " % (len(n)+1))
        while(True):
            customer_fruit=input("請輸入購買的水果名稱: ")
            customer_num=int(input("請輸入要購買的數量: "))
            fruit2[customer_fruit] = customer_num       #將對應的水果，存取正確的數量
            exit_1=input("購買完成，離開請輸入\"E\"")   #離開輸入E
            if(exit_1 == "E" or exit_1 == "e"):
                break
        for i in range(0,len(customer)):        #將customer_buynum新增水果的數量
            customer_buynum.append(fruit2.get((customer[i]),0))
        n.append(customer_buynum)     #將customer_buynum的數量以串列的方式新增至N
        exit_2 =input("需要採購嗎?(y/n) ")       #是否有顧客還須購買?
        if(exit_2 == "N" or exit_2 == "n"):     #沒有請輸入N
            break
    return n
#程式開始

customer_data=customer_data()  #將購買資料回傳

#程式輸出
count = 0
print("姓名  香蕉  芒果  蘋果  總價")
for i in range(0,len(customer_buynum),3):   
    print("顧客%s%4s%5s%6s %6s" % (count+1,n[0][i],n[0][i+1],n[0][i+2],fruit["香蕉"]*n[0][i]+fruit["芒果"]*n[0][i+1]+fruit["蘋果"]*n[0][i+2]))

