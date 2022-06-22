from loguru import logger
from time import time
from sys import platform

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

    def check_platform(self, path_folder_full, path_input):
        real_path = path_folder_full
        if path_folder_full == None:
            real_path = self.real_path_resource

        if platform == "linux" or platform == "linux2":
            # linux
            path_folder_full = real_path+'/'+path_input
        elif platform == "darwin":
            # OS X
            path_folder_full = real_path+'/'+path_input
        elif platform == "win32":
            # Windows..
            path_folder_full = real_path+'\\'+path_input

        return path_folder_full

    def once_click_button(self, path_pic):
        status_click_button = False
        path_folder_full = None
        try:
            start = time() + 5
            while time() < start:
                pic_path_folder_full = self.check_platform(path_folder_full, path_pic)
                button_join = pyautogui.locateOnScreen(pic_path_folder_full  , confidence=0.7)

                if button_join:
                    pyautogui.click(button_join)
                    status_click_button = True
                    logger.debug("click button : {}".format(status_click_button))
                    break

            return status_click_button
        except Exception as e:
            logger.error("{}".format(e)) 

    def once_click_seat_button_05(self, total_tickets, folder_pic_seat_button, pic_seat_success):
        status_click_button = False
        path_folder_full = None
        try:
            start = time() + 10
            while time() < start:
                real_path_folder_full = self.check_platform(path_folder_full, folder_pic_seat_button)

                for path_pic in os.listdir(real_path_folder_full):
                    if path_pic.endswith(".png"):
                        pic_path_folder_full = self.check_platform(real_path_folder_full, path_pic)

                    button_join_location = pyautogui.locateOnScreen(pic_path_folder_full  , confidence=0.8)
                    logger.debug("search seat : {}".format(path_pic))

                    if button_join_location:
                        for press_time in range(total_tickets):
                            logger.debug("press {} : total {}".format(press_time, total_tickets))
                            button_join_point = pyautogui.center(button_join_location)
                            button_join_point_x, button_join_point_y = button_join_point
                            pyautogui.click(button_join_point_x+press_time, button_join_point_y)
                            status_click_button = True

                    logger.debug("click seat : {}".format(status_click_button))

                    if status_click_button == True:
                        break
                if status_click_button == True:
                    break

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

    def check_seat_success(self, pic_seat_success):
        status_text_pic_seat_success = False
        path_folder_full = None
        try:
            pic_path_folder_full = self.check_platform(path_folder_full, pic_seat_success)
            text_pic_seat_success = pyautogui.locateOnScreen(pic_path_folder_full  , confidence=0.7)
            if text_pic_seat_success:
                status_text_pic_seat_success = True

            return status_text_pic_seat_success
        except Exception as e:
            logger.error("{}".format(e)) 
