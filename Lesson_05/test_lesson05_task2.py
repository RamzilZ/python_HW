from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    driver.maximize_window()
    sleep(2)

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Ramzil")
    sleep(3)

    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_btn.click()
    assert "https://httpbin.qa-territory.online/post" == driver.current_url
    sleep(3)

    driver.quit()