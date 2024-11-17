import allure
from locators.registration_locators import RegistrationLocators
from generators.generator_email import generate_login
from generators.generator_pass import generate_password


class Registration:  # Ссылка на регистрацию

    def __init__(self, driver):
        self.driver = driver

    # @allure.step('Получение "Name"')
    # def value_name(self):

    @allure.step('Получение "Email"')
    def value_email(self):
        email = generate_login()
        return email

    @allure.step('Получение "Password"')
    def value_password(self):
        password = generate_password()
        return password

    @allure.step('Проверка видимости поля "Name"')
    def check_input_name(self):
        self.driver.find_element(*RegistrationLocators.name).is_displayed()

    @allure.step('ввод в поле "Name"')
    def input_name(self):
        element = self.driver.find_element(*RegistrationLocators.name)
        element.click()
        element.send_keys("Artem")
        email_value = element.get_attribute('value')
        print("Name - Artem")
        assert email_value != ''

    @allure.step('Проверка видимости поля "Email"')
    def check_input_email(self):
        self.driver.find_element(*RegistrationLocators.email).is_displayed()

    @allure.step('ввод в поле "Email"')
    def input_email(self):
        element = self.driver.find_element(*RegistrationLocators.email)
        element.click()
        element.send_keys(self.value_email())
        email_value = element.get_attribute('value')
        print("Email - " + email_value)
        assert email_value != ''

    @allure.step('Проверка видимости поля "Пароль"')
    def check_input_password(self):
        self.driver.find_element(*RegistrationLocators.password).is_displayed()

    @allure.step('ввод в поле "Пароль"')
    def input_password(self):
        element = self.driver.find_element(*RegistrationLocators.password)
        element.click()
        element.send_keys(self.value_password())
        password_value = element.get_attribute('value')
        print("Password - " + password_value)
        assert password_value != ''

    @allure.step('Нажатие на кнопку "Зарегистрироваться')
    def click_reg(self):
        element = self.driver.find_element(*RegistrationLocators.btn_reg)
        element.click()

    @allure.step('Нажатие на ссылку "Зарегистрироваться')
    def click_link_reg(self):
        element = self.driver.find_element(*RegistrationLocators.link_input)
        element.click()

    def registration(self):
        self.check_input_name()
        self.input_name()
        self.check_input_email()
        self.input_email()
        self.check_input_password()
        self.input_password()
        self.click_reg()
