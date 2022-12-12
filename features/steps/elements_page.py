from behave import *

from features.libr.pages.elements_page import ElementsPage

use_step_matcher("re")


@Then("I verify that elements page was opened successfully")
def step_impl(context):
    page = ElementsPage(context)
    assert page.elements_header.text is not None


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
    assert page.result_table is not None
