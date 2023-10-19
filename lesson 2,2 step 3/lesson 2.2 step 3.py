
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = int(x_element.text)
    print(x)
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y_element.text)
    print(y)
    z = x + y
    print(z)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(z))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()