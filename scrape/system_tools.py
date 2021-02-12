from appdirs import *
import platform

class SystemTools:
     #############
     # Class to manage file pathing for cross platforms
     ############# 
     def __init__(self):
           
          #Get the OS 
          self.platform_os =  platform.system()
          
          # Find where Chrome stores the users Google Account on a given OS
          if (self.platform_os == "Darwin"):
              app_name                = "Google/Chrome"
              app_author              = "Google"
          elif(self.platform_os == "Linux"):    
              app_name                = "google-chrome"
              app_author              = "Google"
          elif(self.platform_os != "Linux" or self.platform_os == "Darwin"):
              print("Could not Find a Usable Operating System, Please Retry or Ubuntu or MacOS")
              exit()
          #Use appdirs library to find the users Chrome Account
          self.config_path         = user_config_dir(app_name , app_author)
          print("Looking for users Google Account account at " + self.config_path ) 
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

     def get_sys_platform():
          return self.platform_os

#testing = "a dog walks tall"
#testing = testing.replace(' ' , '\ ')
#print(testing)

#test = SystemTools()  
#print(test.get_chrome_config_path())

#import platform
#print(platform.system())
#print(os.name)
#print(sys.platform)


