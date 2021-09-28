from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# @pytest.fixture(params=list_items)
# def list_loop(request):
#     return request.param
#
#
# class TestList:
#     def test_clicking_items(self):
#         self.browser.get(URL)
#         self.browser.find_element()


class TestListItems:
    URL = "https://lambdatest.github.io/sample-todo-app/"

    ITEM_1 = (By.NAME, 'li1')
    ITEM_2 = (By.NAME, 'li2')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def find_list_item_1(self):
        list_item = self.browser.find_element(self.ITEM_1)