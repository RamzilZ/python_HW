from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 20)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    firstname_input = wait.until(
        EC.presence_of_element_located((By.NAME, "first-name")))
    firstname_input.send_keys("Иван")
    lastname_input = wait.until(
        EC.presence_of_element_located((By.NAME, "last-name")))
    lastname_input.send_keys("Петров")
    address_input = wait.until(
        EC.presence_of_element_located((By.NAME, "address")))
    address_input.send_keys("Ленина, 55-3")
    email_input = wait.until(
        EC.presence_of_element_located((By.NAME, "e-mail")))
    email_input.send_keys("test@skypro.com")
    city_input = wait.until(
        EC.presence_of_element_located((By.NAME, "city")))
    city_input.send_keys("Москва")
    country_input = wait.until(
        EC.presence_of_element_located((By.NAME, "country")))
    country_input.send_keys("Россия")
    phone_input = wait.until(
        EC.presence_of_element_located((By.NAME, "phone")))
    phone_input.send_keys("+7985899998787")
    job_input = wait.until(
        EC.presence_of_element_located((By.NAME, "job-position")))
    job_input.send_keys("QA")
    company_input = wait.until(
        EC.presence_of_element_located((By.NAME, "company")))
    company_input.send_keys("SkyPro")

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    zip_code_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_code_field.get_attribute("class"), "Zip code field is not highlighted in red"

    green_fields_ids = ["first-name", "last-name", "address", "email", "phone_number", "city",
                        "country", "job-position", "company"]

    for field_id in green_fields_ids:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        assert "alert-success" in field_classes, f"Поле{field_id} должна быть зеленым. Классы {field_classes}"

        driver.quit()
