from io import StringIO
import os.path

# Application Created Code
from scrape.group_tools import GroupTools
from scrape.group_tools import BrowserTools

#############
# Tests group_tools.py
#############

success_test_page = ("file://" + os.getcwd() + "/tests/test_webpages/test_group_tools/test_success_page_group_tools.html")
fail_test_page = ("file://" + os.getcwd() + "/tests/test_webpages/test_group_tools/test_fail_page_group_tools.html")
back_page = "back"
test_local_groups_file = "test_local_group"
timeout = 4


def test__init__():
    group_tools = GroupTools()
    browser_type = BrowserTools()
    assert type(group_tools.browser) == type(browser_type)
    assert type(group_tools.group_elements) == list and len(group_tools.group_elements) == 0
    assert type(group_tools.group_list) == list and len(group_tools.group_list) == 0

def test_success_join_group_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: success_test_page)
    assert group_tools.join_group_cli() == True

def test_fail_join_group_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: fail_test_page)
    assert group_tools.join_group_cli(timeout) == False

def test_back_join_group_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: back_page)
    assert group_tools.join_group_cli() == None

def test_success_join_multiple_groups_cli(monkeypatch):
    try:
        if not os.path.exists('scrape/group_files/groups_to_join'):
            os.makedirs('scrape/group_files/groups_to_join')
        if not os.path.exists('scrape/group_files/groups_failed'):
            os.makedirs('scrape/group_files/groups_failed')
    except Exception:
        return
    with open("scrape/group_files/groups_to_join/" + test_local_groups_file, 'w+') as fp:
        fp.write(success_test_page + "\n")
        fp.write(success_test_page + "\n")
        fp.write(fail_test_page + "\n")
    fp.close()
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: test_local_groups_file)
    group_tools.join_multiple_groups_cli(timeout)
    assert sum(1 for line in open("scrape/group_files/groups_failed/" + test_local_groups_file, 'r')) == 1
    os.remove(os.getcwd() + "/scrape/group_files/groups_to_join/" + test_local_groups_file)
    os.remove(os.getcwd() + "/scrape/group_files/groups_failed/" + test_local_groups_file)

def test_back_join_multiple_groups_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: back_page)
    assert group_tools.join_multiple_groups_cli() == None


"""
def test_get_group_list():
    group_tools = GroupTools()
    #group_tools.browser.open_browser()
    #group_tools.browser.go_to_url(test_page)
    assert len(group_tools.get_group_list(test_page)) == 16
    group_tools.browser.close_browser()
"""
