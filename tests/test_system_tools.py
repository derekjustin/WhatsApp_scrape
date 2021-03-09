from appdirs import *
from scrape.system_tools import SystemTools
import os.path
import platform
import pytest

#############
# Tests the system_tools.py and relative pathing
#    that must exist for the Google Chrome Driver
#############


def test_get_cwd_path():
    system_tools = SystemTools()
    assert system_tools.get_cwd_path() == os.getcwd()


def test_chrome_config_path_MacOs():
    system_tools = SystemTools('Darwin')
    if(system_tools.platform_os == "Darwin"):
        app_name = "Google/Chrome"
        app_author = "Google"
    assert system_tools.get_chrome_config_path() == user_config_dir(app_name, app_author)
    assert system_tools.app_name == app_name
    assert system_tools.app_author == app_author


def test_chrome_config_path_Linux():
    system_tools = SystemTools('Linux')
    if(system_tools.platform_os == "Linux"):
        app_name = "google-chrome"
        app_author = "Google"
    assert system_tools.get_chrome_config_path() == user_config_dir(app_name, app_author)
    assert system_tools.app_name == app_name
    assert system_tools.app_author == app_author


def test_chrome_config_exception():
    with pytest.raises(Exception):
        system_tools = SystemTools('invalid_os')


def test_platform():
    system_tools = SystemTools()
    system_platform = system_tools.get_sys_platform()
    platform_os = platform.system()
    assert system_platform == platform_os


def test_get_html_dir_path():
    system_tools = SystemTools()
    system_html_dir_path = system_tools.get_html_dir_path()
    html_dir_path = os.getcwd() + '/scrape/group_files/raw_html_files'
    assert system_html_dir_path == html_dir_path


def test_get_raw_html_list():
    system_tools = SystemTools()
    system_raw_html_list = system_tools.get_raw_html_list()
    html_dir_path = os.getcwd() + '/scrape/group_files/raw_html_files'
    test_list = os.listdir(html_dir_path)
    assert system_raw_html_list == test_list


def test_get_processed_html_pickles_dir():
    system_tools = SystemTools()
    system_processed_html_pickles_dir = system_tools.get_processed_html_pickles_dir()
    processed_html_dir_path = os.getcwd() + '/scrape/group_files/processed_html_pickles'
    assert system_processed_html_pickles_dir == processed_html_dir_path


def test_get_os_platform():
    system_tools = SystemTools()
    platform_system = system_tools.get_os_platform()
    if platform_system != 'Darwin' and platform_system != 'Linux':
        assert False
    assert True
