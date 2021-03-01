from appdirs import *
from scrape.system_tools import SystemTools
import os.path
import platform

#############
# Tests the system_tools.py and relative pathing
#    that must exist for the Google Chrome Driver
#############


def test_get_cwd_path():
    system_tools = SystemTools()
    assert system_tools.get_cwd_path() == os.getcwd() 


def test_chrome_config_path():
    system_tools = SystemTools()
    if(system_tools.get_sys_platform() == "Darwin"):
        app_name = "Google/Chrome"
        app_author = "Google"
    if(system_tools.get_sys_platform() == "Linux"):
        app_name = "google-chrome"
        app_author = "Google"
    assert system_tools.get_chrome_config_path() == user_config_dir(app_name, app_author)


def test_platform():
    system_tools = SystemTools()
    system_platform = system_tools.get_sys_platform()
    platform_os = platform.system()
    assert system_platform == platform_os
