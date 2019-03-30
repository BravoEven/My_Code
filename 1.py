import requests
#coding=utf-8
import sys
import re
import  json
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
city="苏州"
city.encode(encoding="UTF-8")
url='http://www.todayonhistory.com/'

f=open('data.txt','w')

try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        #dict=r.json()

    #print(r.text)
except:
        print("异常",r.status_code)

dict=r.text
dict.encode(encoding='UTF-8')
#dictj=r,json()
f.write(dict)