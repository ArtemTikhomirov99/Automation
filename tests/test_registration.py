import allure
from selenium import webdriver
from pages.registration import Registration


class TestRegistration:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    @allure.title('Регистрация')
    @allure.description('Проверяет успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email '
                        'в формате логин@домен: например, 123@ya.ru.Минимальный пароль — шесть символов.Ошибку для '
                        'некорректного пароля')
    @allure.link("https://stellarburgers.nomoreparties.site/register", name='Ссылка на регистрацию')
    def test_registration(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        driver = Registration(self.driver)
        driver.registration()


    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
