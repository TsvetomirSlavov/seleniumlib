import time
import urlparse


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.parsedCurrentUrl = urlparse.urlparse(self.driver.current_url)
        time.sleep(2)

    @classmethod
    def in_page(cls, driver):
        parsed_current_url = urlparse.urlparse(driver.current_url)
        return parsed_current_url.path in cls.PAGE_URL_PATHS

    @staticmethod
    def wait(seconds):
        time.sleep(seconds)