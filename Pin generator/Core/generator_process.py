#Библиотеки
import string
import secrets
from rich import print

TEXTS = {
	"ru": {
		"prompt_length": "Введите длину своего пароля: ",
		"error_min_length": "[bold red]🚫 Ошибка | Длина пароля должна быть не менее 8 символов[/bold red]",
		"error_number": "[bold red]🚫 Ошибка | Введите число[/bold red]",
	},
	"en": {
		"prompt_length": "Enter your password length: ",
		"error_min_length": "[bold red]🚫 Error | Password length must be at least 8 characters[/bold red]",
		"error_number": "[bold red]🚫 Error | Enter a number[/bold red]",
	},
}

#Пароль на 16 символов
def generate_password_16(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

#Пароль на 32 символа
def generate_password_32(length=32):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

#Пароль на 64 символа
def generate_password_64(length=64):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

#Пароль пользовательской длины
def generate_password_user(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Длина пароля пользователя
def user_length(lang="ru"):
    t = TEXTS[lang]
    while True:
        try:
            length_user = int(input(t["prompt_length"]))

            if length_user < 8:
                print(t["error_min_length"])
                continue

            return length_user

        except ValueError:
            print(t["error_number"])
