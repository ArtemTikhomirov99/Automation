import random
import string


def generate_password(length=12):
    """Генерирует случайный пароль заданной длины."""
    if length < 6:
        raise ValueError("Пароль должен быть не менее 6 символов.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))

    # Убедимся, что пароль содержит хотя бы одну заглавную букву, одну строчную букву, одну цифру и один специальный
    # символ
    while not (any(c.islower() for c in password) and
               any(c.isupper() for c in password) and
               any(c.isdigit() for c in password) and
               any(c in string.punctuation for c in password)):
        password = ''.join(random.choices(characters, k=length))

    file = open("generators/resource/Password.txt", "w+")
    try:
        file.write(password)  # работа с файлом
    finally:
        file.close()
    return password



