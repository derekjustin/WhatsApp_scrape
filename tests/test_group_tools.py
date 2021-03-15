from io import StringIO
import os.path
import glob

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
single_group_name = "GroupONE"


def test__init__():
    group_tools = GroupTools()
    browser_type = BrowserTools()
    assert type(group_tools.browser) == type(browser_type)
    assert type(group_tools.group_elements) == list and len(group_tools.group_elements) == 0
    assert type(group_tools.group_list) == list and len(group_tools.group_list) == 0


def test_success_join_group_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: success_test_page)
    assert group_tools.join_group_cli() is True


def test_fail_join_group_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: fail_test_page)
    assert group_tools.join_group_cli(timeout) is False


def test_back_join_group_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: back_page)
    assert group_tools.join_group_cli() is None


def test_join_group_gui():
    group_tools = GroupTools()
    assert group_tools.join_group_gui(success_test_page) is True


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
    assert group_tools.join_multiple_groups_cli() is None


def test_join_multiple_groups_gui():
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
    group_tools.join_multiple_groups_gui(test_local_groups_file, timeout)
    assert sum(1 for line in open("scrape/group_files/groups_failed/" + test_local_groups_file, 'r')) == 1
    os.remove(os.getcwd() + "/scrape/group_files/groups_to_join/" + test_local_groups_file)
    os.remove(os.getcwd() + "/scrape/group_files/groups_failed/" + test_local_groups_file)


def test_save_all_groups_data_cli():
    group_tools = GroupTools()
    group_tools.save_all_groups_data_cli(success_test_page)
    test_html_files = glob.glob(os.getcwd() + '/scrape/group_files/raw_html_files/*_Group*')
    assert len(test_html_files) == 2
    for file in test_html_files:
        os.remove(file)


def test_save_single_groups_data_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: single_group_name)
    group_tools.save_single_groups_data_cli(success_test_page)
    test_html_files = glob.glob(os.getcwd() + '/scrape/group_files/raw_html_files/*_GroupONE')
    assert len(test_html_files) == 1
    for file in test_html_files:
        os.remove(file)


def test_print_groups():
    group_tools = GroupTools()
    assert len(group_tools.print_groups(success_test_page)) == 2
