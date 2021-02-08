import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#Application Created Code
from scrape.system_tools import SystemTools
from scrape.browser_tools import BrowserTools


class GroupTools:

     def __init__(self):
         self.browser = BrowserTools()
         """browser.go_to_url('https://google.com')
         time.sleep(5)
         browser.go_to_url('https://web.whatsapp.com')
         time.sleep(5)
         browser.close()"""

     def join_groups(self):
          print("Im a tool.")
