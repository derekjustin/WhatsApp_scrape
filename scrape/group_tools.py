import time

#Application Created Code
from scrape.system_tools import SystemTools
from scrape.browser_tools import BrowserTools

class GroupTools:
    #############
    # Class to naviate Group automation for https://web.whatsapp.com/
    # through Google Chrome Browser
    #############

     def __init__(self):
         self.browser = BrowserTools()

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

     def join_multiple_groups(self):
         if  self.browser.check_browser_status() == "Alive":
             pass
         else:
             self.browser.open_browser()
         file_name = input("Please provide name of the file to read group links from inside of 'scrape/group_files/groups_to_join' folder: ")
         with open("scrape/group_files/groups_to_join" + file_name) as fp:
             while True:
                 line = fp.readline()
                 if not line:
                     break