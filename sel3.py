from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_registration():
    try:
        # Инициализируем браузер
        browser = webdriver.Chrome()

        # Открываем первую страницу
        browser.get("http://suninjuly.github.io/registration2.html")

        # Заполняем обязательные поля (селекторы уникальны!)
        browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]').send_keys("Ivan")
        browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys("Petrov")
        browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys("test@test.com")

        # Нажимаем кнопку Submit
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверяем успешный переход
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        browser.quit()


# Запуск теста
if __name__ == "__main__":
    test_registration()


    