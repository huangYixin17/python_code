# -*- coding: utf-8 -*-
"""
刪除xml的資料
"""
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
for country in root.findall('country'):
    rank=int(country.find("rank").text)
    if rank>50:
        root.remove(country)  #移除整個'country'內的所有內容
tree.write("Ch10_29output.xml",encoding="utf-8") #儲存











