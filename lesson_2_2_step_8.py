from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 

try:

    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Иван")

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input1.send_keys("Иванов")

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input1.send_keys("test@test.ru")

    attach = browser.find_element(By.ID, "file")
    attach.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()