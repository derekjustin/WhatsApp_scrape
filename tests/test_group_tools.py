from io import StringIO
import os.path

#### Application Code ###########
from scrape.group_tools import GroupTools
from scrape.group_tools import BrowserTools

#############
# Tests group_tools.py
#############

test_page = ("file://" + os.getcwd() + "/tests/test_webpages/mock_WhatsApp.html")

def test__init__():
    group_tools = GroupTools()
    browser_type = BrowserTools()
    assert type(group_tools.browser) == type(browser_type)
    assert type(group_tools.group_elements) == list and len(group_tools.group_elements) == 0
    assert type(group_tools.group_list) == list and len(group_tools.group_list) == 0

"""
def test_join_group(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('sys.stdin', test_page)
    group_tools.join_group()

    #href="https://chat.whatsapp.com/invite/El9vG0AQn1AAXPsG73ueTI" 
"""

def test_get_group_list():
    group_tools = GroupTools()
    group_tools.browser.open_browser()
    group_tools.browser.go_to_url(test_page)
    assert len(group_tools.get_group_list()) == 16
    group_tools.browser.close_browser()
