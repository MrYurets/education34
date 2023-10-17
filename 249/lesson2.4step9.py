from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element(By.ID, "book").click()
    e_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = e_element.text
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    input1.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()