from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(2)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 1. Scroll down the page by pixel
driver.execute_script("window.scrollBy(0,3000)")

# # Get the vertical scroll position
# scroll_position = driver.execute_script("return window.pageYOffset")
# print("Number of pixels moved:", scroll_position) #3000


# #2 scroll down page till element is visible (flag of the country)
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Nigeria']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# scroll_position = driver.execute_script("return window.pageYOffset")
# print("Number of pixels moved:", scroll_position) 

#3 scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
scroll_position = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", scroll_position) 
time.sleep(5)


#4 scroll up to starting postion
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
scroll_position = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", scroll_position) 