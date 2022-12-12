import time

from behave import *

from features.libr.pages.elements_page import ElementsPage

use_step_matcher("re")


@Then("I verify that elements page was opened successfully")
def step_impl(context):
    page = ElementsPage(context)
    assert page.elements_header.text is not None


@when("I click on check box in the menu")
def step_impl(context):
    page = ElementsPage(context)
    page.elements_check_box.click()


@when("I click on text box in the menu")
def step_impl(context):
    page = ElementsPage(context)
    page.elements_text_box.click()


@when("I click on radio button in the menu")
def step_impl(context):
    page = ElementsPage(context)
    page.elements_radio_button.click()


@when("I click on web tables in the menu")
def step_impl(context):
    page = ElementsPage(context)
    page.elements_web_tables.click()


@when('I enter full name "([^"]*)"')
def step_impl(context, full_name):
    page = ElementsPage(context).TextBox(context)
    page.full_name_text_box.send_keys(full_name)


@when('I enter email "([^"]*)"')
def step_impl(context, full_name):
    page = ElementsPage(context).TextBox(context)
    page.email_text_box.send_keys(full_name)


@when('I enter current address "([^"]*)"')
def step_impl(context, full_name):
    page = ElementsPage(context).TextBox(context)
    page.current_address_text_box.send_keys(full_name)


@when('I enter permanent address "([^"]*)"')
def step_impl(context, full_name):
    page = ElementsPage(context).TextBox(context)
    page.permanent_address_text_box.send_keys(full_name)


@when('I click submit button')
def step_impl(context):
    page = ElementsPage(context).TextBox(context)
    page.submit_button.click()


@Then('I verify that form was processed')
def step_impl(context):
    page = ElementsPage(context).TextBox(context)
    assert 'border' in page.result_table.get_attribute('class')


@Then('I verify email has red border')
def step_impl(context):
    page = ElementsPage(context).TextBox(context)
    assert 'field-error' in page.email_text_box.get_attribute('class')


@Then('I verify that result table did not appear')
def step_impl(context):
    page = ElementsPage(context).TextBox(context)
    assert 'border' not in page.result_table.get_attribute('class')


@When('I click on check box next to home')
def step_impl(context):
    page = ElementsPage(context).CheckBox(context)
    page.home_check_box.click()
    time.sleep(5)


@Then("Verify text of what was selected is showing")
def step_impl(context):
    page = ElementsPage(context).CheckBox(context)
    assert page.result_text is not None


@When("I expand full tree")
def step_impl(context):
    page = ElementsPage(context).CheckBox(context)
    page.expand_all_button.click()


@When('I select "([^"]*)" checkbox')
def step_impl(context, value):
    page = ElementsPage(context).CheckBox(context)
    for checkbox in page.list_of_checkboxes:
        if checkbox.text == value:
            checkbox.click()


@When("I select 'Yes' radio button")
def step_impl(context):
    page = ElementsPage(context).RadioButton(context)
    page.yes_radio.click()


@When("I select 'Impressive' radio button")
def step_impl(context):
    page = ElementsPage(context).RadioButton(context)
    page.impressive_radio.click()


@Then('I verify bottom text "([^"]*)" with radio button selected')
def step_impl(context, value):
    page = ElementsPage(context).RadioButton(context)
    assert value == page.success_text.text


@When('I click add button')
def step_impl(context):
    page = ElementsPage(context).WebTables(context)
    page.add_button.click()


@When('I click trash can on user number "([^"]*)"')
def step_impl(context, value):
    page = ElementsPage(context).WebTables(context)
    page.delete_buttons[int(value) - 1].click()
    time.sleep(5)


@When('I click edit on user number "([^"]*)"')
def step_impl(context, value):
    page = ElementsPage(context).WebTables(context)
    page.edit_buttons[int(value) - 1].click()


@When('I enter "([^"]*)" as first name')
def step_impl(context, first_name):
    page = ElementsPage(context).WebTables(context)
    page.first_name_input.clear()
    page.first_name_input.send_keys(first_name)


@When('I enter "([^"]*)" as last name')
def step_impl(context, last_name):
    page = ElementsPage(context).WebTables(context)
    page.last_name_input.clear()
    page.last_name_input.send_keys(last_name)


@When('I enter "([^"]*)" as email')
def step_impl(context, email):
    page = ElementsPage(context).WebTables(context)
    page.email_input.clear()
    page.email_input.send_keys(email)


@When('I enter "([^"]*)" as age')
def step_impl(context, age):
    page = ElementsPage(context).WebTables(context)
    page.age_input.clear()
    page.age_input.send_keys(age)


@When('I enter "([^"]*)" as salary')
def step_impl(context, salary):
    page = ElementsPage(context).WebTables(context)
    page.salary_input.clear()
    page.salary_input.send_keys(salary)


@When('I enter "([^"]*)" as department')
def step_impl(context, department):
    page = ElementsPage(context).WebTables(context)
    page.department_input.clear()
    page.department_input.send_keys(department)


@When('I click submit button in form')
def step_impl(context):
    page = ElementsPage(context).WebTables(context)
    page.submit_button.click()
    time.sleep(5)


@Then('I verify data is in table: "([^"]*)", "([^"]*)", "([^"]*)", "([^"]*)", "([^"]*)", "([^"]*)"')
def step_impl(context, first_name, last_name, email, age, salary, department):
    page = ElementsPage(context).WebTables(context)
    data_from_table = []
    for i in page.data_in_table:
        data_from_table.append(i.text)
    assert first_name in data_from_table
    assert last_name in data_from_table
    assert email in data_from_table
    assert age in data_from_table
    assert salary in data_from_table
    assert department in data_from_table


@Then('I verify data is not in table: "([^"]*)", "([^"]*)", "([^"]*)", "([^"]*)", "([^"]*)", "([^"]*)"')
def step_impl(context, first_name, last_name, email, age, salary, department):
    page = ElementsPage(context).WebTables(context)
    data_from_table = []
    for i in page.data_in_table:
        data_from_table.append(i.text)
    assert first_name not in data_from_table
    assert last_name not in data_from_table
    assert email not in data_from_table
    assert age not in data_from_table
    assert salary not in data_from_table
    assert department not in data_from_table
