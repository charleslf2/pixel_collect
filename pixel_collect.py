import requests 
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import base64

keyword="ai"

url="https://images.google.com/search?q="+keyword



driver=webdriver.Chrome()


driver.get(url)

image_btn=driver.find_element(By.XPATH,"//*[contains(text(),'Images')]")


image_btn.click()

#d_img_btn=image_btn.find_element(By.TAG_NAME, value="div")

#d_img_btn.click()

r=requests.get(driver.current_url)

soup=BeautifulSoup(r.text, 'html.parser')


for img in soup.find_all("img"):
    
    image_url=img.get("src")

    print(image_url)



#print(soup.find_all('img'))

driver.implicitly_wait(120)







