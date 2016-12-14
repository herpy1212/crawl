# encoding : utf-8


import requests
from bs4 import BeautifulSoup

f = open('Data.csv','w',encoding = 'UTF-8')

url = 'http://www.i-part.com.tw/file/file_viewfile.php?u=8105392'
r = requests.get(url)
soup=BeautifulSoup(r.text.encode('utf-8'), "html.parser")

def clean(L):
        #L = line.text
	L = L.replace('\t','')
	L = L.replace('\n','')
	L = L.replace('\r','')
	L = L.replace(' ','')
	L = L.replace('\xa0','')
	L = L.replace('\u3000','')
	L = L.split('：')
	return L

def capture(*label):
	for line in label :
		L = line.text
		L = clean(L)
		#print(L[0]+',')
		if L[0] != "":			
			f.write(L[0]+';')
		
"""

for line in soup.find_all(style="margin:auto;background-color:#FFFFFF;border:1px solid #c2e0ff;padding:10px"):
	L = line.text
	L = clean(L)
	print(L[0]+',')


"""
user_data = soup.find_all(style="font-size:11pt")
user_data2 = soup.find_all(style="border-bottom:1px dashed #999999;padding-left:10px")
user_friend = soup.find(style="margin:auto;width:190px;font-size:9pt;background-color:#f3f3f3;padding:5px") 
user_friend = user_friend.text.split('\n')

hobby = soup.findAll("span", { "class" : "hobbyTag" })

capture( *user_data )
capture( *user_data2 )
#capture( *user_friend )

for line in user_friend :
	L = clean(line)
	#print(L[0]+',')
	if L[0] != "" :
		f.write(L[0]+';')

f.write('興趣')


"""
tag = ''
for line in hobby :
	L = line.text
	tag = L + ';' + H

if tag != ""
	f.write(tag+',')
"""
f.write('\n')

f.close()
