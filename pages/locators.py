from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form button')

    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_ITEM_PRICE = (By.XPATH, "//div[contains(@class,'basket-mini')]")

    BOOK_NAME_ON_PAGE = (By.XPATH, '//div[contains(@class, "product_main")]/h1')
    BOOK_NAME_IN_TEXT_MESSAGE = (By.XPATH, "//div[@class = 'alertinner ']//strong")
