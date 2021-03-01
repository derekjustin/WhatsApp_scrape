import time
import os.path
import datetime
import os

# Application Created Code
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

    def join_group_cli(self):
        group_link = input("Please enter a WhatsApp group link or 'back to return to group_tools menu: ")
        if group_link == 'back':
            return
        self.browser.open_browser()
        if self.__navigate_join_screens_and_return_success(group_link) is False:
            print("\n\nFailed to join group: " + group_link + "\nCheck to make sure the link is valid.")
        self.browser.close_browser()

    def join_group_gui(self, group_link):
        self.browser.open_browser()
        success = self.__navigate_join_screens_and_return_success(group_link)
        self.browser.close_browser()
        return success

    def join_multiple_groups_cli(self):
        try:
            if not os.path.exists('scrape/group_files/groups_to_join'):
                os.makedirs('scrape/group_files/groups_to_join')
            if not os.path.exists('scrape/group_files/groups_failed'):
                os.makedirs('scrape/group_files/groups_failed')
        except:
            return
        while True:
            file_name = input("Please provide name of the file to read group links from inside of the\n"
                              "'scrape/group_files/groups_to_join' folder or 'back' to return to group_tools menu: ")
            if os.path.isfile("scrape/group_files/groups_to_join/" + file_name):
                break
            elif file_name == 'back':
                return
            else:
                print("FILE DOES NOT EXIST")
        self.browser.open_browser()
        with open("scrape/group_files/groups_to_join/" + file_name, 'r') as input_group_file:
            failed_group_file = open("scrape/group_files/groups_failed/" + file_name, 'w+')
            while True:
                group_link = input_group_file.readline()
                if not group_link:
                    break
                if self.__navigate_join_screens_and_return_success(group_link) is not True:
                    failed_group_file.write(group_link)
        failed_group_file.close()
        input_group_file.close()
        self.browser.close_browser()
        # TODO: Add functionality to check if any groups failed to join and notify user of failure or complete success.

    def join_multiple_groups_gui(self, file_name):
        try:
            if not os.path.exists('scrape/group_files/groups_to_join'):
                os.makedirs('scrape/group_files/groups_to_join')
            if not os.path.exists('scrape/group_files/groups_failed'):
                os.makedirs('scrape/group_files/groups_failed')
        except:
            return False
        if os.path.isfile("scrape/group_files/groups_to_join/" + file_name):
            self.browser.open_browser()
            with open("scrape/group_files/groups_to_join/" + file_name, 'r') as input_group_file:
                failed_group_file = open("scrape/group_files/groups_failed/" + file_name, 'w+')
                while True:
                    group_link = input_group_file.readline()
                    if not group_link:
                        break
                    if self.__navigate_join_screens_and_return_success(group_link) is not True:
                        failed_group_file.write(group_link)
            failed_group_file.close()
            input_group_file.close()
            self.browser.close_browser()
            return True
        else:
            return False
        # TODO: Add functionality to check if any groups failed to join and notify user of failure or complete success.


    def save_all_groups_data(self):
        try:
            self.get_group_list()
            if not os.path.exists('scrape/group_files/raw_html_files'):
                os.makedirs('scrape/group_files/raw_html_files')
        except:
            return
        self.browser.open_browser()
        self.browser.go_to_url("https://web.whatsapp.com/")
        for group in self.group_list:
            html = self.__get_raw_html(group)
            time = datetime.datetime.now()
            self.__write_group_data_to_html_file(group, time.strftime("%Y%m%d%H:%M:%S"), html)
        print("All group data has been saved SUCCESSFULLY.")
        self.browser.close_browser()

    def save_single_groups_data(self):
        try:
            group = input("\nPlease Enter A Group Name: ")
            if not os.path.exists('scrape/group_files/raw_html_files'):
                os.makedirs('scrape/group_files/raw_html_files')
            self.browser.open_browser()
            self.browser.go_to_url("https://web.whatsapp.com/")
        except:
            print("Please make sure you have a secure internet connection and you are signed into a whatsapp web account, then try again.")
            self.browser.close_browser()
            return
        html = self.__get_raw_html(group)
        time = datetime.datetime.now()
        self.__write_group_data_to_html_file(group, time.strftime("%Y%m%d%H:%M:%S"), html)
        print("Group data has been saved SUCCESSFULLY.")
        self.browser.close_browser()

    def print_groups(self):
        try:
            self.get_group_list()
        except:
            return
        print(30 * '#' + " GROUP LIST " + 30 * '#')
        for group in self.group_list:
            print(group)
        print(70 * '#')

    def get_group_list(self, url="https://web.whatsapp.com/"):
        try:
            self.group_list = []
            self.browser.open_browser()
            self.browser.go_to_url(url)
            self.group_elements = self.browser.browser_find_multiple_elements_by_xpath_with_wait("//span[@class='_35k-1 _1adfa _3-8er']")
        except:
            self.browser.close_browser()
            print("Please make sure you have a secure internet connection and you are signed into a whatsapp web account, then try again.")
            return
        for element in self.group_elements:
            if element.get_attribute("title") != '':
                self.group_list.append(element.text)
        self.browser.close_browser()
        return self.group_list

# **********************PRIVATE FUNCTIONS **************************************

    def __get_raw_html(self, group):
        self.browser.browser_find_element_by_xpath_with_wait("//span[text()='" + group + "']").click()
        self.browser.browser_find_element_by_xpath_with_wait("//span[text()='" + group + "']")
        return self.browser.driver.page_source

    def __write_group_data_to_html_file(self, group, time, html):
        fp = open("scrape/group_files/raw_html_files/" + time + "_" + group, "w+")
        fp.write(html)
        fp.close()

    def __navigate_join_screens_and_return_success(self, group_link):
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
