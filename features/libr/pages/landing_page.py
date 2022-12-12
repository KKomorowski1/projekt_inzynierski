from features.libr.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.browser, base_url="https://demoqa.com/")

    locator_dictionary = {
        "card_elements": (By.XPATH, "//h5[text()='Elements']"),
        "card_forms": (By.XPATH, "//h5[text()='Forms']"),
        "card_alerts": (By.XPATH, "//h5[text()='Alerts, Frame & Windows']"),
        "card_widgets": (By.XPATH, "//h5[text()='Widgets']"),
        "card_interactions": (By.XPATH, "//h5[text()='Interactions']"),
    }
