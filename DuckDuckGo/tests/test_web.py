"""
[Test Objectives]
    1. Navigate to DuckDuckGo
    2. Enter search phrase
    3. Verify:
        a. Results appear on the results page
        b. The search phrase appears in the search bar
        c. At least one search result contains the search phrase

[Pending tests]
    1. Parameterized test to search other phrases
    2. Click a result
    3. Search for images, videos, and news

[to run]
    pipenv run python -m pytest
"""

from DuckDuckGo.pages.results import DuckDuckGoResultPage
from DuckDuckGo.pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
    """

    ------------------------------------
    // Code prior to converting to POM //
    ------------------------------------

    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'
    browser.get(URL)
    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(PHRASE + Keys.RETURN)

    """

    PHRASE = 'test automation'

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    """
    
    -------------------------------------------------------------
    // Code prior to converting to POM commented above POM code//
    -------------------------------------------------------------
    
    """

    result_page = DuckDuckGoResultPage(browser)

    # link_divs = browser.find_elements_by_css_selector('#links > div')
    # assert len(link_divs) > 0
    # BECOMES:
    assert result_page.link_div_count() > 0

    # phrase_results = browser.find_elements_by_xpath(xpath)
    # assert len(phrase_results) > 0
    # BECOMES:
    assert result_page.phrase_result_count(PHRASE) > 0

    # search_input = browser.find_element_by_id('search_form_input')
    # assert search_input.get_attribute('value') == PHRASE
    # BECOMES:
    assert result_page.search_input_value() == PHRASE
