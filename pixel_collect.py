import requests 
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from PIL import image

keyword="ai"

url="https://images.google.com/search?q="+keyword



driver=webdriver.Chrome()


driver.get(url)

image_btn=driver.find_element(By.XPATH,"//*[contains(text(),'Images')]")


image_btn.click()


r=requests.get(driver.current_url)

soup=BeautifulSoup(r.text, 'html.parser')


for imgs in soup.find_all("img"):
    image_url=imgs.get("src")
    data=request.get(image_url).content


#print(soup.find_all('img'))

driver.implicitly_wait(120)







