# -*- coding: utf-8 -*-
"""
讀取xml的檔案
讀取檔案內的標籤,屬性
了解跟目錄以及子節點的用法
如何讀取節點內容

"""
import xml.etree.ElementTree as et  #import xml的檔案 設變數為et
tree = et.ElementTree(file='a1.xml')  #(變數tree)為(變數et)開啟檔案的元素
root = tree.getroot()  #(變數root)是(變數tree)的跟目錄
print(root.tag)  #輸出跟目錄的大標題
for child in root:
         print('tag:', child.tag, 'attributes:', child.attrib)  #.tag 是讀取某目錄底下的子目錄,.attrib是某目錄的屬性
         for grandchild in child:
             print('\ttag:', grandchild.text, 'attributes:', grandchild.attrib) #.text是目錄裡面的內容
#print(len(root))     # 菜單選項的數目
#print(len(root[0]))  # 早餐選項的數目
             
print("             時間            內容")
print("-----------------------------------")
for child in root:
    print("%-13s%-10s" % (child.tag,child.attrib["hours"]),end = "\0")  #用.attrib["hours"]是字典的找尋方式
    for grandchild in child:
        print("| %2s%s" % (grandchild.text,grandchild.attrib["cash"]),end = "\0")
    print("\n")    
        

