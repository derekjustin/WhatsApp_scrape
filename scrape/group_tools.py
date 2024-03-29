import time
import os.path
import datetime
import os
import glob

# Application Created Code
from scrape.browser_tools import BrowserTools
from scrape.system_tools import SystemTools
from scrape.scrape_html import MultiProcessHtml


class GroupTools:
    #############
    # Class to naviate Group automation for https://web.whatsapp.com/
    # through Google Chrome Browser
    #############
    system_tools = SystemTools()

    def __init__(self):
        self.browser = BrowserTools()
        self.scraper = MultiProcessHtml()
        self.group_elements = []
        self.group_list = []

    def join_group_cli(self, timeout=60):
        group_link = input("Please enter a WhatsApp group link or 'back' to return to group_tools menu: ")
        if group_link == 'back':
            return None
        self.browser.open_browser()
        if self.__navigate_join_screens_and_return_success(group_link, timeout) is False:
            print("\n\nFailed to join group: " + group_link + "\nCheck to make sure the link is valid.")
            self.browser.close_browser()
            return False
        else:
            self.browser.close_browser()
            return True

    def join_group_gui(self, group_link):
        self.browser.open_browser()
        success = self.__navigate_join_screens_and_return_success(group_link)
        self.browser.close_browser()
        return success

    def join_multiple_groups_cli(self,
                                 groups_to_join_path=system_tools.get_groups_to_join_path(),
                                 groups_failed_path=system_tools.get_groups_failed_path(),
                                 timeout=60):
        try:
            if not os.path.exists(groups_to_join_path):
                os.makedirs(groups_to_join_path)
            if not os.path.exists(groups_failed_path):
                os.makedirs(groups_failed_path)
        except Exception:
            return None
        while True:
            file_name = input("Please provide name of the file to read group links from inside of the\n"
                              "'scrape/group_files/groups_to_join' folder or 'back' to return to group_tools menu: ")
            if os.path.isfile(groups_to_join_path + file_name):
                break
            elif file_name == 'back':
                return None
            else:
                print("FILE DOES NOT EXIST")
        self.browser.open_browser()
        with open(groups_to_join_path + file_name, 'r') as input_group_file:
            failed_group_file = open(groups_failed_path + file_name, 'w+')
            while True:
                group_link = input_group_file.readline()
                if not group_link:
                    break
                if self.__navigate_join_screens_and_return_success(group_link, timeout) is not True:
                    failed_group_file.write(group_link)
        failed_group_file.close()
        input_group_file.close()
        self.browser.close_browser()
        # TODO: Add functionality to check if any groups failed to join and notify user of failure or complete success.

    def join_multiple_groups_gui(self,
                                 file_name,
                                 groups_to_join_path=system_tools.get_groups_to_join_path(),
                                 groups_failed_path=system_tools.get_groups_failed_path(),
                                 timeout=60):
        try:
            if not os.path.exists(groups_to_join_path):
                os.makedirs(groups_to_join_path)
            if not os.path.exists(groups_failed_path):
                os.makedirs(groups_failed_path)
        except Exception:
            return False
        if os.path.isfile(groups_to_join_path + file_name):
            self.browser.open_browser()
            with open(groups_to_join_path + file_name, 'r') as input_group_file:
                failed_group_file = open(groups_failed_path + file_name, 'w+')
                while True:
                    group_link = input_group_file.readline()
                    if not group_link:
                        break
                    if self.__navigate_join_screens_and_return_success(group_link, timeout) is not True:
                        failed_group_file.write(group_link)
            failed_group_file.close()
            input_group_file.close()
            self.browser.close_browser()
            return True
        else:
            return False

    def save_all_groups_data_cli(self,
                                 url="https://web.whatsapp.com/",
                                 raw_html_file=system_tools.get_html_dir_path() + '/'):
        try:
            self.get_group_list(url)
            if not os.path.exists(raw_html_file):
                os.makedirs(raw_html_file)
        except Exception:
            return False
        self.browser.open_browser()
        self.browser.go_to_url(url)
        for group in self.group_list:
            html = self.__get_raw_html(group)
            timestamp = datetime.datetime.now()
            self.__write_group_data_to_html_file(group, timestamp.strftime("%Y%m%d%H:%M:%S"), html, raw_html_file)
            self.__remove_group_old_html(group, raw_html_file)
        self.scraper.process_all_raw_html_to_pickles(self.browser.system_tools.get_raw_html_list(), self.browser.system_tools.get_processed_html_pickles_dir(), self.browser.system_tools.get_html_dir_path())
        print("All group data has been saved SUCCESSFULLY.")
        self.browser.close_browser()
        return True

    def save_all_groups_data_gui(self,
                                 url="https://web.whatsapp.com/",
                                 raw_html_file=system_tools.get_html_dir_path() + '/'):
        try:
            self.get_group_list(url)
            if not os.path.exists(raw_html_file):
                os.makedirs(raw_html_file)
        except Exception:
            return False
        self.browser.open_browser()
        self.browser.go_to_url(url)
        for group in self.group_list:
            html = self.__get_raw_html(group)
            timestamp = datetime.datetime.now()
            self.__write_group_data_to_html_file(group, timestamp.strftime("%Y%m%d%H:%M:%S"), html, raw_html_file)
            self.__remove_group_old_html(group, raw_html_file)
        self.scraper.process_all_raw_html_to_pickles(self.browser.system_tools.get_raw_html_list(), self.browser.system_tools.get_processed_html_pickles_dir(), self.browser.system_tools.get_html_dir_path())
        self.browser.close_browser()
        return True

    def save_single_groups_data_cli(self,
                                    url="https://web.whatsapp.com/",
                                    raw_html_file=system_tools.get_html_dir_path()):
        try:
            group = input("\nPlease Enter A Group Name: ")
            if group == "back":
                return None
            elif not os.path.exists(raw_html_file):
                os.makedirs(raw_html_file)
            self.browser.open_browser()
            self.browser.go_to_url(url)
        except Exception:
            print("Please make sure you have a secure internet connection and you are signed into a whatsapp web account, then try again.")
            self.browser.close_browser()
            return None
        html = self.__get_raw_html(group)
        time = datetime.datetime.now()
        self.__write_group_data_to_html_file(group, time.strftime("%Y%m%d%H:%M:%S"), html, raw_html_file)
        self.__remove_group_old_html(group, raw_html_file)
        # self.scraper.process_all_raw_html_to_pickles()
        print("Group data has been saved SUCCESSFULLY.")
        self.browser.close_browser()

    def save_single_groups_data_gui(self,
                                    group,
                                    url="https://web.whatsapp.com/",
                                    raw_html_file=system_tools.get_html_dir_path()):
        try:
            if not os.path.exists(raw_html_file):
                os.makedirs(raw_html_file)
            self.browser.open_browser()
            self.browser.go_to_url(url)
        except Exception:
            self.browser.close_browser()
            return False
        html = self.__get_raw_html(group)
        time = datetime.datetime.now()
        self.__write_group_data_to_html_file(group, time.strftime("%Y%m%d%H:%M:%S"), html, raw_html_file)
        self.__remove_group_old_html(group, raw_html_file)
        # self.scraper.process_all_raw_html_to_pickles()
        self.browser.close_browser()
        return True

    def print_groups(self, url="https://web.whatsapp.com/"):
        try:
            self.get_group_list(url)
        except Exception:
            return False
        print(30 * '#' + " GROUP LIST " + 30 * '#')
        for group in self.group_list:
            print(group)
        print(70 * '#')
        return self.group_list

    def get_group_list(self, url="https://web.whatsapp.com/"):
        try:
            self.group_list = []
            self.browser.open_browser()
            self.browser.go_to_url(url)
            self.group_elements = self.browser.browser_find_multiple_elements_by_xpath_with_wait("//span[@class='_35k-1 _1adfa _3-8er']")
        except Exception:
            self.browser.close_browser()
            print("Please make sure you have a secure internet connection and you are signed into a whatsapp web account, then try again.")
            return
        for element in self.group_elements:
            if element.get_attribute("title") != '':
                self.group_list.append(element.get_attribute('title'))
        self.browser.close_browser()
        return self.group_list

# **********************PRIVATE FUNCTIONS **************************************

    def __get_raw_html(self, group):
        self.browser.browser_find_element_by_xpath_with_wait("//span[@title='" + group + "']").click()
        self.browser.browser_find_element_by_xpath_with_wait("//span[@title='" + group + "']")
        return self.browser.driver.page_source

    def __write_group_data_to_html_file(self, group, time, html, raw_html_file):
        fp = open(raw_html_file + time + "_" + group, "w+")
        fp.write(html)
        fp.close()

    def __navigate_join_screens_and_return_success(self, group_link, timeout=60):
        try:
            self.browser.go_to_url(group_link)
            group_name = self.browser.browser_find_element_by_xpath_with_wait("//h2[@class='_2yzk']", timeout).text
            self.browser.browser_find_element_by_xpath_with_wait("//a[@title='Follow this link to join']", timeout).click()
            self.browser.browser_find_element_by_link_text_with_wait("use WhatsApp Web", timeout).click()
        except Exception:
            return False
        try:
            self.browser.browser_find_element_by_xpath_with_wait("//div[text()='Join group']", timeout).click()
        except Exception:
            pass
        try:
            if group_name == self.browser.browser_find_element_by_xpath_with_wait("//span[@title='" + group_name + "']", timeout).get_attribute("title"):
                return True
            else:
                return False
        except Exception:
            return False

    def __remove_group_old_html(self, group, raw_html_file):
        found_files = glob.glob(raw_html_file + "/*_" + group)
        newest_html_file = ''
        for file in found_files:
            if file > newest_html_file:
                newest_html_file = file
            else:
                continue
        for file in found_files:
            if file == newest_html_file:
                continue
            else:
                os.remove(file)
