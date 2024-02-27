from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(4)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# reglink = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)

# #new tab on selenium 4
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://orangehrm.com/")

#new window on selenium 4
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('tab')
driver.get("https://orangehrm.com/")
