import pytest
from selenium import webdriver
from lesson_07.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_from_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open_calculator_page()
    calculator_page.set_delay()
    calculator_page.fill_numbers()
    result = calculator_page.check_form_result()
    assert result == "15", f"Результат не равен 15"
