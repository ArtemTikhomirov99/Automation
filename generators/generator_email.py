import random
import string


def generate_login():
    """Генерирует случайный логин в формате email."""
    prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = "ya.ru"
    email = f"{prefix}@{domain}"
    file = open("generators/resource/Email.txt", "w+")
    try:
        file.write(email)  # работа с файлом
    finally:
        file.close()
    return email
