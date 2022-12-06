from features.libr.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser, base_url="https://www.globalsqa.com/demo-site/")

    locator_dictionary = {
        "tabs_link": (By.XPATH, "//a[text()='Tabs']")
    }
