from appdirs import *
import platform
import os
import re


class SystemTools:
    #############
    # Class to manage file pathing for cross platforms
    #############
    def __init__(self, platform_system = platform.system()):
        # Get the OS
        #self.platform_os = platform.system()
        self.platform_os = platform_system
        print(self.platform_os)
        # Find where Chrome stores the users Google Account on a given OS
        if (self.platform_os == "Darwin"):
            self.app_name = "Google/Chrome"
            self.app_author = "Google"
        elif(self.platform_os == "Linux"):
            self.app_name = "google-chrome"
            self.app_author = "Google"
        elif(self.platform_os != "Linux" or self.platform_os == "Darwin"):
            raise Exception("WhatsAppScrape can not read your currrent OS\nPlease ensure you are using MacOS or Ubuntu")
        # Use appdirs library to find the users Chrome Account
        self.config_path = user_config_dir(self.app_name, self.app_author)
        self.current_working_dir = self.get_cwd_path()

    def get_os_platform(self):
        return platform.system()

    def get_chrome_config_path(self):
        return self.config_path

    def get_cwd_path(self):
        return os.getcwd()

    def get_sys_platform(self):
        return self.platform_os

    def get_html_dir_path(self):
        return self.get_cwd_path() + '/scrape/group_files/raw_html_files'

    def get_raw_html_list(self):
        html_dir = self.get_html_dir_path()
        return os.listdir(html_dir)

    def get_processed_html_pickles_dir(self):
        return self.get_cwd_path() + '/scrape/group_files/processed_html_pickles'

    def delete_all_files_in_dir(self, myfolder):
        mypath = myfolder
        for root, dirs, files in os.walk(mypath):
            for file in files:
                os.remove(os.path.join(root, file))

    def clean_processed_pickle_dir(self):
        if not os.path.isdir(self.get_processed_html_pickles_dir()):
            os.mkdir(self.get_processed_html_pickles_dir())
        else:
            self.delete_all_files_in_dir(self.get_processed_html_pickles_dir())
