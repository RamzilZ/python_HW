from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.maximize_window()


    button = driver.find_element(By.CSS_SELECTOR, "#start button")
    button.click()


    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#finish"), "Hello World!"))
    driver.save_screenshot("screenshots/text_screen.png")

    hello_element = driver.find_element(By.CSS_SELECTOR, "#finish")
    assert hello_element.text == "Hello World!"

    driver.quit()
