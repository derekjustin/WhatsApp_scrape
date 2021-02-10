import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

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
         self.browser.browser_find_element_by_xpath_with_wait("//a[@title='Follow this link to join']").click()
         self.browser.browser_find_element_by_link_text_with_wait("use WhatsApp Web").click()
         self.browser.browser_find_element_by_xpath_with_wait("//div[text()='Join group']").click()
         time.sleep(3)

