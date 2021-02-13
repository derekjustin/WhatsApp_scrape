from selenium import webdriver

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

def test_open_browser():
    browser_tools = BrowserTools()
    browser_tools.open_browser()
    browser = browser_tools.driver
    browser_tools.close_browser()
    assert type(browser) ==  webdriver.chrome.webdriver.WebDriver

def test_check_browser_status():
    browser_tools = BrowserTools()
    browser_tools.open_browser()
    alive_status = browser_tools.check_browser_status()
    browser_tools.close_browser()
    assert alive_status == "Alive"
    assert browser_tools.check_browser_status() == "Dead"

def test_browser_find_element_by_xpath_with_wait():
    browser_tools = BrowserTools()
    browser_tools.open_browser()
    browser_tools.go_to_url("https://google.com")
    found_element = browser_tools.browser_find_element_by_xpath_with_wait("//input[@value='Google Search']")
    browser_tools.close_browser()
    assert type(found_element) == webdriver.remote.webelement.WebElement

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
    assert browser_tools.check_browser_status() == "Dead"

