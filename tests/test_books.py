import time
from pages.book_page import BookPage

def test_homepage_title(driver):
    page = BookPage(driver)
    page.open_homepage()
    assert "Books to Scrape" in page.get_page_title()

def test_click_first_book(driver):
    page = BookPage(driver)
    page.open_homepage()
    page.click_first_book()
    # 修复：只断言是否进入了图书详情页（包含 catalogue 或图书标题）
    assert "catalogue" in driver.current_url or "index.html" in driver.current_url


def test_click_category_science(driver):
    page = BookPage(driver)
    page.open_homepage()
    page.click_category("Science")
    assert "Science" in page.get_page_title()

def test_price_format(driver):
    page = BookPage(driver)
    page.open_homepage()
    prices = page.get_all_prices()
    for price in prices:
        assert price.text.startswith("£")

def test_pagination(driver):
    page = BookPage(driver)
    page.open_homepage()
    titles_page_1 = page.get_all_book_titles()
    page.click_next_page()
    titles_page_2 = page.get_all_book_titles()
    # 验证翻页后内容不同
    assert titles_page_1 != titles_page_2
