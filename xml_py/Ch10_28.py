# -*- coding: utf-8 -*-
"""
修改xml的檔案
上傳新的資料取代舊資料
"""

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
for rank in root.iter("rank")   #找尋root所有(rank)所有節點
    new_rank=int(rank.text)+1   #所有rank都增加'1'
    rank.text=str(new_rank)     #新的rank存入rank
    rank.set("updated","yes")       #可有可無的一行,是新增root屬性'updated'='yes'
tree.write("Ch1028output.xml",encoding="utf-8") #寫入到檔案,有點像寫好程式儲存的意思
