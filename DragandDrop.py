from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains



serv_obj = Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(2)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")
driver.maximize_window()

source_ele = driver.find_element(By.ID, "box6")
target_ele = driver.find_element(By.ID, "box106")
source_ele1 = driver.find_element(By.ID, "box7")
target_ele1 = driver.find_element(By.ID, "box107")
source_ele2 = driver.find_element(By.ID, "box3")
target_ele2 = driver.find_element(By.ID, "box103")

action = ActionChains(driver)
action.drag_and_drop(source_ele,target_ele).perform()
action.drag_and_drop(source_ele1,target_ele1).perform()
action.drag_and_drop(source_ele2,target_ele2).perform()