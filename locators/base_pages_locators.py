
class BaseLocators:
    link_input = ["xpath", "//a[text() = 'Войти']"]  # Ссылка на "Вход" переносит в class PersonalAccount
    email = ["xpath", '//fieldset[1]//input']  # Поле email
    password = ["xpath", '//fieldset[2]//input']  # Поле пароль
    btn_input = ["xpath", "//button[text() = 'Войти']"]