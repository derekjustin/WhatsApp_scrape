import pandas as pd

from scrape.whats_scrape_GUI import WhatsScrapeGUI
from scrape.group_tools import GroupTools
from scrape.scrape_html import MultiProcessHtml
from scrape.system_tools import SystemTools
import time


def main():
    gui = WhatsScrapeGUI()
    group_tools = GroupTools()
    scrape = MultiProcessHtml()
    system = SystemTools()

    while True:
        window = gui.make_home_menu()
        event, values = window.read()

        if event == '-QUITER-':
            window.close()
            exit(0)
        elif event == '-PRINT_GROUPS-':
            window = gui.make_print_groups_screen(window)
            event, values = window.read()
            if event == '-QUITER-':
                window.close()
                window = gui.make_home_menu()
        elif event == '-JOIN_GROUP-':
            window = gui.make_join_group_screen(window)
            event, values = window.read()
            if event == '-QUITER-':
                window.close()
                window = gui.make_home_menu()
            elif event == '-SUBMIT-':
                if group_tools.join_group_gui(values[0]) is False:
                    window = gui.make_group_failure_screen(window, values[0])
                    event, values = window.read()
                    if event == '-QUITER-':
                        window.close()
                        window = gui.make_home_menu()
                else:
                    window = gui.make_group_success_screen(window, values[0])
                    event, values = window.read()
                    if event == '-QUITER-':
                        window.close()
                        window = gui.make_home_menu()
        elif event == '-JOIN_MULTI_GROUP-':
            window = gui.make_join_multiple_groups_screen(window)
            event, values = window.read()
            if event == '-QUITER-':
                window.close()
                window = gui.make_home_menu()
            elif event == '-SUBMIT-':
                if group_tools.join_multiple_groups_gui(values[0]) is False:
                    window = gui.make_multiple_group_failure_screen(window, values[0])
                    event, values = window.read()
                    if event == '-QUITER-':
                        window.close()
                        window = gui.make_home_menu()
                else:
                    window = gui.make_multiple_group_success_screen(window, values[0])
                    event, values = window.read()
                    if event == '-QUITER-':
                        window.close()
                        window = gui.make_home_menu()
        elif event == '-ALL_GROUPS-':
            window = gui.make_save_all_groups_data_screen(window)
            window.finalize()
            if group_tools.save_all_groups_data_gui() is False:
                window = gui.make_save_group_data_fail_screen(window)
                event, values = window.read()
                if event == '-QUITER-':
                    window.close()
                    window = gui.make_home_menu()
            else:
                window = gui.make_save_group_data_success_screen(window)
                event, values = window.read()
                if event == '-QUITER-':
                    window.close()
                    window = gui.make_home_menu()
        elif event == '-SINGLE_GROUP-':
            window = gui.make_save_single_group_data_screen(window)
            event, values = window.read()
            if event == '-QUITER-':
                window.close()
                window = gui.make_home_menu()
            elif event == '-SUBMIT-':
                if group_tools.save_single_groups_data_gui(values[0]) is False:
                    window = gui.make_group_failure_screen(window, values[0])
                    event, values = window.read()
                    if event == '-QUITER-':
                        window.close()
                        window = gui.make_home_menu()
                else:
                    window = gui.make_save_group_data_success_screen(window)
                    event, values = window.read()
                    if event == '-QUITER-':
                        window.close()
                        window = gui.make_home_menu()
        elif event == '-GENERATE_CSV-':
            df = pd.DataFrame()
            df = scrape.get_message_frame_all_groups(system.get_processed_pck_list())
            scrape.generate_message_summary_csv(df)
            window = gui.make_generate_csv_screen(window)
            event, values = window.read()
            if event == '-QUITER-':
                window.close()
                window = gui.make_home_menu()
        else:
            quit()
