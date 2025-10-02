from .base_page import BasePage
from .locators import ProductPageLocators
import re

class ProductPage(BasePage):
    def click_to_button_add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_link.click()

    def should_be_correct_cost_in_success_message(self):
        TEXT_PRICE = self.browser.find_element(*ProductPageLocators.PRICE).text
        PRICE = re.search(r"\d+,\d+", TEXT_PRICE).group() #использование регулярных выражений для извлечения стоимости из текста
        TEXT_BASKET_ITEM_PRICE = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_PRICE).text
        BASKET_ITEM_PRICE = re.search(r"\d+,\d+", TEXT_BASKET_ITEM_PRICE).group()
        assert PRICE == BASKET_ITEM_PRICE, f'text in basket [{PRICE}] is not equals text in page[{BASKET_ITEM_PRICE}].'

    def should_be_correct_product_name_in_success_message(self):
        BOOK_NAME_ON_PAGE = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_PAGE).text
        BOOK_NAME_IN_TEXT_MESSAGE = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_TEXT_MESSAGE).text
        assert BOOK_NAME_ON_PAGE == BOOK_NAME_IN_TEXT_MESSAGE, f'book name on page [{BOOK_NAME_ON_PAGE}] not equals book name in text message [{BOOK_NAME_IN_TEXT_MESSAGE}]'