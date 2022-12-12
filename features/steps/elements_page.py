import time

from behave import *

from features.libr.pages.elements_page import ElementsPage

use_step_matcher("re")


@step("I verify that elements page was opened successfully")
def step_impl(context):
    page = ElementsPage(context)
    assert page.elements_header.text is not None


@step("I click on text box in the menu")
def step_impl(context):
    page = ElementsPage(context)
    page.elements_text_box.click()


@step('I enter full name "([^"]*)"')
def step_impl(context, full_name):
    page = ElementsPage(context).TextBox(context)
    page.full_name_text_box.send_keys(full_name)


@step('I enter email "([^"]*)"')
def step_impl(context, full_name):
    page = ElementsPage(context).TextBox(context)
    page.email_text_box.send_keys(full_name)


@step('I enter current address "([^"]*)"')
def step_impl(context, full_name):
    page = ElementsPage(context).TextBox(context)
    page.current_address_text_box.send_keys(full_name)


@step('I enter permanent address "([^"]*)"')
def step_impl(context, full_name):
    page = ElementsPage(context).TextBox(context)
    page.permanent_address_text_box.send_keys(full_name)


@step('I click submit button')
def step_impl(context):
    page = ElementsPage(context).TextBox(context)
    page.submit_button.click()
