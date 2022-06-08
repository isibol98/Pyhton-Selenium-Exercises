from unittest import result
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = "https://github.com"
driver.get(url)

driver.maximize_window()
searchInput = driver.find_element_by_class_name("form-control")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
result = driver.find_elements_by_css_selector(".repo-list-item a")
for element in result:
    print(element.text)
driver.close()