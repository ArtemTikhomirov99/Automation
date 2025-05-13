import allure
from selenium import webdriver
from pages.main_page import MainPage



class TestBurgersPopup:
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    @allure.title('Выбор ингридиентов для бургера')
    @allure.description('Выбор и нажатие на рандомный ингридиент')
    @allure.link("https://stellarburgers.nomoreparties.site", name='Ссылка на Главную')
    def test_popup(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        driver = MainPage(self.driver)
        driver.choosing_loaf()
        driver.popup_exit()
        driver.choosing_sauce()
        driver.popup_exit()
        driver.choosing_filling()
        driver.popup_exit()

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()