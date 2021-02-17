import time
import os.path
import datetime

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
         self.group_elements = []
         self.group_list = []

     def join_group(self):
         group_link = input("Please enter a WhatsApp group link: ")
         if self.browser.check_browser_status() == "Alive":
             pass
         else:
             self.browser.open_browser()
         if self.navigate_join_screens_and_return_success(group_link) == False:
             print("\n\nFailed to join group: " + group_link + "\nCheck to make sure the link is valid.")

     def join_multiple_groups(self):
         while True:
             file_name = input("Please provide name of the file to read group links from inside of the\n"
                               "'scrape/group_files/groups_to_join' folder or 'back' to return to main menu: ")
             if os.path.isfile("scrape/group_files/groups_to_join/" + file_name):
                 break
             elif file_name == 'back':
                 quit()
             else:
                 print("FILE DOES NOT EXIST")
         if self.browser.check_browser_status() == "Alive":
             pass
         else:
             self.browser.open_browser()
         with open("scrape/group_files/groups_to_join/" + file_name, 'r') as input_group_file:
             failed_group_file = open("scrape/group_files/groups_failed/" + file_name, 'w')
             while True:
                 group_link = input_group_file.readline()
                 if not group_link:
                     break
                 if self.navigate_join_screens_and_return_success(group_link) != True:
                     failed_group_file.write(group_link)
             failed_group_file.close()
             input_group_file.close()
             # TODO: Add functionality to check if any groups failed to join and notify user of failure or complete success.

     def print_groups(self):
         group_list = self.get_group_list()
         print(30 * '#' + " GROUP LIST " + 30 * '#')
         for group in group_list:
             print(group)
         print(70 * '#')
         self.browser.close_browser()

     def navigate_join_screens_and_return_success(self, group_link):
         try:
             self.browser.go_to_url(group_link)
             group_name = self.browser.browser_find_element_by_xpath_with_wait("//h2[@class='_2yzk']").text     
             self.browser.browser_find_element_by_xpath_with_wait("//a[@title='Follow this link to join']").click()
             self.browser.browser_find_element_by_link_text_with_wait("use WhatsApp Web").click()
         except:
             return False
         try:
             self.browser.browser_find_element_by_xpath_with_wait("//div[text()='Join group']").click()
         except:
             pass
         if group_name == self.browser.browser_find_element_by_xpath_with_wait("//span[@title='" + group_name + "']").text:
             return True
         else:
             return False
         
     def get_group_list(self):
         self.group_elements = []
         self.group_list = []
         if self.browser.check_browser_status() == "Alive":
             pass
         else:
             self.browser.open_browser()
         try:
             self.browser.go_to_url("https://web.whatsapp.com/")
             self.group_elements = self.browser.browser_find_multiple_elements_by_xpath_with_wait("//span[@class='_1hI5g _1XH7x _1VzZY']")
         except:
             print("Please make sure you have a secure internet connection and you are signed into a whatsapp web account, then try again.")
             quit()
         for element in self.group_elements:
             if element.get_attribute("title") != '':
                 self.group_list.append(element.text)
         return self.group_list

     def get_raw_html(self, group):
         self.browser.browser_find_element_by_xpath_with_wait("//span[text()='" + group + "']").click()
         self.browser.browser_find_element_by_xpath_with_wait("//span[text()='" + group + "']")
         return self.browser.driver.page_source

     def write_group_data_to_html_file(self, group, time, html):
         fp = open("scrape/group_files/raw_html_files/" + time + group, "w")
         fp.write(html)
         fp.close()

     def save_all_groups_data(self):
         group_list = self.get_group_list()
         for group in group_list:
             html = self.get_raw_html(group)
             time = datetime.datetime.now()
             self.write_group_data_to_html_file(group, time.strftime("%Y%m%d"), html)


             
