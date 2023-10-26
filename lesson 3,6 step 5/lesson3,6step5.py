import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("link", ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    browser.get(link)
    browser.implicitly_wait(15)
    browser.find_element(By.CSS_SELECTOR, "#ember33").click() # кнопка "Войти"
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("ura9464@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("17111999")
    browser.find_element(By.CSS_SELECTOR, "button.button_with-loader").click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys(str(math.log(int(time.time()))))
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, "submit-submission").click() # кнопка "отправить ответ"
    time.sleep(5)
    otvet = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    assert otvet == "Correct!", f"_________Not correct. Text - {otvet}___________"

if __name__ == '__main__':
    pytest.main()

