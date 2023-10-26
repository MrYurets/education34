import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser_object = webdriver.Chrome()
    return browser_object

class TestMainPage1:
    # Вызываем фикстуру в тесте, передав её как параметр
    def test_quest_should_see_login_link(self, browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
    def test_quest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(url)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
