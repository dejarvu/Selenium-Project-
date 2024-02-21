from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
driver.maximize_window()
driver.implicitly_wait(2)

# Switch to the iframe containing the button
driver.switch_to.frame("iframeResult")

# Find the button element within the iframe
button = driver.find_element(By.XPATH, "//button[normalize-space()='Double-click me']")

# Perform double-click action on the button
action = ActionChains(driver)
action.double_click(button).perform()
