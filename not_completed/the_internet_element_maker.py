from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/"

all_elements = []
try:
    driver.get(url)

    # Find the content body
    content = driver.find_element_by_id("content")

    # Find the full unordered list
    ul = content.find_element_by_xpath("/html/body/div[2]/div/ul")

    # Iterate through each item and add to all_elements
    # To find all child elements by css_selector: object.find_elements_by_css_selector("*")
    # To find all child elements by xpath: object.find_elements_by_xpath(".//*")
    for li in ul.find_elements_by_css_selector("*"):
        new_item = li.text
        all_elements.append(new_item)

    print(all_elements)

finally:
    driver.close()
    driver.quit()
