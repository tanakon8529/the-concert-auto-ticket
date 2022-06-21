from loguru import logger
import webbrowser

class browser_controls(object):

    def __init__(self):
        self.blabla = ''

    def open_browser(self, url_input):
        url = url_input
        browser_enable = False
        try:
            while browser_enable == False:
                browser_enable = webbrowser.open(url, autoraise=False)
                logger.info("open : {}".format(url))
        except Exception as e:
            logger.error("can't open browser : {}".format(e)) 

    def check_stage_page(self, url_stage):
        status_page_stage = False
        try:
            if "stage" in url_stage:
                logger.info("url stage : {}".format(url_stage))
                status_page_stage = True
        except Exception as e:
            logger.error("{}".format(e))

        return status_page_stage
