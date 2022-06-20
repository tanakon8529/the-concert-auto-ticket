from utils.browser_uill import browser_controls
from utils.auto_click_utill import auto_click_controls

class auto_click_controls(object):
    
    def __init__(self):
        self.path_pic_get_tickets = path_pic_get_tickets
        self.path_pic_path_url_stage = path_pic_path_url_stage

    >>> HERE <<<
    url_concert = "https://www.theconcert.com/concert/1437"
    bc = browser_controls()
    acc = auto_click_controls("get_tickets.png", "url_stage.png")

    bc.open_browser(url_concert)
    acc.click_button_get_tickets()
    html_stage_url = bc.get_current_url()
    print(html_stage_url)
    # acc.click_price_stage(html_stage_url)