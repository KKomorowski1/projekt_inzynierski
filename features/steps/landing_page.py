from behave import *

from features.libr.pages.elements_page import ElementsPage
from features.libr.pages.landing_page import LandingPage

use_step_matcher("re")


@given("I open demoqa website")
def step_impl(context):
    page = LandingPage(context)
    page.open_website("https://demoqa.com/")


@when("I click Elements Card")
def step_impl(context):
    page = LandingPage(context)
    page.card_elements.click()
