from loguru import logger
from bs4 import BeautifulSoup

import urllib.request
import pyautogui
import time
import os

class auto_click_controls(object):
    
    def __init__(self):
        # create folder resource
        path_resource = r'resource'
        self.real_path_resource = os.path.realpath(path_resource) 
        if not os.path.exists(self.real_path_resource):
            os.makedirs(self.real_path_resource)
        self.html_parser = 'html.parser'

    def once_click_button(self, url_page, path_pic):
        try:
            button_join = pyautogui.locateOnScreen(self.real_path_resource+'/'+path_pic  , confidence=0.7)
            if button_join:
                pyautogui.click(button_join)
                logger.error("{}".format(e))
        except Exception as e:
            logger.error("{}".format(e)) 

    def click_price_stage(self, html_url):
        try:
            soup = BeautifulSoup(html_url, self.html_parser)
            ele_stage_body = soup.findAll("div", class_="stage-body")
        except Exception as e:
            logger.error("{}".format(e))