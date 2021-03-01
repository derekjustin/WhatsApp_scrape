from scrape.whats_scrape_GUI import WhatsScrapeGUI
import time


def main():
    gui = WhatsScrapeGUI()

    while True:
        window = gui.make_home_menu()
        event, values = window.read()

        if event == 'Quit':
            window.close()
            exit(0)
        elif event == "Print Groups":
            window = gui.make_print_groups_screen(window)
            event, values = window.read()
            if event == 'Return':
                window.close()
                window = gui.make_home_menu()
        elif event == "Join Group":
            window = gui.make_join_group_screen(window)
            event, values = window.read()
            if event == 'Return':
                window.close()
                window = gui.make_home_menu()
        else:
            print("Im nothing")
