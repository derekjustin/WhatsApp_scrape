from scrape.scrape_html import WhatsAppHtmlParser, MultiProcessHtml
import os
import platform
import pytest
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import shutil


def test_parser_object():
    whatsApp_parser = WhatsAppHtmlParser(os.getcwd() + '/tests/test_html_parser/test.html')
    with open(os.getcwd() + '/tests/test_html_parser/test.html', 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    assert whatsApp_parser.soup == soup


def test_save_pd_frame_to_pickle():
    if os.path.exists(os.getcwd() + '/tests/test_html_parser/test.pkl'):
        os.remove(os.getcwd() + '/tests/test_html_parser/test.pkl')
    df = pd.DataFrame(columns=['Datetime', 'Author', 'Message'])
    whatsApp_parser = WhatsAppHtmlParser(os.getcwd() + '/tests/test_html_parser/test.html')
    whatsApp_parser.save_pd_frame_to_pickle(df, 'test', os.getcwd() + '/tests/test_html_parser')
    assert os.path.isfile(os.getcwd() + '/tests/test_html_parser/test.pkl')


def test_save_pdFram_to_csv():
    if os.path.exists(os.getcwd() + '/tests/test_html_parser/test.csv'):
        os.remove(os.getcwd() + '/tests/test_html_parser/test.csv')
    df = pd.DataFrame(columns=['Datetime', 'Author', 'Message'])
    multi_process = MultiProcessHtml()
    multi_process.save_pd_frame_to_csv(df, 'test', os.getcwd() + '/tests/test_html_parser')
    assert os.path.isfile(os.getcwd() + '/tests/test_html_parser/test.csv')


def test_get_messages_pd_frame():
    whatsApp_parser = WhatsAppHtmlParser(os.getcwd() + '/tests/test_html_parser/test.html')
    message_frame = whatsApp_parser.get_messages_pd_frame()
    whatsApp_parser.save_pd_frame_to_pickle(message_frame, 'test_message', os.getcwd() + '/tests/test_html_parser')
    data = {'Author': ['Derek', 'Unknown'], 'Message': ['hello this is the derek group', 'Do I know you?']}
    df = pd.DataFrame(data, index=[datetime.datetime(2021, 2, 1, 16, 27, 0), datetime.datetime(2021, 2, 1, 16, 30, 0)])
    assert message_frame.iloc[0, 0] == df.iloc[0, 0]
    assert message_frame.iloc[0, 1] == df.iloc[0, 1]
    assert message_frame.iloc[1, 0] == df.iloc[1, 0]
    assert message_frame.iloc[1, 1] == df.iloc[1, 1]
    assert message_frame.index.values[0] == df.index.values[0]
    assert message_frame.index.values[1] == df.index.values[1]


def test_MultiprocessHtml_process_all_raw_html_to_pickles():
    multi_process_html = MultiProcessHtml()
    test_html_dir = os.getcwd() + '/tests/test_html_parser/test_raw_html'
    multi_process_html.process_all_raw_html_to_pickles(raw_html_list=os.listdir(test_html_dir),
                                                       html_pickle_dir=os.getcwd() + '/tests/test_html_parser/test_pickle_output',
                                                       html_dir_path=test_html_dir)
    assert os.listdir(os.getcwd() + '/tests/test_html_parser/test_pickle_output') != []


def test_MultiprocessHtml_process_all_raw_html_to_picklesi_mkdir():
    dne_dir = os.getcwd() + '/tests/test_html_parser/test_dne_dir'
    test_html_dir = os.getcwd() + '/tests/test_html_parser/test_raw_html'
    if os.path.isdir(dne_dir):
        shutil.rmtree(dne_dir)

    multi_process_html = MultiProcessHtml()
    multi_process_html.process_all_raw_html_to_pickles(html_pickle_dir=dne_dir,
                                                       raw_html_list=os.listdir(test_html_dir),
                                                       html_dir_path=test_html_dir)
    assert os.listdir(dne_dir) != []


def test_MultiprocessHtml_process_all_raw_html_to_pickles_exception():
    multi_process_html = MultiProcessHtml()
    with pytest.raises(Exception):
        multi_process_html.process_all_raw_html_to_pickles(raw_html_list=[])
