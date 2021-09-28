import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

"""
Test Objectives
    1. Navigate to https://lambdatest.github.io/sample-todo-app/
    2. Select the first two checkboxes
    3. Send "Happy Testing!" to the textbox with id=sampletodotext
    4. Click the Add Button and verify if text has been added or not
"""



def test_todo_app():
    URL = 'https://lambdatest.github.io/sample-todo-app/'

    # initialize driver
    chrome_driver = webdriver.Chrome()

    # get page to test and maximize window
    chrome_driver.get(URL)
    chrome_driver.maximize_window()

    chrome_driver.find_element(By.NAME, 'li1').click()
    chrome_driver.find_element(By.NAME, 'li2').click()

    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title

    sample_text = "Happy Testing!"
    email_text_field = chrome_driver.find_element(By.ID, 'sampletodotext')
    email_text_field.send_keys(sample_text)
    sleep(5)

    chrome_driver.find_element(By.ID, 'addbutton').click()
    sleep(5)

    output_str = chrome_driver.find_element(By.NAME, 'li6').text
    sys.stderr.write(output_str)

    sleep(2)
    chrome_driver.close()
