import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('selenium_practice\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(5)

driver.find_element_by_name('q').send_keys("Cheese" + Keys.RETURN)

time.sleep(10)

driver.quit()