from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import unittest
import time

test_sites = {
    "The-internet": "https://the-internet.herokuapp.com/",
    "ToolsQA": "https://demoqa.com/",
    "Formy": "https://formy-project.herokuapp.com/",
    "ParaBank": "https://parabank.parasoft.com/parabank/index.htm",
    "OpenCart": "http://opencart.abstracta.us/",
    "Auto-practice": "http://automationpractice.com/index.php"
}

para_bank_creds = {'john': 'demo'}


class ChromeBrowse(unittest.TestCase):

    def chrome_setup(self):
        chrome_opts = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.maximize_window()

    def test_browse_test_sites_chrome(self):
        driver_chrome = self.driver

    def tearDown(self):
        # Close browser window
        self.driver.close()


class FirefoxBrowse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_browse_test_sites_firefox(self):
        driver_firefox = self.driver
        driver_firefox.get(test_sites["The-internet"])
        time.sleep(5)

        # Navigate to 'Add/Remove Elements'
        navigate_1 = driver_firefox.find_element_by_link_text("Add/Remove Elements")
        navigate_1.click()

        # Click 'Add element' button - will add elements each time clicked (maybe track clicks to check in test?)
        add_element = driver_firefox.find_element_by_xpath('//*[@id="content"]/div/button')
        add_element.click()

        # Check how many elements are now present

        # Click 'Delete' to delete the added element
        new_element = driver_firefox.find_element_by_xpath('//*[@id="elements"]/button')

    def tearDown(self):
        # Close browser
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
