from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.parametrize("user, password",[("standard_user", "secret_sauce")])
def test_cart_starts_empty(login_driver, user, password):
    driver = login_driver
    LoginPage(driver).complete_login(user, password)

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_cart_count() == 0

@pytest.mark.parametrize("user, password",[("standard_user", "secret_sauce")])
def test_add_backpack_to_cart(login_driver, user, password):
    driver = login_driver
    LoginPage(driver).complete_login(user, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == 1

@pytest.mark.parametrize("user, password",[("standard_user", "secret_sauce")])
def test_cart_is_empty(login_driver, user, password):
    driver = login_driver
    LoginPage(driver).complete_login(user, password)

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_cart_count() == 0

    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_count() == 1

    inventory_page.remove_backpack_from_cart()
    assert inventory_page.get_cart_count() == 0