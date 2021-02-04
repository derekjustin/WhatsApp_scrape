import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/home/jstrelka/.config/google-chrome")
driver = webdriver.Chrome(executable_path='src/browser_driver/chromedriver', chrome_options=options)
driver.get("https://web.whatsapp.com/")


time.sleep(10)

driver.quit()
