from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login_page import LoginPage
import pytest
from faker import Faker


fake = Faker()

@pytest.mark.parametrize("user, password, works", [
    (fake.user_name(), fake.password(length=8, special_chars=True, upper_case=True, lower_case=True, digits=True), False),
    (fake.user_name(), fake.password(), False)
])
def test_login_validation(login_driver, user, password, works):
    driver = login_driver
    LoginPage(driver).complete_login(user, password)

    if works:
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
    else:
        error_message = LoginPage(driver).get_error()
        assert "Epic sadface" in error_message, "el mensaje de error no existe"