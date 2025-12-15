from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.json_reader import read_products_from_json
import pytest
import time


PATH_JSON = "data/products.json"

@pytest.mark.parametrize("user, password", [("standard_user", "secret_sauce")])
@pytest.mark.parametrize("product_name", read_products_from_json(PATH_JSON))
def test_cart_json(login_driver, user, password, product_name):
    try:
        driver = login_driver
        LoginPage(driver).complete_login(user, password)
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_by_name(product_name)
        inventory_page.go_to_cart()
        time.sleep(1)
        cart_page = CartPage(driver)
        assert cart_page.get_first_item_name() == product_name
    except Exception as ex:
        print(f"Error en test_cart_json: {ex}")
        raise
