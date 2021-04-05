import os.path

from scrape.group_tools_main import main

############
# Tests group_tools_main.py
############

success_test_page = ("file://" + os.getcwd() + "/tests/test_webpages/test_group_tools/test_success_page_group_tools.html")
back_page = "back"

join_group_responses = iter(['join_group', back_page, back_page])
join_multiple_group_responses = iter(['join_multiple_groups', back_page, back_page])
single_group_data_responses = iter(['single_group_data', back_page, back_page])
all_groups_data_responses = iter(['all_groups_data', back_page])
print_groups_responses = iter(['print_groups', back_page])
invalid_input_responses = iter(['im_not_valid', back_page])


def test_main_join_group(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda msg: next(join_group_responses))
    assert main() == "join_group"


def test_main_join_multiple_groups(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda msg: next(join_multiple_group_responses))
    assert main() == "join_multiple_groups"


def test_main_single_group_data(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda msg: next(single_group_data_responses))
    assert main() == "single_group_data"


def test_main_all_groups_data(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda msg: next(all_groups_data_responses))
    assert main(True) == "all_groups_data"


def test_main_print_groups(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda msg: next(print_groups_responses))
    assert main() == "print_groups"


def test_main_invalid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda msg: next(invalid_input_responses))
    assert main() == "invalid_input"
