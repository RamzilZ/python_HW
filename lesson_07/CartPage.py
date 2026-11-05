from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def __init__(self, driver, url):
    self.driver = driver
    self.url = url
    self.wait = WebDriverWait(self.driver, 10)

class CartPage:
    SHOPPING_CART_BUTTON = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    TOTAL_VALUE = (By.CLASS_NAME, "summary_total_label")
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)
    def get_shopping_card(self):
        self.wait.until(
            EC.presence_of_element_located(self.SHOPPING_CART_BUTTON)
        ).click()
    def get_checkout(self):
        self.wait.until(
            EC.presence_of_element_located(self.CHECKOUT_BUTTON)
        ).click()
    def get_form(self):
        fist_name_input = self.wait.until(EC.presence_of_element_located(
            self.FIRST_NAME_INPUT
        ))
        fist_name_input.send_keys("Kirill")

        last_name_input = self.wait.until(EC.presence_of_element_located(
            self.LAST_NAME_INPUT
        ))
        last_name_input.send_keys("Stanin")

        postal_code_input = self.wait.until(EC.presence_of_element_located(
            self.POSTAL_CODE_INPUT
        ))
        postal_code_input.send_keys("456537")
    def get_continue(self):
        self.wait.until(
            EC.presence_of_element_located(self.CONTINUE_BUTTON)
        ).click()
    def get_total(self):
        self.wait.until(EC.presence_of_element_located(
            self.TOTAL_VALUE
        ))
    def get_result(self):
        self.wait.until(EC.text_to_be_present_in_element(self.TOTAL_VALUE, "Total: $58.29"))
        result_element = self.driver.find_element(*self.TOTAL_VALUE)
        return result_element.text