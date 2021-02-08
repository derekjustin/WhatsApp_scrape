from appdirs import *


class systemTools:
     #############
     # Class to manage file pathing for cross platforms
     ############# 
     def __init__(self):
           
          #appdirs will get the Google Chrome .config file across platforms
          appname                = "google-chrome"
          appauthor              = "Google"
          self.configPath        = user_config_dir(appname , appauthor)

          self.currentWorkingDir = os.getcwd()

     def getChromeConfigPath(self):
            #############
            # Get the path of the .config for Google Chrome App
            #
            # Returns
            # -----------
            # configPath : string
            #           The configuration path of the Google
            #             Chrome App
            #############
            return self.configPath

     def getCwdPath(self):
            #############
            # Get the WhatsApp_scrape working directory
            #
            # Returns
            # -----------
            # currentWorkingDir : string
            #           The path of the working directory of the 
            #             WhatsApp_scrape Application
            #############
          return self.currentWorkingDir
