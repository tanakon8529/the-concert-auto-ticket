import re
from utils.browser_uill import browser_controls
from utils.auto_click_utill import auto_click_controls

from loguru import logger

class auto_tickets_controls(object):
    
    def __init__(self):
        self.browser = browser_controls()
        self.auto_click = auto_click_controls()

    def open_and_click_get_ticket(self, url_get_ticket, pic_get_ticket):
        status_click_button = False
        count_round = 0
        self.browser.open_browser(url_get_ticket)
        while status_click_button != True:
            if (count_round % 2 == 0):
                self.auto_click.funtion_five()
            status_click_button = self.auto_click.once_click_button(pic_get_ticket)
            count_round += 1

    def copy_url_and_process_stage_page(self, pic_url_stage):
        status_click_button = False
        while status_click_button != True:
            status_click_button = self.auto_click.once_click_button(pic_url_stage)

        url_stage = self.auto_click.ctrl_c()
        if url_stage:
            status_page_stage = self.browser.check_stage_page(url_stage)
        return status_page_stage

    def click_pointer_and_add_tickets(self, pic_pointer_button, pic_seat_button, pic_sold_out_button, pic_add_tickets, total_tickets, pic_buy_tickeys):
        status_click_pointer_button = False
        status_click_add_button = False
        status_click_buy_button = False
        status_click_seat_button = False
        count_scroll_down = 0

        while status_click_pointer_button != True:
            status_click_pointer_button = self.auto_click.once_click_button(pic_pointer_button)

            if status_click_pointer_button == True:
                while status_click_seat_button != True:
                    for total in range(total_tickets-1):
                        status_click_seat_button = self.auto_click.once_click_button_05(pic_seat_button)

            if status_click_pointer_button == False:
                self.auto_click.once_click_button(pic_sold_out_button)
                self.auto_click.scroll_down()
                count_scroll_down += 1
                logger.debug("round scroll : {}".format(count_scroll_down))

                if count_scroll_down > 3:
                    return status_click_buy_button

        if status_click_seat_button == False:
            for total in range(total_tickets-1):
                status_click_add_button = self.auto_click.once_click_button(pic_add_tickets)

        if status_click_add_button == True or status_click_seat_button == True:
            status_click_buy_button = self.auto_click.once_click_button(pic_buy_tickeys)

        return status_click_buy_button
        

    def process_auto_tickers_bot(self, payload):
        url_get_ticket = payload["url_get_ticket"]
        pic_get_ticket = payload["pic_get_ticket"]
        pic_url_stage = payload["pic_url_stage"]
        pic_pointer_button = payload["pic_pointer_button"]
        pic_seat_button = payload["pic_seat_button"]
        pic_sold_out_button = payload["pic_sold_out_button"]
        pic_add_tickets = payload["pic_add_tickets"]
        total_tickets = payload["total_tickets"]
        pic_buy_tickeys = payload["pic_buy_tickeys"]

        status_click_buy_button = False

        while status_click_buy_button != True:
            if status_click_buy_button == False:
                self.open_and_click_get_ticket(url_get_ticket, pic_get_ticket)

            status_page_stage = self.copy_url_and_process_stage_page(pic_url_stage)
            if status_page_stage:
                status_click_buy_button = self.click_pointer_and_add_tickets(pic_pointer_button, pic_seat_button, pic_sold_out_button, pic_add_tickets, total_tickets, pic_buy_tickeys)
                logger.debug("ready to buy tickets : {}".format(status_click_buy_button))

