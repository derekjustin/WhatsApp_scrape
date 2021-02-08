import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#Application Created Code
from scrape.system_tools import SystemTools

class BrowserTools:
    #############
    # Class to use the selenium library to navigate the
    #    Google Chrome Browser
    #############

      def __init__(self):
           
           #Setup the selenium drivers
           system_tools = SystemTools()
           self.options = webdriver.ChromeOptions()
           self.options.add_argument("user-data-dir=" + system_tools.get_chrome_config_path() )
           self.executable_path = system_tools.get_cwd_path() + '/scrape/browser_driver/chromedriver'

           #self.driver = webdriver.Chrome(executable_path= system_tools.get_cwd_path() + '/scrape/browser_driver/chromedriver', chrome_options=options)

      def open_browser(self):
           self.driver = webdriver.Chrome(executable_path= self.executable_path, chrome_options=self.options)


      def go_to_url(self, go_to_url):
           #############
           # Open up the browser and navigate to Url 
           #
           # Parameters
           # -----------
           # goToUrl : string
           #           the url the user wants the browser to open 
           #############
           self.driver.get(go_to_url)
      
      def close(self):
           #############
           # Close the Google Chrome Browser 
           #############
           self.driver.quit()


