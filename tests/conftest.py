"""
This module contains shared fixtures.
"""
import json
import pytest
import selenium

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):

    # Initialize the ChromeDriver instance
    # driver = webdriver.Chrome("/Users/smowin/.wdm/drivers/chromedriver/mac64/100.0.4896.60/chromedriver")
    # driver = webdriver.Chrome(service=Service("/Users/smowin/.wdm/drivers/chromedriver/mac64/100.0.4896.60/chromedriver"))
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()
