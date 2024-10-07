import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time




@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser



def test_open_site(browser):
    browser.get('https://the-internet.herokuapp.com')
    time.sleep(5)
    flagi = browser.find_element(By.LINK_TEXT, value="Checkboxes")
    flagi.click()
    time.sleep(3)
    title = browser.find_element(By.CSS_SELECTOR, value='h3')
