
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button_first = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    e_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = e_element.text
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    input1.send_keys(y)
    element2 = browser.find_element(By.TAG_NAME, "button")
    element2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()