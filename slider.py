from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains



serv_obj = Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(2)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider =driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/span[1]")
max_slider =driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/span[2]")

print("location of slider before moving")
print(min_slider.location)
print(max_slider.location)

action = ActionChains(driver)

action.drag_and_drop_by_offset(min_slider, 150, 0).perform()
action.drag_and_drop_by_offset(max_slider, -50, 0 ).perform()