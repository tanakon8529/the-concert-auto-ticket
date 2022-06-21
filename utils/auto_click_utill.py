from loguru import logger
from time import time

import urllib.request
import subprocess
import pyautogui
import pyperclip
import os

class auto_click_controls(object):
    
    def __init__(self):
        # create folder resource
        path_resource = r'resource'
        self.real_path_resource = os.path.realpath(path_resource) 
        if not os.path.exists(self.real_path_resource):
            os.makedirs(self.real_path_resource)

    def get_current_url(self):
        current_url = urllib.urlopen("http://www.stackoverflow.com").getcode()
        return current_url

    def once_click_button(self, path_pic):
        status_click_button = False
        try:
            start = time() + 1
            count_round = 0
            while time() < start:
                button_join = pyautogui.locateOnScreen(self.real_path_resource+'/'+path_pic  , confidence=0.7)
                if button_join:
                    pyautogui.click(button_join)
                    status_click_button = True
                    logger.debug("click button : {}".format(status_click_button))
                    break
                
                count_round += 1
                logger.debug("count click button : {}".format(count_round))

            return status_click_button
        except Exception as e:
            logger.error("{}".format(e)) 

    def once_click_button_05(self, path_pic):
        status_click_button = False
        try:
            start = time() + 1
            count_round = 0
            while time() < start:
                button_join = pyautogui.locateOnScreen(self.real_path_resource+'/'+path_pic  , confidence=0.4)
                if button_join:
                    pyautogui.click(button_join)
                    status_click_button = True
                    logger.debug("click button : {}".format(status_click_button))
                    break
                
                count_round += 1
                logger.debug("count click button : {}".format(count_round))

            return status_click_button
        except Exception as e:
            logger.error("{}".format(e)) 

    def ctrl_c(self):
        text_cilpboard = None
        pyautogui.hotkey('ctrl', 'c')
        try:
            # clipboard windows
            text_cilpboard = pyperclip.paste()
        except Exception as e1:
            try:
                # clipboard linux
                p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
                retcode = p.wait()
                text_cilpboard = p.stdout.read()
            except Exception as e2:
                logger.error("{} - {}".format(e1, e2)) 
        return text_cilpboard

    def ctrl_v(self, path_pic):
        pyautogui.hotkey('ctrl', 'v')

    def funtion_five(self):
        pyautogui.press('f5')
        logger.debug("Refresh !")

    def scroll_down(self):
        for scroll_scale in range(5):
            pyautogui.scroll(-1)

