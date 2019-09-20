# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:10:19 2019

@author: user

program:輸入要賣的水果,以及要購買的水果,輸出乾淨的格式,並計算總價
"""


 
def build_dict(fruit):      #建立字典
    print("請輸入要賣的水果以及價錢,編輯完成請輸入\"E\"")
    while(True):
        temprary=input("請輸入水果: 或離開(E)")
        if(temprary == "E" or temprary == "e"):
            break
        num=int(input("請輸入價錢: "))
        fruit[temprary]=num
    return fruit

                    
def customer_data():
    while(True):
        for i in range(0,len(customer)):  #將fruit2的值設定為0
            fruit2[customer[i]] = 0
        print("\n顧客%d請購買: " % (len(customer_buynum)+1),end="\0")  #輸出的格式
        for i in range(0,len(customer)):                #輸出的格式
            print("%d.%s" % (i+1,customer[i]),end="\0")  #輸出的格式
        while(True):
            customer_fruit_n=input("請輸入購買的水果代號: (或離開請輸入E)")
            if(customer_fruit_n == "E" or customer_fruit_n == "e"):
                break
            customer_num=int(input("請輸入要購買的數量: "))
            for i in range(0,len(customer)):
                if((customer_fruit_n) == str(i+1)):    
                    customer_fruit_n = customer[i]
                    print(customer[i],customer_fruit_n)
            fruit2[customer_fruit_n] = customer_num       #將對應的水果，存取正確的數量
        for i in range(0,len(customer)):        #將customer_buynum新增水果的數量
            customer_buynum.append(fruit2.get((customer[i]),0))
        exit_2 =input("需要採購嗎?(y/n) ")       #是否有顧客還須購買?
        if(exit_2 == "N" or exit_2 == "n"):     #沒有請輸入N
            break
    return customer_buynum


#程式開始
fruit={}  #新增空字典

#程式輸入
fruit=build_dict(fruit)  #建立字典
fruit2=fruit.copy()         #把字典fruit複製
customer=list(fruit2)       #將字典的(水果名稱)存入customer
customer_buynum=[]        #建立購買的空串列   
customer_data=customer_data()  #將購買資料回傳

#程式輸出

print("姓名 ",end="\0")
for i in range(0,len(customer)):           #輸出的格式(把字典內的水果名稱印出來)
    print("%3s" % (customer[i]),end="\0")  #輸出的格式(以每空 3 格的格式輸出)
print("  總價")

count = 0
total = 0

while(count < (int((len(customer_buynum))/len(customer)))):     #如果count<購買人數,結束while迴圈
    for i in range(0,len(customer_buynum),(len(customer))):     #(0,購買的人數*水果總類,水果種類)
        count+=1                                                #計算人數
        print("顧客%d" % (count),end="\0")        #輸出顧客是第幾位
        for j in range(i,count*len(customer)):      #(第count位顧客,第n種水果)
            print("%4d" %(customer_buynum[j]),end = "\0")  
            total = total+int(fruit[customer[int(j-i)]])*customer_buynum[j]  #計算以顧客為單位的總價錢
        print("%6d\n" % (total))
        total = 0  #以顧客為單位的從新計算價錢


    
    

