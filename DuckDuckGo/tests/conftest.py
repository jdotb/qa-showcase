import json
import pytest

from selenium.webdriver import Chrome, Firefox

CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file then return as parsed dictionary
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


# Ensure config file holds the "browser" key, raise exception if browser unsupported
# Return browser choice so available to tests and other fixtures
@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"\nPlease specify a browser in config.json')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


# Ensure a fallback wait_time of 10s, otherwise use the specified wait_time
@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    driver.implicitly_wait(config_wait_time)    # implicitly wait for elements to become available

    yield driver  # return driver after setup

    driver.quit()  # Cleanup: quit driver
