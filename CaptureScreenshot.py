from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

serv_obj = Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(4)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#driver.save_screenshot(r"C:\Users\USER\Documents\seleniumProjects\.idea\screenshotImage.png")
driver.save_screenshot(os.getcwd() + "\\screenshotImage.png")

driver.quit()
