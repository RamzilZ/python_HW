from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    driver.maximize_window()
    sleep(2)

    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) == 9

    for link in links:
        assert link.is_displayed(), "Ссылка не отображается на странице"

    first_link = links[0]
    assert "1" in first_link.text
    sleep(2)

    driver.quit()