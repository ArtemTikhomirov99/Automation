from locators.base_pages_locators import BaseLocators


class PersonalAccountLocators:  # class MainPage ведет сюда
    email = BaseLocators.email
    password = BaseLocators.password
    link_registration = ["xpath", '//p[1]/a']  # Ссылка на регистрацию
    link_recover_password = ["xpath", '//*[@id="root"]/div/main/div/div/p[2]/a']  # Ссылка на "Восстановление пароля"
