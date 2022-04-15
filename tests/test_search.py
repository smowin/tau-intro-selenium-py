"""
These tests cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    # SEARCH_PHRASE = "panda"

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for phrase
    search_page.search(phrase)

    # Then the search result query is phrase
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to phrase
    # for title in result_page.result_link_titles():
    #     assert SEARCH_PHRASE.lower() in title.lower()
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains "panda"
    # (Putting this assertion last guarantees that the page tittle will be ready)
    assert phrase in result_page.title()

    # # TODO: Remove this exception once the test is complete
    # raise Exception("Incomplete Test")
