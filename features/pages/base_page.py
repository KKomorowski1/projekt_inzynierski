class BasePage(object):
    def __init__(self, browser, base_url="https://www.globalsqa.com/demo-site/"):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def open_website(self, url):
        self.browser.get(url)