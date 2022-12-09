from behave import *

from features.libr.pages.home_page import HomePage

use_step_matcher("re")


@step("I open globalsqa website")
def step_impl(context):
    page = HomePage(context)
    page.open_website("https://www.globalsqa.com/demo-site/")
    page.tabs_link.click()

