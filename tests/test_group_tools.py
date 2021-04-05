from io import StringIO
import os.path
import glob
import shutil
import pytest

# Application Created Code
from scrape.group_tools import GroupTools
from scrape.group_tools import BrowserTools
from scrape.group_tools import SystemTools

#############
# Tests group_tools.py
#############

system_tools = SystemTools()
success_test_page = ("file://" + os.getcwd() + "/tests/test_webpages/test_group_tools/test_success_page_group_tools.html")
fail_test_page = ("file://" + os.getcwd() + "/tests/test_webpages/test_group_tools/test_fail_page_group_tools.html")
back_page = "back"
test_local_groups_file = "multi_group_test"
test_local_groups_path = "tests/test_group_tools/groups_to_join/multi_group_test"
test_groups_to_join = "tests/test_group_tools/groups_to_join/"
test_groups_failed = "tests/test_group_tools/groups_failed/"
test_multi_group_join_responses = iter(['i_dont_exist', 'back'])
test_raw_html_path = "tests/test_group_tools/raw_html_files/"
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
    if not os.path.exists(test_groups_to_join):
                os.makedirs(test_groups_to_join)
    with open(test_local_groups_path, 'w+') as fp:
        fp.write(success_test_page + "\n")
        fp.write(success_test_page + "\n")
        fp.write(fail_test_page + "\n")
    fp.close()
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: test_local_groups_file)
    group_tools.join_multiple_groups_cli(groups_to_join_path=test_groups_to_join,
                                         groups_failed_path=test_groups_failed,
                                         timeout=timeout)
    assert sum(1 for line in open(test_groups_failed + test_local_groups_file, 'r')) == 1
    shutil.rmtree(test_groups_to_join, ignore_errors=True)
    shutil.rmtree(test_groups_failed, ignore_errors=True)


def test_back_join_multiple_groups_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: next(test_multi_group_join_responses))
    assert group_tools.join_multiple_groups_cli(groups_to_join_path=test_groups_to_join) is None
    shutil.rmtree(test_groups_to_join, ignore_errors=True)


def test_join_multiple_groups_gui():
    if not os.path.exists(test_groups_to_join):
                os.makedirs(test_groups_to_join)
    with open(test_local_groups_path, 'w+') as fp:
        fp.write(success_test_page + "\n")
        fp.write(success_test_page + "\n")
        fp.write(fail_test_page + "\n")
    fp.close()
    group_tools = GroupTools()
    group_tools.join_multiple_groups_gui(test_local_groups_file,
                                         groups_to_join_path=test_groups_to_join,
                                         groups_failed_path=test_groups_failed,
                                         timeout=timeout)
    assert sum(1 for line in open(test_groups_failed + test_local_groups_file, 'r')) == 1
    shutil.rmtree(test_groups_to_join, ignore_errors=True)
    shutil.rmtree(test_groups_failed, ignore_errors=True)


def test_bad_file_join_multiple_groups_gui():
    group_tools = GroupTools()
    assert group_tools.join_multiple_groups_gui(test_local_groups_file,
                                                groups_to_join_path=test_groups_to_join,
                                                groups_failed_path=test_groups_failed,
                                                timeout=timeout) is False
    shutil.rmtree(test_groups_to_join, ignore_errors=True)
    shutil.rmtree(test_groups_failed, ignore_errors=True)


def test_save_all_groups_data_cli():
    group_tools = GroupTools()
    group_tools.save_all_groups_data_cli(url=success_test_page,
                                         raw_html_file=test_raw_html_path)
    test_html_files = glob.glob(test_raw_html_path + '*_Group*')
    assert len(test_html_files) == 2
    shutil.rmtree(test_raw_html_path, ignore_errors=True)


def test_save_all_groups_data_gui():
    group_tools = GroupTools()
    group_tools.save_all_groups_data_gui(url=success_test_page,
                                         raw_html_file=test_raw_html_path)
    test_html_files = glob.glob(test_raw_html_path + '*_Group*')
    assert len(test_html_files) == 2
    shutil.rmtree(test_raw_html_path, ignore_errors=True)


def test_save_single_groups_data_cli(monkeypatch):
    group_tools = GroupTools()
    monkeypatch.setattr('builtins.input', lambda _: single_group_name)
    group_tools.save_single_groups_data_cli(url=success_test_page, raw_html_file=test_raw_html_path)
    test_html_files = glob.glob(test_raw_html_path + '*_GroupONE')
    assert len(test_html_files) == 1
    shutil.rmtree(test_raw_html_path, ignore_errors=True)


def test_save_single_groups_data_gui():
    group_tools = GroupTools()
    group_tools.save_single_groups_data_gui(single_group_name, url=success_test_page, raw_html_file=test_raw_html_path)
    test_html_files = glob.glob(test_raw_html_path + '*_GroupONE')
    assert len(test_html_files) == 1
    shutil.rmtree(test_raw_html_path, ignore_errors=True)


def test_remove_group_old_html():
    if not os.path.exists(test_raw_html_path):
                os.makedirs(test_raw_html_path)
    with open(test_raw_html_path + '99999_' + single_group_name, 'w+') as fp:
        fp.write("\n")
    fp.close()
    with open(test_raw_html_path + '00000_' + single_group_name, 'w+') as fp:
        fp.write("\n")
    fp.close()
    group_tools = GroupTools()
    group_tools.save_single_groups_data_gui(single_group_name,
                                         url=success_test_page,
                                         raw_html_file=test_raw_html_path)
    test_html_files = glob.glob(test_raw_html_path + '*_GroupONE')
    assert len(test_html_files) == 1
    shutil.rmtree(test_raw_html_path, ignore_errors=True)


def test_print_groups():
    group_tools = GroupTools()
    assert len(group_tools.print_groups(success_test_page)) == 2
