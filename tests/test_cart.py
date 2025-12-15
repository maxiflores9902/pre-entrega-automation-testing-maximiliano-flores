from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import pytest


@pytest.mark.parametrize("user, password",[("standard_user", "secret_sauce")])
def test_cart(login_driver, user, password):
    try:
        driver = login_driver
        LoginPage(driver).complete_login(user, password)

        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_products = cart_page.get_items_count()

        assert cart_products == 1
    except Exception as ex:
        print(f"Error en test_cart: {ex}")
        raise
