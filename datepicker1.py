from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Create a WebDriver instance using the Chrome driver executable
serv_obj = Service("C:\\Users\\USER\\Documents\\Setup\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Open the jQuery UI datepicker example page
driver.get("https://jqueryui.com/datepicker/")

# Maximize the browser window for a better view
driver.maximize_window()

# Click on the date input field to open the date picker
driver.find_element(By.ID, "datepicker").click()

# Select the month from the dropdown
datepicker_month = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text("Dec")

# Select the year from the dropdown
datepicker_year = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
datepicker_year.select_by_visible_text("2022")

# Locate all date elements in the datepicker
alldates = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

# Iterate through the date elements and click on the desired date (e.g., "25")
for date in alldates:
    if date.text == "25":
        date.click()
        break
