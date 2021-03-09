import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.command import Command

from webdriver_manager.chrome import ChromeDriverManager

# Application Created Code
from scrape.system_tools import SystemTools


class BrowserTools:
    #############
    # Class to use the selenium library to navigate the
    #    Google Chrome Browser
    #############

    def __init__(self):
        # Setup the selenium drivers
        self.system_tools = SystemTools()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("user-data-dir=" + self.system_tools.get_chrome_config_path())
        self.executable_path = ChromeDriverManager().install()

    def init_browser(self):
        self.driver = webdriver.Chrome(executable_path=self.executable_path,
                                       options=self.options)

    def open_browser(self):
        try:
            self.driver.execute(Command.STATUS)
        except Exception:
            return self.init_browser()

    def browser_find_element_by_xpath_with_wait(self, element_description):
        element = ''
        timeout_counter = 0
        while not element and timeout_counter <= 60:
            timeout_counter += 1
            time.sleep(2)
            try:
                element = self.driver.find_element_by_xpath(element_description)
            except Exception:
                continue
        return element

    def browser_find_multiple_elements_by_xpath_with_wait(self, elements_description):
        elements = ''
        timeout_counter = 0
        while not elements and timeout_counter <= 60:
            timeout_counter += 1
            time.sleep(2)
            try:
                elements = self.driver.find_elements_by_xpath(elements_description)
            except Exception:
                continue
        return elements

    def browser_find_element_by_link_text_with_wait(self, link_description):
        element = ''
        timeout_counter = 0
        while not element and timeout_counter <= 60:
            timeout_counter += 1
            time.sleep(2)
            try:
                element = self.driver.find_element_by_link_text(link_description)
            except Exception:
                continue
        return element

    def go_to_url(self, go_to_url):
        self.driver.get(go_to_url)

    def close_browser(self):
        self.driver.quit()
