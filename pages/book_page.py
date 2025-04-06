from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookPage:
    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        self.driver.get("http://books.toscrape.com/")

    def click_first_book(self):
        self.driver.find_element(By.CSS_SELECTOR, "article.product_pod h3 a").click()

    def click_category(self, category_name):
        self.driver.find_element(By.LINK_TEXT, category_name).click()

    def get_page_title(self):
        return self.driver.title

    def get_all_prices(self):
        return self.driver.find_elements(By.CLASS_NAME, "price_color")

    def get_all_book_titles(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "article.product_pod h3 a")
        return [title.get_attribute("title") for title in titles]

    def click_next_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.next a"))
        ).click()

    def is_title_contain(self, text):
        return text in self.driver.title
