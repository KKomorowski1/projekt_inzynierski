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


@step('I select "([^"]*)" checkbox')
def step_impl(context, value):
    page = ElementsPage(context).CheckBox(context)
    for checkbox in page.list_of_checkboxes:
        if checkbox.text == value:
            checkbox.click()
