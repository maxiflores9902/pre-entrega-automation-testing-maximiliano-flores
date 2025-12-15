from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Your Cart"

    def get_items_count(self):
        return len(self.wait.until(lambda d: d.find_elements(*self.CART_ITEMS)))

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def get_first_item_name(self):
        return self.get_text(self.ITEM_NAME)

    def get_items_names(self):
        elements = self.find_elements(self.ITEM_NAME)
        return [el.text for el in elements]
