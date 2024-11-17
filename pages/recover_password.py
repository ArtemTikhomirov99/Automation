import allure
from locators.recover_password_locators import RecoverPasswordLocators
from locators.base_pages_locators import BaseLocators


class RecoverPassword:  # Ссылка на "Восстановление пароля"

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажатие на ссылку "войти"')
    def click_input(self):
        element = self.driver.find_element(*RecoverPasswordLocators.link_input)
        element.click()
        assert self.driver.find_element(*BaseLocators.btn_input), "Ожидает кнопку 'Войти'"
