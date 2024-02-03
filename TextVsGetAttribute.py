from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")

emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")

emailbox.clear()
emailbox.send_keys("abc@gmail.com")

print("result of text:", emailbox.text)
print("result of get_attribute():", emailbox.get_attribute('value'))

driver.quit