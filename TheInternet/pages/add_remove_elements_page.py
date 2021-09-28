from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TheInternetHerokuPage:
    URL = 'https://the-internet.herokuapp.com/add_remove_elements/'

    # Locator to find the 'add element'
    ADD_ELEMENT = (By.CLASS_NAME, 'example')
    REMOVE_ELEMENT = (By.CLASS_NAME, 'elements')
    NUM_ELEMENTS = 0

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    # Add new element to page
    def add_element(self):
        add_new_element = self.browser.find_element(self.ADD_ELEMENT)
        add_new_element.click()

    def count_elements(self):
        num_added = self.browser.find_elements(By.CLASS_NAME, 'added-manually')
        num_added_count = len(num_added)
        return num_added_count

    # Remove element from page
    def remove_element(self, ):

        num_added = self.browser.find_elements(self.REMOVE_ELEMENT)
        num_added_count = len(num_added)
        remove_added_element = self.browser.find_element(self.REMOVE_ELEMENT)
        remove_added_element.click()
