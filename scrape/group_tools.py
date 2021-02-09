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

     def join_group(self):
         if  self.browser.check_browser_status() == "Alive":
             pass
         else:
             self.browser.open_browser()
         group_link = input("Please enter a WhatsApp group link: ")
         self.browser.go_to_url(group_link)
         time.sleep(3)

        
