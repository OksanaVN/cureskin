from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchPage(Page):
    PRODUCT_IMG = (By.CSS_SELECTOR, 'div.card-wrapper lazy-image.image-animate')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.card-wrapper a.card-information__text.h4')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.card-wrapper div.price')

    def open_search_page(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def verify_first_results_have_name_img_price(self):
        assert self.find_element(*self.PRODUCT_IMG), 'Product Image is missing'
        assert self.find_element(*self.PRODUCT_NAME), 'Product Name is missing'
        assert self.find_element(*self.PRODUCT_PRICE), 'Product Price is missing'