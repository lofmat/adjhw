import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from task2.pages.search_page import SearchPage


@pytest.fixture(scope='class')
def setup(request):
    print("Initiating chrome driver")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://en.wikipedia.org/w/index.php?search')
    request.cls.driver = driver
    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
class TestSearch:
    def test_wiki_search_default(self):
        search_page = SearchPage(self.driver)
        assert search_page.search_by_default('Berlin Wall')

    def test_wiki_search_jpg_images(self):
        search_page = SearchPage(self.driver)
        adv = search_page.advanced_search_not_these_words('Berlin Wall')
        assert adv





