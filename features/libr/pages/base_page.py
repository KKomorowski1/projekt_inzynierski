from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback
import time


class BasePage(object):
    def __init__(self, browser, base_url="https://demoqa.com/"):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 30
    #
    # def find_element(self, *loc):
    #     return self.browser.find_element(*loc)

    def find_elements(self, *loc):
        return self.browser.find_elements(*loc)

    def find_and_scroll_to_element(self, *loc):
        elements = self.find_elements(*loc)
        if len(elements) == 1:
            self.browser.execute_script("arguments[0].scrollIntoView();", elements[0])
            return elements[0]
        else:
            self.browser.execute_script("arguments[0].scrollIntoView();", elements[0])
            return elements

    def open_website(self, url):
        self.browser.get(url)

    def __getattr__(self, element):
        try:
            if element in self.locator_dictionary.keys():
                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[element])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[element])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                return self.find_and_scroll_to_element(*self.locator_dictionary[element])
        except AttributeError:
            super(BasePage, self).__getattribute__("missing_method")(element)

    def missing_method(self, element):
        print("No %s here!" % element)