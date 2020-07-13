from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS) , "basket isn't empty"
        el = self.browser.find_element(*BasketPageLocators.BASKET_TEXT)
        text = el.text
        print(text)
        assert "is empty" in text , "text says that basket isn't empty"