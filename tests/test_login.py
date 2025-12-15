from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.login_page import LoginPage
from utils.data import read_csv_login
from utils.logger import logger
import pytest

@pytest.mark.parametrize("user,password,works",read_csv_login("data/data_login.csv"))
def test_login_validation(login_driver, user, password, works):
    logger.info("Inicia prueba de validacion")
    driver = login_driver

    LoginPage(driver).complete_login(user, password)

    if works == True:
        logger.info("Verificando redireccionamiento dentor de la pagina")
        try:
            assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
            logger.info("test de login ejecutado de forma correcta")
        except AssertionError as e:
            logger.error(f"Assert fallido: {e}")
    elif works == False:
        error_message = LoginPage(driver).get_error()
        assert "Epic sadface" in error_message, "El mensaje de error no existe"
        logger.info("Test login falla de forma satisfactoria :)")
