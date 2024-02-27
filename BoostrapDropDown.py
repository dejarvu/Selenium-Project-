from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(4)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Click on the country dropdown to open it using XPath
driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

# Find all the options in the country dropdown list using XPath
countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")

# Iterate through each option and click on the one with the text "Nigeria"
for country in countries_list:
    if country.text == "Nigeria":
        country.click()
        break
