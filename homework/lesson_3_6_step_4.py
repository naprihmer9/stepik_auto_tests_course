import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_auth(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth_login")))
    button.click()
    login = browser.find_element(By.ID, "id_login_email")
    login.send_keys("email")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("password")
    login_button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    login_button.click()