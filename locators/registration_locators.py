from locators.base_pages_locators import BaseLocators


class RegistrationLocators:  # Ссылка на регистрацию
    name = ["xpath", '//fieldset[1]//input']  # Имя
    email = ["xpath", '//fieldset[2]//input']  # Эмайл
    password = ["xpath", '//fieldset[3]//input']  # Пароль
    btn_reg = ["xpath", '//*[@id="root"]/div/main/div/form/button']  # Кнопка на регистрацию
    text_registration = ["xpath", "//h2[text() = 'Регистрация']"]
    link_input = BaseLocators.link_input
