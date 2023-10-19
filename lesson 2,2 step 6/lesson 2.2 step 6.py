
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    e_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = e_element.text
    print(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    input3.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()