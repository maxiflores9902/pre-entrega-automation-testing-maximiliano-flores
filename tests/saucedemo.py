import pytest
from selenium.webdriver.common.by import By
from utils.helpers import start_driver, wait_element

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    driver = start_driver()
    yield driver
    driver.quit()


def test_login_exitoso(driver):
    driver.get(URL)
    wait_element(driver, By.ID, "user-name").send_keys(USERNAME)
    wait_element(driver, By.ID, "password").send_keys(PASSWORD)
    wait_element(driver, By.ID, "login-button").click()

    # Validar redireccion y textos
    assert "/inventory.html" in driver.current_url
    titulo = wait_element(driver, By.CLASS_NAME, "title").text
    assert "Products" in titulo


def test_catalogo_visible(driver):
    driver.get(URL)
    wait_element(driver, By.ID, "user-name").send_keys(USERNAME)
    wait_element(driver, By.ID, "password").send_keys(PASSWORD)
    wait_element(driver, By.ID, "login-button").click()

    titulo = wait_element(driver, By.CLASS_NAME, "title").text
    assert titulo == "Products"

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0

    nombre = productos[0].find_element(
        By.CLASS_NAME, "inventory_item_name").text
    precio = productos[0].find_element(
        By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto: {nombre} - {precio}")


def test_agregar_producto_al_carrito(driver):
    driver.get(URL)
    wait_element(driver, By.ID, "user-name").send_keys(USERNAME)
    wait_element(driver, By.ID, "password").send_keys(PASSWORD)
    wait_element(driver, By.ID, "login-button").click()

    primer_producto_btn = wait_element(
        driver, By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")
    primer_producto_btn.click()

    contador = wait_element(
        driver, By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1"

    wait_element(driver, By.CLASS_NAME, "shopping_cart_link").click()
    producto_en_carrito = wait_element(
        driver, By.CLASS_NAME, "inventory_item_name").text
    assert producto_en_carrito != ""
