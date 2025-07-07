from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def browser_work(link):
#    link = link
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#    assert "Congratulations! You have successfully registered!" == welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    return welcome_text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(browser_work("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "ожидаемый текст совпадает с текстом на странице сайта")
    def test_abs2(self):
        self.assertEqual(browser_work("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "ожидаемый текст совпадает с текстом на странице сайта")
    
if __name__ == "__main__":
    unittest.main()

