from appdirs import *


class SystemTools:
     #############
     # Class to manage file pathing for cross platforms
     ############# 
     def __init__(self):
           
          #appdirs will get the Google Chrome .config file across platforms
          app_name                = "google-chrome"
          app_author              = "Google"
          self.config_path        = user_config_dir(app_name , app_author)

          self.current_working_dir = os.getcwd()

     def get_chrome_config_path(self):
            #############
            # Get the path of the .config for Google Chrome App
            #
            # Returns
            # -----------
            # configPath : string
            #           The configuration path of the Google
            #             Chrome App
            #############
            return self.config_path

     def get_cwd_path(self):
            #############
            # Get the WhatsApp_scrape working directory
            #
            # Returns
            # -----------
            # currentWorkingDir : string
            #           The path of the working directory of the 
            #             WhatsApp_scrape Application
            #############
          return self.current_working_dir
