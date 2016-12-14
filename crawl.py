# encoding : utf-8


import requests
from bs4 import BeautifulSoup
import os
import sys

Sex = sys.argv[1]

domain = 'http://www.i-part.com.tw'



def crawl():
        #domain = 'http://www.i-part.com.tw'
        user =  soup.find_all(style="padding-top:3pt")
        for line in user:
                L = line.a['href']
                print(L.split('?u=')[1])
                url = domain+L
                cmd = 'python3 ./crawl_user.py ' + url
                f = open('Data.csv','a',encoding = 'UTF-8')
                os.system(cmd)
                f.write('\n')
                f.close()




for i in  range(0, 10 , 1):
	print(i)
	url = 'http://www.i-part.com.tw/search/query_online.php?f=all&s='+Sex+'&page='+str(i)
	print(url)
	r = requests.get(url)
	soup=BeautifulSoup(r.text.encode('utf-8'), "html.parser")
	crawl()





