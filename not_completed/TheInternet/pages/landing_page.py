from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TheInternetHerokuPage:
    URL = 'https://the-internet.herokuapp.com/'

    # Locator to find search input element
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    # Search method - parameterized for extended usability
    # The * operator expands self.SEARCH_INPUT into positional arguments for the method call
    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)