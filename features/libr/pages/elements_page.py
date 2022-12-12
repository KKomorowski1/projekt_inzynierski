from selenium.webdriver.common.by import By

from features.libr.pages import BasePage


class ElementsPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser, base_url="https://demoqa.com/")

    locator_dictionary = {
        "elements_text_box": (By.XPATH, "//span[text()='Text Box']"),
        "elements_header": (By.XPATH, "//div[@class='main-header']")
    }

    class TextBox(BasePage):
        def __init__(self, context):
            BasePage.__init__(self, context.browser, base_url="https://demoqa.com/")

        locator_dictionary = {
            "elements_header": (By.XPATH, "//div[@class='main-header']"),
            "email_text_box": (By.ID, "userEmail"),
            "current_address_text_box": (By.ID, "currentAddress"),
            "permanent_address_text_box": (By.ID, "permanentAddress"),
            "full_name_text_box": (By.ID, "userName"),
            "submit_button": (By.ID, "submit")
        }

