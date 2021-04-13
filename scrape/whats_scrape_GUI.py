import PySimpleGUI as sg

from scrape.group_tools import GroupTools


class WhatsScrapeGUI:

    def __init__(self):
        self.group_tools = GroupTools()

    def make_home_menu(self):
        layout = [
            [sg.Column([[sg.Text('Welcome to the WhatsApp Web Scraping Tool', key='-MESSAGE_1-', font=['Comic', 30, 'bold'], text_color='#ffffff', background_color='#2e9688')]], background_color='#2e9688')],
            [sg.Column([[sg.Text('Please Choose One Of The Following Options!', key='-MESSAGE_2-', font=['Comic', 20, 'bold'], text_color='#000000', background_color='#d8dbd4')]], background_color='#d8dbd4', justification='center', pad=(50, 50))],
            [sg.Column([[sg.Button('Join Group', key='-JOIN_GROUP-'),
                         sg.Button('Join Multiple Groups', key='-JOIN_MULTI_GROUP-'),
                         sg.Button('Save All Groups Data', key='-ALL_GROUPS-'),
                         sg.Button('Save Single Group Data', key='-SINGLE_GROUP-'),
                         sg.Button('Print Groups', key='-PRINT_GROUPS-'),
                         sg.Button('Quit', key='-QUITER-')]], background_color='#d8dbd4', justification='center')]]
        return sg.Window('Window Title', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_print_groups_screen(self, calling_window):
        group_list = self.group_tools.get_group_list()
        group_text = ""
        for group in group_list:
            group_text += (group + "\n")
        layout = [
            [sg.Column([[sg.Text('Your Joined Group List', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], background_color='#2e9688')],
            [sg.Column([[sg.Multiline(default_text=group_text, key='-OUTPUT_1-', auto_size_text=True, size=(20, 30))]])],
            [sg.Column([[sg.Button('Return', key='-QUITER-')]], background_color='#d8dbd4', justification='center')]]
        calling_window.close()
        return sg.Window('Printed Groups', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_join_group_screen(self, calling_window):
        layout = [
            [sg.Column([[sg.Text('JOIN A GROUP', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Text('Please provide a group link to join: ', key='-INPUT_1-', size=(30, 1), background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000'), sg.InputText()],
            [sg.Column([[sg.Button('Return', key='-QUITER-'), sg.Button('Submit', key='-SUBMIT-')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('JOIN A GROUP', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_group_failure_screen(self, calling_window, group_link):
        layout = [
            [sg.Column([[sg.Text('GROUP FAIL NOTIFICATION', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Column([[sg.Text('This group link FAILED: "' + group_link + '"', key='-MESSAGE_2-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')],
            [sg.Column([[sg.Text('Please ensure the link is valid.', key='-MESSAGE_3-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')],
            [sg.Column([[sg.Button('Return', key='-QUITER-')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('GROUP FAIL', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_group_success_screen(self, calling_window, group_link):
        layout = [
            [sg.Column([[sg.Text('GROUP SUCCESS NOTIFICATION', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Column([[sg.Text('This group link SUCCEEDED: "' + group_link + '"', key='-MESSAGE_2-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')],
            [sg.Column([[sg.Button('Return', key='-QUITER-')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('GROUP SUCCESS', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_join_multiple_groups_screen(self, calling_window):
        layout = [
            [sg.Column([[sg.Text('JOIN MULTIPLE GROUPS', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Text('Please provide a filename in the "/scrape/group_files/groups_to_join/" directory: ', key='-MESSAGE_2-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000'), sg.InputText()],
            [sg.Column([[sg.Button('Return', key='-QUITER-'), sg.Button('Submit', key='-SUBMIT-')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('JOIN MULTIPLE GROUPS', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_multiple_group_failure_screen(self, calling_window, file_name):
        layout = [
            [sg.Column([[sg.Text('GROUP FAIL NOTIFICATION', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Column([[sg.Text('This group file FAILED: "' + file_name + '"', key='-MESSAGE_2-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')],
            [sg.Column([[sg.Text('Please ensure the file exists.', key='-MESSAGE_3-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')],
            [sg.Column([[sg.Button('Return', key='-QUITER-')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('GROUP FAIL', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_multiple_group_success_screen(self, calling_window, file_name):
        failed_group_text = self.__get_failed_group_list(file_name)
        layout = [
            [sg.Column([[sg.Text('GROUP SUCCESS NOTIFICATION', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Column([[sg.Text('This group file SUCCEEDED: "' + file_name + '"', key='-MESSAGE_2-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')],
            [sg.Column([[sg.Text('Group links in the TEXT box below FAILED:', key='-MESSAGE_3-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')],
            [sg.Column([[sg.Multiline(default_text=failed_group_text, key='-OUTPUT_1-', auto_size_text=True, size=(70, 30))]])],
            [sg.Column([[sg.Button('Return', key='-QUITER-')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('GROUP FAIL', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_save_all_groups_data_screen(self, calling_window):
        layout = [
            [sg.Column([[sg.Text('SAVING ALL GROUPS DATA: *** PLEASE WAIT ***', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Column([[sg.Text('\tPLEASE WAIT for proccess to finish.\nYou will recieve a success response message when completed.', key='-MESSAGE_2-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('SAVING ALL GROUPS DATA', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_save_single_group_data_screen(self, calling_window):
        layout = [
            [sg.Column([[sg.Text('SAVE SINGLE GROUPS DATA', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Text('Please provide WhatsApp Web GROUP NAME: ', key='-MESSAGE_2-', size=(38, 1), background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000'), sg.InputText()],
            [sg.Column([[sg.Button('Return', key='-QUITER-'), sg.Button('Submit', key='-SUBMIT-')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('SAVING ALL GROUPS DATA', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_save_group_data_fail_screen(self, calling_window):
        layout = [
            [sg.Column([[sg.Text('SAVE GROUP(S) DATA FAIL NOTIFICATION', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Column([[sg.Text('Please ensure you have a secure internet connection\nand your WhatsApp Web account is signed in.', key='-MESSAGE_2-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')],
            [sg.Column([[sg.Button('Return', key='-QUITER-')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('SAVE GROUP(S) DATA FAIL NOTIFICATION', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

    def make_save_group_data_success_screen(self, calling_window):
        layout = [
            [sg.Column([[sg.Text('SAVE GROUP(S) DATA SUCCESS NOTIFICATION', key='-MESSAGE_1-', font=['Comic', 20, 'bold'], text_color='#ffffff', background_color='#2e9688')]], justification='center')],
            [sg.Column([[sg.Text('All your group data has been saved SUCCESSFULLY!', key='-MESSAGE_2-', background_color='#d8dbd4', font=['Comic', 12, 'bold'], text_color='#000000')]], background_color='#d8dbd4', justification='center')],
            [sg.Column([[sg.Button('Return', key='-QUITER-')]], background_color='#d8dbd4', justification='center')]
        ]
        calling_window.close()
        return sg.Window('SAVE GROUP(S) DATA SUCCESS NOTIFICATION', layout=layout, background_color='#d8dbd4', button_color=['#000000', '#2e9688'], margins=[0, 0])

# *************** PRIVATE FUNCTIONS ***************************

    def __get_failed_group_list(self, file_name):
        failed_group_text = ""
        with open("scrape/group_files/groups_failed/" + file_name, 'r') as failed_group_file:
            while True:
                failed_link = failed_group_file.readline()
                if not failed_link:
                    break
                else:
                    failed_group_text += (failed_link + "\n")
            failed_group_file.close()
        return failed_group_text
