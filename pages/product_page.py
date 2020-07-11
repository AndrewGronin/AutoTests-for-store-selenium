import math

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла



class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()


    def is_name_right(self):
        el = self.browser.find_element(*ProductPageLocators.ALERT_ADD_TO_BASKET_NAME)
        text = el.text
        nm = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name = nm.text
        return text == name

    def is_price_right(self):
        el = self.browser.find_element(*ProductPageLocators.ALERT_ADD_TO_BASKET_PRICE)
        text = el.text
        nm = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price = nm.text
        return text == price


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ADD_TO_BASKET_NAME), \
            "Success message is not disappered"