
from locators.base_pages_locators import BaseLocators


class RecoverPasswordLocators:  # Ссылка на "Восстановление пароля"
    email = BaseLocators.email  # Поле email
    link_input = BaseLocators.link_input  # Ссылка на "Вход"
    text_recover_password = ["xpath", "//h2[text() = 'Восстановление пароля']"]
