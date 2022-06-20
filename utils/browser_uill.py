from loguru import logger
import webbrowser

class browser_controls(object):

    def __init__(self):
        self.blabla = ""

    def open_browser(self, url_input):
        url = url_input
        browser_enable = False
        try:
            while browser_enable == False:
                browser_enable = webbrowser.open(url, autoraise=False)

                logger.info("open : {}".format(url))
        except Exception as e:
            logger.error("can't open browser : {}".format(e)) 