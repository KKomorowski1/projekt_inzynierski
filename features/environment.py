from selenium import webdriver


def before_all(context):
    print("Executing before all")


def before_scenario(context, scenario):
    print("User data:", context.config.userdata)
    # behave -D BROWSER=chrome
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'
    # For some reason, python doesn't have switch case -
    if BROWSER == 'chrome':
        context.browser = webdriver.Chrome()

    context.browser.maximize_window()
    print("Before scenario\n")

