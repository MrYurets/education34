
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def get_link(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys("ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys("ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys("ivan@")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    return welcome_text

class TestReg(unittest.TestCase):
    def test_link1(self):
        welcome_text = get_link("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_link2(self):
        welcome_text = get_link("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
if __name__ == "__main__":
    unittest.main()