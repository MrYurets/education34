
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first = browser.find_element(By.NAME, "firstname")
    first.send_keys("ivan")
    second = browser.find_element(By.NAME, "lastname")
    second.send_keys("ivanov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("rtd")
    current_dir = os.path.dirname(os.path.realpath(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, "file.txt")
    print("путь к файлу", rf"{file_path}")
    button_file = browser.find_element(By.CSS_SELECTOR, '#file')
    button_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()