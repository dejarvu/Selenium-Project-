from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


serv_obj = Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

# Login
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

time.sleep(5)

#Admin-->User management --> users
admin=driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
usermgmt=driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagemnt']")
users=driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

#mousehover
act=ActionChains(driver)


act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()