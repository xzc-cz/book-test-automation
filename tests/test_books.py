import logging
import pytest
from pages.book_page import BookPage

def test_homepage_title(driver):
    logging.info("开始测试：主页标题")
    page = BookPage(driver)
    page.open_homepage()
    assert "Books to Scrape" in page.get_page_title()
    logging.info("测试通过 ✅")

def test_click_first_book(driver):
    page = BookPage(driver)
    page.open_homepage()
    page.click_first_book()
    assert "catalogue" in driver.current_url

def test_click_category_science(driver):
    page = BookPage(driver)
    page.open_homepage()
    page.click_category("Science")
    assert page.is_title_contain("Science")

@pytest.mark.parametrize("category", ["Science", "Poetry", "Fiction"])
def test_price_format(driver, category):
    page = BookPage(driver)
    page.open_homepage()
    page.click_category(category)
    prices = page.get_all_prices()
    for price in prices:
        assert price.text.startswith("£")

@pytest.mark.slow
def test_pagination(driver):
    page = BookPage(driver)
    page.open_homepage()
    titles_page_1 = page.get_all_book_titles()
    page.click_next_page()
    titles_page_2 = page.get_all_book_titles()
    assert titles_page_1 != titles_page_2
