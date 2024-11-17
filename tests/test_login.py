import allure
from selenium import webdriver
from pages.base_pages import BasePages
from pages.main_page import MainPage
from pages.personal_account import PersonalAccount
from pages.registration import Registration
from pages.recover_password import RecoverPassword


class TestButtonsLogin:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    @allure.title('Заполнение полей данными')
    @allure.description('Заполнение полей "Email" и "Password" данными')
    @allure.link("https://stellarburgers.nomoreparties.site/login", name='Ссылка на login')
    def test_login(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        driver = BasePages(self.driver)
        driver.login()

    @allure.title('вход через ссылку «Личный кабинет»')
    @allure.description('вход через ссылку "Личный Кабинет" в панели навигации')
    # @allure.testcase('ссылка на тест-кейс', 'TestCase-112')
    # @allure.issue('ссылка на баг', 'BUG-113')
    @allure.link("https://stellarburgers.nomoreparties.site/", name='Ссылка на  главную страницу')
    def test_login_personal_account(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        driver = MainPage(self.driver)
        driver.check_click_cabinet()
        driver.click_cabinet()
        driver = BasePages(self.driver)
        driver.login()

    @allure.title('вход по кнопке «Войти в аккаунт» на главной"')
    @allure.description('Проверка Перехода в Личный Кабинет через кнопку "Войти в аккаунт + вход по кнопке «Войти в '
                        'аккаунт» на главной"')
    @allure.link("https://stellarburgers.nomoreparties.site/", name='Ссылка на  главную страницу')
    def test_login_personal_account_btn(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        driver = MainPage(self.driver)
        driver.check_click_cabinet_btn()
        driver.click_cabinet_btn()
        driver = BasePages(self.driver)
        driver.login()

    @allure.title('вход через кнопку в форме регистрации')
    @allure.description('Проверка Перехода в Личный Кабинет через кнопку в форме регистрации')
    @allure.link("https://stellarburgers.nomoreparties.site/", name='Ссылка на  главную страницу')
    def test_login_registration(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        main_page = MainPage(self.driver)
        main_page.check_click_cabinet()
        main_page.click_cabinet()
        personal_account = PersonalAccount(self.driver)
        personal_account.click_link_registration()
        registration = Registration(self.driver)
        registration.click_link_reg()
        base_pages = BasePages(self.driver)
        base_pages.login()

    @allure.title('вход через кнопку в форме восстановления пароля.')
    @allure.description('Проверка Перехода в Личный Кабинет через кнопку в форме восстановления пароля')
    @allure.link("https://stellarburgers.nomoreparties.site/", name='Ссылка на  главную страницу')
    def test_login_recover_password(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        main_page = MainPage(self.driver)
        main_page.check_click_cabinet()
        main_page.click_cabinet()
        personal_account = PersonalAccount(self.driver)
        personal_account.click_recover_password()
        recover_password = RecoverPassword(self.driver)
        recover_password.click_input()
        base_pages = BasePages(self.driver)
        base_pages.login()

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
