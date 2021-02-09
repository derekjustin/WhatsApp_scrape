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
         #WebDriverWait(self.browser.driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "//a[@title='Follow this link to join']")))
         WebDriverWait(self.browser.driver, 3).until(lambda x: x.find_element_by_xpath("//a[@title='Follow this link to join']"))
         self.browser.driver.find_element_by_xpath("//a[@title='Follow this link to join']").click()
         #WebDriverWait(self.browser.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "//a[@class='_36or' and text()='use WhatsApp Web']")))
         WebDriverWait(self.browser.driver, 3).until(lambda x: x.find_element_by_xpath("//a[text()='use WhatsApp Web']"))
         self.browser.driver.find_element_by_xpath("//a[@class='_36or' and text()='use WhatsApp Web']").click()
         #WebDriverWait(self.browser.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "//div[@class='_2xUEC _2XHG4' and text()='Join group']")))
         WebDriverWait(self.browser.driver, 3).until(lambda x: x.find_element_by_xpath("//div[@class='_2xUEC _2XHG4' and text()='Join group']"))
         self.browser.driver.find_elements_by_xpath("//div[@class='_2xUEC _2XHG4' and text()='Join group']").click()
         time.sleep(30)
         

        
