from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.TAG_NAME, "button")

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Products"

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)
    
    def add_product_by_name(self, product_name):
        items = self.find_elements(self.INVENTORY_ITEMS)

        for item in items:
            name = item.find_element(*self.ITEM_NAME).text

            if name.strip().lower() == product_name.strip().lower():
                item.find_element(*self.ADD_TO_CART_BUTTON).click()
                return

        raise Exception(f"Product not found: {product_name}")

    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK)

    def get_cart_count(self):
        if self.is_displayed(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_ICON)
