"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from config.config import URL


class DuckDuckGoSearchPage:

    # Locators

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
