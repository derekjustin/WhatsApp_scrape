from appdirs import *
from scrape.system_tools import SystemTools
import os.path

#############
# Tests the system_tools.py and relative pathing 
#    that must exist for the Google Chrome Driver
#############

def test_get_cwd_path():
    system_tools = SystemTools()
    assert system_tools.get_cwd_path() == os.getcwd()

def test_chrome_config_path():
    system_tools = SystemTools()
    app_name     = "google-chrome"
    app_author   = "Google"

    assert system_tools.get_chrome_config_path()  == user_config_dir(app_name , app_author)

def test_driver_dir_exists():
    system_tools = SystemTools()
    assert os.path.isdir(system_tools.get_cwd_path() + '/scrape/browser_driver')

def test_driver_exists():
    system_tools = SystemTools()
    assert os.path.isfile(system_tools.get_cwd_path() + '/scrape/browser_driver/chromedriver')



