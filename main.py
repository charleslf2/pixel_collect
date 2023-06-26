import requests 
from bs4 import BeautifulSoup

keyword="tits"

url="https://images.google.com/search?q="+keyword+"&tbm=isch&sxsrf"

r=requests.get(url)

#print(r.text)

soup=BeautifulSoup(r.content, 'html.parser')

links=soup.find_all('img')

link_list=[]

for link in links:
    link_href=link.get('src')
    #link_href=link_href.split("https")
    #link_list.append(href_c)
    link_list.append(link_href)
    #link_list.append("==========================================\n")
    #print(link_href) 

for i in range(len(link_list)):
    begin=link_list[i][0:5]
    print(begin)
    if begin =="https":
        image_data=requests.get(link_list[i]).content
        img_file=open("image_{:03d}.jpg".format(i),"wb")
        img_file.write(image_data)
        img_file.close()
        #print(image_data)

#print(soup.prettify())
func=open("index.html","w",encoding="utf-8")
func.write(str(link_list))
func.close()


#print(soup.find_all('img'))







