from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def __init__(self, driver, url):
    self.driver = driver
    self.url = url
    self.wait = WebDriverWait(self.driver, 10)

class MainShopPage:
    LOGIN_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ADD_sauce_labs_backpack_BUTTON =(
        By.NAME, 'add-to-cart-sauce-labs-backpack')
    ADD_sauce_labs_bolt_t_shirt_BUTTON =(
            By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_to_cart_sauce_labs_onesie_BUTTON =(
            By.NAME, "add-to-cart-sauce-labs-onesie")
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)
    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/checkout-step-one.html"
            )
    def authorization (self):
        login_input = self.wait.until(EC.presence_of_element_located(
            self.LOGIN_INPUT
        ))
        login_input.send_keys("standard_user")

        password_input = self.wait.until(EC.presence_of_element_located(
            self.PASSWORD_INPUT
        ))
        password_input.send_keys("secret_sauce")

        login_button = self.wait.until(EC.presence_of_element_located(
            self.LOGIN_BUTTON
        ))
        login_button.click()
    def get_add_product(self):
        self.wait.until(
          EC.presence_of_element_located(self.ADD_sauce_labs_backpack_BUTTON)
        ).click()
        self.wait.until(
            EC.presence_of_element_located(self.ADD_sauce_labs_bolt_t_shirt_BUTTON)
        ).click()
        self.wait.until(
        EC.presence_of_element_located(self.ADD_to_cart_sauce_labs_onesie_BUTTON)
        ).click()