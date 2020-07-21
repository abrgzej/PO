from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.go_to_login_link()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def go_to_login_link(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form not present'
