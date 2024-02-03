from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  #switch to frame

year = "2023"
month = "March"
date = "30"

driver.find_element(By.XPATH, "//*[@id='datepicker']").click()  #open datepicker 

while True:
    mon: driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr: driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    
    else: 
        #driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  #Next Arrow 
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()  #previous

    
#select date
        
dates= dates=driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")


for ele in dates:
    if ele.text==date:
        ele.click()
        break

driver.close()