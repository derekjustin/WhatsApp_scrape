from scrape.whats_scrape_GUI import WhatsScrapeGUI
from scrape.group_tools import GroupTools

#############
# Tests Whats scrape GUI
############


def test_init():
    gui = WhatsScrapeGUI()
    group_type = GroupTools()
    assert type(gui.group_tools) == type(group_type)


def test_make_home_menu():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    join_group = window.Element(key='-JOIN_GROUP-', silent_on_error=True)
    join_multi_group = window.Element(key='-JOIN_MULTI_GROUP-', silent_on_error=True)
    all_groups = window.Element(key='-ALL_GROUPS-', silent_on_error=True)
    single_group = window.Element(key='-SINGLE_GROUP-', silent_on_error=True)
    print_groups = window.Element(key='-PRINT_GROUPS-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    assert join_group.Key == '-JOIN_GROUP-'
    assert join_multi_group.Key == '-JOIN_MULTI_GROUP-'
    assert all_groups.Key == '-ALL_GROUPS-'
    assert single_group.Key == '-SINGLE_GROUP-'
    assert print_groups.Key == '-PRINT_GROUPS-'
    assert quiter.Key == '-QUITER-'
    window.close()


def test_make_print_groups_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_print_groups_screen(window)
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    output_1 = window.Element(key='-OUTPUT_1-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert output_1.Key == '-OUTPUT_1-'
    assert quiter.Key == '-QUITER-'
    window.close()


def test_make_join_group_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_join_group_screen(window)
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    input_1 = window.Element(key='-INPUT_1-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert input_1.Key == '-INPUT_1-'
    assert quiter.Key == '-QUITER-'
    window.close()


def test_make_group_failure_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_group_failure_screen(window, "I FAILED")
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    message_3 = window.Element(key='-MESSAGE_3-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    assert message_3.Key == '-MESSAGE_3-'
    assert quiter.Key == '-QUITER-'
    window.close()


def test_make_group_success_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_group_success_screen(window, "I SUCCEEDED")
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    assert quiter.Key == '-QUITER-'
    window.close()


def test_make_join_multiple_groups_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_join_multiple_groups_screen(window)
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    submit = window.Element(key='-SUBMIT-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    assert quiter.Key == '-QUITER-'
    assert submit.Key == '-SUBMIT-'
    window.close()


def test_make_multiple_group_failure_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_multiple_group_failure_screen(window, "I FAILED")
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    message_3 = window.Element(key='-MESSAGE_3-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    assert message_3.Key == '-MESSAGE_3-'
    assert quiter.Key == '-QUITER-'
    window.close()


def test_make_multiple_group_success_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_multiple_group_success_screen(window, "I SUCCEEDED")
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    message_3 = window.Element(key='-MESSAGE_3-', silent_on_error=True)
    output_1 = window.Element(key='-OUTPUT_1-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    assert message_3.Key == '-MESSAGE_3-'
    assert output_1.Key == '-OUTPUT_1-'
    assert quiter.Key == '-QUITER-'
    window.close()


def test_make_save_all_groups_data_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_save_all_groups_data_screen(window)
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    window.close()


def test_make_save_single_group_data_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_save_single_group_data_screen(window)
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    submit = window.Element(key='-SUBMIT-', silent_on_error=True)    
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    assert quiter.Key == '-QUITER-'
    assert submit.Key == '-SUBMIT-'
    window.close()


def test_make_save_group_data_fail_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_save_group_data_fail_screen(window)
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    assert quiter.Key == '-QUITER-'
    window.close()


def test_make_save_group_data_success_screen():
    gui = WhatsScrapeGUI()
    window = gui.make_home_menu()
    window = gui.make_save_group_data_success_screen(window)
    message_1 = window.Element(key='-MESSAGE_1-', silent_on_error=True)
    message_2 = window.Element(key='-MESSAGE_2-', silent_on_error=True)
    quiter = window.Element(key='-QUITER-', silent_on_error=True)
    assert message_1.Key == '-MESSAGE_1-'
    assert message_2.Key == '-MESSAGE_2-'
    assert quiter.Key == '-QUITER-'
    window.close()
