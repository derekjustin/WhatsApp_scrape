import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def main():

    profile_path = "user-data-dir=/home/jstrelka/.config/google-chrome"
    driver_path = 'src/browser_drivers/chromedriver'
    url = "https://web.whatsapp.com/"

    options = webdriver.ChromeOptions()
    options.add_argument(profile_path)
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    driver.get(url)
    time.sleep(20)
    driver.quit()

main()