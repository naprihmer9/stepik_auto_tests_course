import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for elements in elements:
        elements.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()   

finally:
    time.sleep(30)
    browser.quit()