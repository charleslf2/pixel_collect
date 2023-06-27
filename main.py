import requests 
from bs4 import BeautifulSoup
import re
import os

keyword="ai"

url="https://images.google.com/search?q="+keyword+"&tbm=isch&sxsrf"

r=requests.get(url)

#print(r.text)

soup=BeautifulSoup(r.content, 'html.parser')

links=soup.find_all('a')

link_list=[]
run =True

for link in links:
    link_href=link.get('href')
    link_list.append(link_href)




def get_real_site_url(link_list):
    i_url_list=[]
    for i in range(len(link_list)):
        s_begin=link_list[i][7:12]
        if s_begin =="https":
            i_url=link_list[i]
            i_url_list.append(i_url)
    return i_url_list


def request_to_real_site_url(i_url_list):
    imglink_list=[]
    #img_links=""
    for i in range(len(i_url_list)):
        ll=re.search("(?P<url>https?://[^\s]+)",i_url_list[3]).group("url")
        ll_split=ll.split('&',1)
        l_link=ll_split[0]
        #print(l_link)
        w_r=requests.get(l_link)
        w_soup=BeautifulSoup(w_r.content,'html.parser')
        img_links=w_soup.find_all('img')
        for link in img_links:
            link_h=link.get('src')
            imglink_list.append(link_h)
        return imglink_list 

def download_image(imglink_list):
    for i in range(len(imglink_list)):
        begin=imglink_list[i][0:5]
        if begin =="https":
            #_,ext=os.path.splitext(imglink_list[i])
            image_data=requests.get(imglink_list[i]).content
            img_file=open("image_{:03d}.jpg".format(i),"wb")
            img_file.write(image_data)
            img_file.close()


real_url=get_real_site_url(link_list)

request_url=request_to_real_site_url(real_url)

download_image(request_url)
    

#print(i_url_list)
#print(soup.find_all('img'))

func=open("index.html","w",encoding="utf-8")
func.write(str(request_url))
func.close()



