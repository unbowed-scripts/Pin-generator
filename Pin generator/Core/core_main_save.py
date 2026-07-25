#Библиотеки
import os
from rich import print
from rich.panel import Panel

#Импорт с других файлов
from Core.generator_process import (
    generate_password_16,
    generate_password_32,
    generate_password_64,
    generate_password_user,
    user_length,
)
from ui.ui_save_passwords import (
    ui_save_password_16,
    ui_save_password_32,
    ui_save_password_64,
    ui_save_password_user,
)
from ui.ui_menu import (
    ui_error_save_password,
    ui_error_find,
    ui_press_enter,
)

PASSWORD_FILE = "save_password.txt"

TEXTS = {
    "ru": {
        "length_label": "Длина",
        "my_passwords_title": "Мои пароли",
    },
    "en": {
        "length_label": "Length",
        "my_passwords_title": "My passwords",
    },
}


def save_file_system(lang, choice):
    t = TEXTS[lang]

    #Пароль на 16 символов
    if choice == 1:
        os.system("cls" if os.name == "nt" else "clear")
        password_16 = generate_password_16()

        with open(PASSWORD_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{t['length_label']} | 16] {password_16}\n")

        ui_save_password_16(lang, password_16)
        ui_press_enter(lang)

    #Пароль на 32 символа
    elif choice == 2:
        os.system("cls" if os.name == "nt" else "clear")
        password_32 = generate_password_32()

        with open(PASSWORD_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{t['length_label']} | 32] {password_32}\n")

        ui_save_password_32(lang, password_32)
        ui_press_enter(lang)

    #Пароль на 64 символа
    elif choice == 3:
        os.system("cls" if os.name == "nt" else "clear")
        password_64 = generate_password_64()

        with open(PASSWORD_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{t['length_label']} | 64] {password_64}\n")

        ui_save_password_64(lang, password_64)
        ui_press_enter(lang)

    #Длина пароля пользователя
    elif choice == 4:
        os.system("cls" if os.name == "nt" else "clear")
        length = user_length(lang)
        password_user = generate_password_user(length)

        with open(PASSWORD_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{t['length_label']} | {length}] {password_user}\n")

        ui_save_password_user(lang, password_user)
        ui_press_enter(lang)

    #Мои пароли
    elif choice == 5:
        os.system("cls" if os.name == "nt" else "clear")

        if os.path.exists(PASSWORD_FILE):
            with open(PASSWORD_FILE, "r", encoding="utf-8") as file:
                saved = file.read()

            if saved.strip():
                print(Panel(saved, title=f"[bold white]{t['my_passwords_title']}[/bold white]", border_style="bright_cyan", padding=(1, 3)))
            else:
                ui_error_save_password(lang)
        else:
            ui_error_save_password(lang)

        ui_press_enter(lang)

    else:
        ui_error_find(lang)
        ui_press_enter(lang)
