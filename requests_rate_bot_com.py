# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
"""
爬台灣銀行的匯率資料
requests就是寫程式去爬別人網站的資料
其他宣告的東西不太懂
"""
import requests
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime,strptime, mktime
from datetime import datetime
from os.path import exists

html = requests.get("http://rate.bot.com.tw/xrt?Lang=zh-TW") #台銀匯率告示表
bsObj = BeautifulSoup(html.content, 'lxml') #網站內的所有.lxml存取
#從lxml找有'table'再從table找'title:牌告匯率',再找'tbody'再找'tr'
#結果是一整串關於美金匯率
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):      
    cell = single_tr.findAll("td")  #再找td 是關於買入及賣出
    #找第1個'td'裡的div'裡的{class:visible-phone}
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0]
    currency_name = currency_name.replace("\r","")  #收尋完資料會有一堆空格跳行
    currency_name = currency_name.replace("\n","")  #需要將全部都用""取代
    currency_name = currency_name.replace(" ","")   #這行也是取代
    currency_rate = cell[2].contents[0]  #讀取第3個td的資料,的第1個內容
    print(currency_name, currency_rate)
    file_name = currency_name + '.csv'  #進行儲存檔案.csv
    now_time = strftime("%Y-%m-%d %H:%M:%S" , localtime())  #目前時間
    if not exists(file_name):
        data = [['          時間        ''|  匯率'] , [now_time, currency_rate]] #如果檔案不存在,執行這行
    else:
        data = [[now_time , currency_rate]] #如果檔案存在,執行這行
    f = open(file_name, "a" , encoding = "UTF-8")  #打開檔案
    w = csv.writer(f)   #存取資料
    w.writerows(data)   #存取資料