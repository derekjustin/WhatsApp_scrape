import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#Application Created Code
from scrape.browser_tools import BrowserTools



def join_groups():

    browser = BrowserTools()
    browser.go_to_url('https://google.com')
    time.sleep(5)
    browser.go_to_url('https://web.whatsapp.com')
    time.sleep(5)
    browser.close()
    #if browser open 
        #skip
    #else:
        #openbrowser
