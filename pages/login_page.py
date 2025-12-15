from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    URL = "https://www.saucedemo.com/"
    _USER_INPUT = (By.ID,"user-name")
    _PASS_INPUT = (By.ID,"password")
    _LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def open_page(self):
        self.driver.get(self.URL)
        return self

    def complete_user(self,user):
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        input.clear()
        input.send_keys(user)
        return self

    def complete_pass(self,password):
        input = self.driver.find_element(*self._PASS_INPUT)
        input.clear()
        input.send_keys(password)
        return self

    def click_button(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def complete_login(self,usuario,password):
        self.complete_user(usuario)
        self.complete_pass(password)
        time.sleep(1)
        self.click_button()
        return self

    def get_error(self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".error-message-container h3")))
        return div_error.text
