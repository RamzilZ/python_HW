from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://gitflic.ru/")
    driver.maximize_window()

    driver.find_element(By.CLASS_NAME, "cookiesBtn").click()
    driver.delete_all_cookies()

    driver.add_cookie ({
        "name": "SESSION",
        "value": "MzViMjI1ZWMtNzMxMS00M2I1LWFjZDktYzMyZjIxODQ3OWZj",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    profile1 = "https://gitflic.ru/testershi"
    driver.get(profile1)
    wait.until(EC.url_contains("testershi"))
    profile1=driver.current_url
    print("URL пользователя 1:", profile1)

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "YTc0ZmU5ODAtZDAzNS00MjRhLWEzZjUtMTk2MzFmZmQ3Y2Y0",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    profile2 = "https://gitflic.ru/ramilia"
    driver.get(profile2)
    wait.until(EC.url_contains("ramilia"))
    profile2 = driver.current_url
    print("URL пользователя 2:", profile2)

    assert profile1 != profile2, f"URL пользователей {profile1} и {profile2} должны быть разные"

    driver.quit()
