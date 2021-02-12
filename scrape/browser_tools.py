import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.command import Command

from webdriver_manager.chrome import ChromeDriverManager

#Application Created Code
from scrape.system_tools import SystemTools

class BrowserTools:
    #############
    # Class to use the selenium library to navigate the
    #    Google Chrome Browser
    #############

      def __init__(self):
           #Setup the selenium drivers
           self.system_tools = SystemTools()
           self.options = webdriver.ChromeOptions()
           self.options.add_argument("user-data-dir=" + self.system_tools.get_chrome_config_path())
       #    self.executable_path = self.system_tools.get_cwd_path() + "/scrape/browser_driver/chromedriver"
#           self.executable_path = self.system_tools.get_cwd_path() + "/scrape/browser_driver/chromedriver_2"
           self.executable_path = ChromeDriverManager().install()

      def open_browser(self):
           self.driver = webdriver.Chrome(executable_path= self.executable_path, options=self.options)
         #  self.driver = webdriver.Chrome(ChromeDriverManager().install())

      def check_browser_status(self):
           try:
                self.driver.execute(Command.STATUS)
                return "Alive"
           except:
                return "Dead"
     
      def browser_find_element_by_xpath_with_wait(self, element_description):
           element = ''
           timeout_counter = 0
           while not element and timeout_counter <= 60:
                timeout_counter += 1
                time.sleep(2)
                try:
                     element = self.driver.find_element_by_xpath(element_description)
                except:
                     continue
           return element

      def browser_find_element_by_link_text_with_wait(self, link_description):
           element = ''
           timeout_counter = 0
           while not element and timeout_counter <= 60:
                timeout_counter += 1
                time.sleep(2)
                try:
                     element = self.driver.find_element_by_link_text(link_description)
                except:
                     continue
           return element           
           
      def go_to_url(self, go_to_url):
           self.driver.get(go_to_url)
      
      def close_browser(self):
           self.driver.quit()

