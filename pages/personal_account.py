import allure
from locators.personal_account_locators import PersonalAccountLocators
from locators.registration_locators import RegistrationLocators
from locators.recover_password_locators import RecoverPasswordLocators


class PersonalAccount:  # class MainPage ведет сюда

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверка доступности ссылки "Зарегистрироваться"')
    def check_click_email(self):
        self.driver.find_element(*PersonalAccountLocators.link_registration).is_displayed()

    @allure.step('Нажатие на ссылку "Зарегистрироваться"')
    def click_link_registration(self):
        element = self.driver.find_element(*PersonalAccountLocators.link_registration)
        element.click()
        assert self.driver.find_element(*RegistrationLocators.text_registration), "Ожидает текст 'Регистрация'"

    @allure.step('Проверка доступности ссылки "Восстановить пароль"')
    def check_click_recover_password(self):
        self.driver.find_element(*PersonalAccountLocators.link_recover_password).is_displayed()

    @allure.step('Нажатие на ссылку "Восстановить пароль"')
    def click_recover_password(self):
        element = self.driver.find_element(*PersonalAccountLocators.link_recover_password)
        element.click()
        assert self.driver.find_element(*RecoverPasswordLocators.text_recover_password), "Ожидает текст " \
                                                                                         "'Восстановление пароля'"
