import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.base_pages import BasePages

class TestBurgersPopup:
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    @allure.title('Набор ингридиентов для бургера')
    @allure.description('Вбор рандомного ингридиента')
    @allure.link("https://stellarburgers.nomoreparties.site", name='Ссылка на Главную')
    def test_popup(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        driver = MainPage(self.driver)
        driver.click_cabinet_btn()
        driver = BasePages(self.driver)
        driver.check_input_email()
        driver.input_email()
        driver.check_input_password()
        driver.input_password()
        driver.click_input()
        driver = MainPage(self.driver)
        driver.choosing_loaf_bb()
        driver.choosing_sauce_bb()
        driver.choosing_filling_bb()


    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()