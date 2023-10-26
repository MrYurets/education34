from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '".first_block .first"')
    input1.send_keys("ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '.second_class [placeholder="Input your last name"]')
    input2.send_keys("ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.third_class [placeholder="Input your email"]')
    input3.send_keys("ivan@")
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)


    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)
    browser.quit()