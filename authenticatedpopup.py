from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.get("https://admin:admin@the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()