from bs4 import BeautifulSoup
from datetime import datetime
import os
import pandas as pd
from scrape.system_tools import SystemTools


class WhatsAppHtmlParser:

    def __init__(self, html_file_path):
        with open(html_file_path, 'r') as f:
            contents = f.read()
        self.soup = BeautifulSoup(contents, 'html.parser')

    def get_messages_pd_frame(self):
        df = pd.DataFrame(columns=['date_time', 'author', 'message'])
        for tag in self.soup.find_all('div'):
            currentDict = tag.attrs
            if "class" in currentDict:
                if self.__search(currentDict, 'copyable-text'):
                    if (len(currentDict) <= 2 and 'data-pre-plain-text' in currentDict):
                        theFinalDict = currentDict
                        dateNameString = theFinalDict["data-pre-plain-text"]
                        timestamp = self.__find_between(dateNameString, "[", "]")
                        datetime_object = datetime.strptime(timestamp, '%I:%M %p, %m/%d/%Y')
                        msgAuthor = self.__find_between(dateNameString, "] ", ":")
                        df = df.append({'date_time': datetime_object, 'author': msgAuthor, 'message': tag.text}, ignore_index=True)
        df = df.set_index('date_time')
        return df

    def save_pd_frame_to_pickle(self, df, file_name, dest_folder):
        df.to_pickle(dest_folder + "/" + file_name + ".pkl")

    def __find_between(self, s, first, last):
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]

    def __search(self, values, searchFor):
        for k in values:
            for v in values[k]:
                if searchFor in v:
                    return k
        return None


class MultiProcessHtml:
    sys_tools = SystemTools()

    def process_all_raw_html_to_pickles(self, raw_html_list=sys_tools.get_raw_html_list(), html_pickle_dir=sys_tools.get_processed_html_pickles_dir(), html_dir_path=sys_tools.get_html_dir_path()):
        if not os.path.isdir(html_pickle_dir):
            os.mkdir(html_pickle_dir)
        else:
            for root, dirs, files in os.walk(html_pickle_dir):
                for file in files:
                    os.remove(os.path.join(root, file))
        if raw_html_list != []:
            for html_file in raw_html_list:
                html_parser = WhatsAppHtmlParser(html_dir_path + '/' + html_file)
                df = html_parser.get_messages_pd_frame()
                html_parser.save_pd_frame_to_pickle(df, html_file, html_pickle_dir)
        else:
            raise Exception("There are no files to process in " + html_dir_path)

    def get_message_frame_all_groups(self, list_of_pkl=sys_tools.get_processed_pck_list()):
        self.process_all_raw_html_to_pickles()
        df_all = pd.DataFrame()
        for file in list_of_pkl:
            file_base_name = os.path.basename(file)
            size = len(file_base_name)
            file_name = file_base_name[17:size - 4]
            df = pd.read_pickle(file)
            df["group_name"] = file_name
            df_all = df_all.append(df)
        return df_all

    def save_pd_frame_to_csv(self, df, file_name, dest_folder):
        df.to_csv(dest_folder + '/' + file_name + '.csv')

    def generate_message_summary_csv(self, df_all, dest_dir=sys_tools.get_cwd_path()):
        summary_file_name = "whatsApp_groups_message_summary"
        if os.path.exists(dest_dir + summary_file_name):
            os.remove(dest_dir + summary_file_name)
        self.save_pd_frame_to_csv(df_all, summary_file_name, dest_dir)
