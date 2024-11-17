import allure
from locators.base_pages_locators import BaseLocators


class BasePages:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получение "Email"')
    def value_email(self):
        with open('./generators/resource/Email.txt', 'r') as file:
            email = file.read().strip()
            return email

    @allure.step('Получение "Password"')
    def value_password(self):
        with open('./generators/resource/Password.txt', 'r') as file:
            password = file.read().strip()
            return password

    @allure.step('Проверка видимости поля "Email"')
    def check_input_email(self):
        self.driver.find_element(*BaseLocators.email).is_displayed()

    @allure.step('ввод в поле "Email"')
    def input_email(self):
        element = self.driver.find_element(*BaseLocators.email)
        element.click()
        element.send_keys(self.value_email())
        email_value = element.get_attribute('value')
        print("Email - " + email_value)
        assert email_value != ''

    @allure.step('Проверка видимости поля "Пароль"')
    def check_input_password(self):
        self.driver.find_element(*BaseLocators.password).is_displayed()

    @allure.step('ввод в поле "Пароль"')
    def input_password(self):
        element = self.driver.find_element(*BaseLocators.password)
        element.click()
        element.send_keys(self.value_password())
        password_value = element.get_attribute('value')
        print("Password - " + password_value)
        assert password_value != ''

    @allure.step('Нажатие на кнопку "Войти"')
    def click_input(self):
        self.driver.find_element(*BaseLocators.btn_input).click()

    def login(self):
        self.check_input_email()
        self.input_email()
        self.check_input_password()
        self.input_password()
        self.click_input()
