from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        EMAIL_FIELD = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        EMAIL_FIELD.send_keys(email)

        PASSWORD_1_FIELD = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        PASSWORD_1_FIELD.send_keys(password)

        PASSWORD_2_FIELD = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        PASSWORD_2_FIELD.send_keys(password)

        BUTTON_SUBMIT = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT_REGISTRATION)
        BUTTON_SUBMIT.click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Current url is not contains 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"