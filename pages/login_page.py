from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        mail_in = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT_INPUT)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        mail_in.send_keys(email)
        pass1.send_keys(password)
        pass2.send_keys(password)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, " 'login' is not in URL "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "there is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "there is no register form"
