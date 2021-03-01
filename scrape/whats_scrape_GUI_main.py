from scrape.whats_scrape_GUI import WhatsScrapeGUI
from scrape.group_tools import GroupTools
import time


def main():
    gui = WhatsScrapeGUI()
    group_tools = GroupTools()


    while True:
        window = gui.make_home_menu()
        event, values = window.read()

        if event == 'Quit':
            window.close()
            exit(0)
        elif event == 'Print Groups':
            window = gui.make_print_groups_screen(window)
            event, values = window.read()
            if event == 'Return':
                window.close()
                window = gui.make_home_menu()
        elif event == 'Join Group':
            window = gui.make_join_group_screen(window)
            event, values = window.read()
            if event == 'Return':
                window.close()
                window = gui.make_home_menu()
            elif event == 'Submit':
                if group_tools.join_group_gui(values[0]) is False:
                    window = gui.make_group_failure_screen(window, values[0])
                    event, values = window.read()
                    if event == 'Return':
                        window.close()
                        window = gui.make_home_menu()
                else:
                    window = gui.make_group_success_screen(window, values[0])
                    event, values = window.read()
                    if event == 'Return':
                        window.close()
                        window = gui.make_home_menu()
        elif event == 'Join Multiple Groups':
            window = gui.make_join_multiple_groups_screen(window)
            event, values = window.read()
            if event == 'Return':
                window.close()
                window = gui.make_home_menu()
            elif event == 'Submit':
                if group_tools.join_multiple_groups_gui(values[0]) is False:
                    window = gui.make_multiple_group_failure_screen(window, values[0])
                    event, values = window.read()
                    if event == 'Return':
                        window.close()
                        window = gui.make_home_menu()
                else:
                    window = gui.make_multiple_group_success_screen(window, values[0])
                    event, values = window.read()
                    if event == 'Return':
                        window.close()
                        window = gui.make_home_menu()
        else:
            print("Im nothing")
