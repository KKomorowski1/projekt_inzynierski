from selenium.webdriver.common.by import By

from features.libr.pages import BasePage


class ElementsPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser, base_url="https://demoqa.com/")

    locator_dictionary = {
        "elements_text_box": (By.XPATH, "//span[text()='Text Box']"),
        "elements_check_box": (By.XPATH, "//span[text()='Check Box']"),
        "elements_radio_button": (By.XPATH, "//span[text()='Radio Button']"),
        "elements_web_tables": (By.XPATH, "//span[text()='Web Tables']"),
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
            "submit_button": (By.ID, "submit"),
            "result_table": (By.XPATH, "//div[@id='output']//div")
        }

    class CheckBox(BasePage):
        def __init__(self, context):
            BasePage.__init__(self, context.browser, base_url="https://demoqa.com/")

        locator_dictionary = {
            "elements_header": (By.XPATH, "//div[@class='main-header']"),
            "home_check_box": (By.XPATH, "//span[text()='Home']"),
            "result_text": (By.ID, "result"),
            "expand_button": (By.XPATH, "//button[@title='Toggle']"),
            "expand_all_button": (By.XPATH, "//button[@title='Expand all']"),
            "list_of_checkboxes": (By.XPATH, "//span[@class='rct-title']")
        }

    class RadioButton(BasePage):
        def __init__(self, context):
            BasePage.__init__(self, context.browser, base_url="https://demoqa.com/")

        locator_dictionary = {
            "elements_header": (By.XPATH, "//div[@class='main-header']"),
            "yes_radio": (By.XPATH, "//label[@for='yesRadio']"),
            "impressive_radio": (By.XPATH, "//label[@for='impressiveRadio']"),
            "success_text": (By.XPATH, "//span[@class='text-success']")
        }

    class WebTables(BasePage):
        def __init__(self, context):
            BasePage.__init__(self, context.browser, base_url="https://demoqa.com/")

        locator_dictionary = {
            "add_button": (By.ID, "addNewRecordButton"),
            "delete_buttons": (By.XPATH, "//span[@title='Delete']"),
            "edit_buttons": (By.XPATH, "//span[@title='Edit']"),
            "success_text": (By.XPATH, "//span[@class='text-success']"),
            "first_name_input": (By.ID, "firstName"),
            "last_name_input": (By.ID, "lastName"),
            "email_input": (By.ID, "userEmail"),
            "age_input": (By.ID, "age"),
            "salary_input": (By.ID, "salary"),
            "department_input": (By.ID, "department"),
            "submit_button": (By.ID, "submit"),
            "data_in_table": (By.XPATH, "//div[@class='rt-td']")
        }
