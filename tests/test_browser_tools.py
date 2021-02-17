from selenium import webdriver
from selenium.webdriver.remote.command import Command

#### Application Code ###########
from scrape.browser_tools import BrowserTools
from scrape.system_tools import SystemTools

#############
# Tests browser_tools.py
#############

def test__init__():
    browser_tools = BrowserTools()
    system_type = SystemTools()
    assert type(browser_tools.system_tools) == type(system_type) 
    assert type(browser_tools.options) == webdriver.chrome.options.Options 

def test_init_browser():
    browser_tools = BrowserTools()
    browser_tools.init_browser()
    browser_tools.close_browser()
    assert type(browser_tools.driver) ==  webdriver.chrome.webdriver.WebDriver

def test_open_browser():
    browser_tools = BrowserTools()
    browser_tools.open_browser()
    url = browser_tools.driver.current_url
    browser_tools.close_browser()
    assert url ==  "chrome://new-tab-page/"

def test_browser_find_element_by_xpath_with_wait():
    browser_tools = BrowserTools()
    browser_tools.open_browser()
    browser_tools.go_to_url("https://google.com")
    found_element = browser_tools.browser_find_element_by_xpath_with_wait("//input[@value='Google Search']")
    browser_tools.close_browser()
    assert type(found_element) == webdriver.remote.webelement.WebElement

def test_browser_find_multiple_elements_by_xpath_with_wait():
    browser_tools = BrowserTools()
    browser_tools.open_browser()
    browser_tools.go_to_url("https://google.com")
    found_elements = browser_tools.browser_find_multiple_elements_by_xpath_with_wait("//a[@class='MV3Tnb']")
    browser_tools.close_browser()
    assert len(found_elements) == 2


def test_browser_find_element_by_link_text_with_wait():
    browser_tools = BrowserTools()
    browser_tools.open_browser()
    browser_tools.go_to_url("https://google.com")
    found_element = browser_tools.browser_find_element_by_link_text_with_wait("About")
    browser_tools.close_browser()
    assert type(found_element) == webdriver.remote.webelement.WebElement

def test_browser_go_to_url():
    browser_tools = BrowserTools()
    browser_tools.open_browser()
    browser_tools.go_to_url("https://www.google.com/")
    current_url = browser_tools.driver.current_url
    browser_tools.close_browser()
    assert current_url == "https://www.google.com/"

def test_close_browser():
    browser_tools = BrowserTools()
    browser_tools.open_browser()
    browser_tools.close_browser()
    try:
        assert browser_tools.driver.execute(Command.STATUS) == True
        return True
    except:
        return False
