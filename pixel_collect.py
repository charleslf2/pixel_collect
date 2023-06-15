#import requests 
from selenium import webdriver
from selenium.webdriver.common.by import By

keyword="ai"

url="https://images.google.com/search?q="+keyword



driver=webdriver.Chrome()


driver.get(url)

image_btn=driver.find_element(By.XPATH,"//*[contains(text(),'Images')]")

image_btn.click()

print(image_btn)
print(driver.title)

#driver.implicitly_wait(120)




#r =requests.get("https://images.google.com/search?q="+keyword)
