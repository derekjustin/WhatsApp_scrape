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
    gui.make_home_menu()
    
