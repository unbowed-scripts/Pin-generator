#Библиотеки
import os

#Импорт с других файлов
from Core.core_main_save import save_file_system
from ui.ui_menu import (
    ui_lang_select,
    ui_intro,
    ui_menu,
    ui_error_number,
)

#Выбор языка / Language selection
lang = ui_lang_select()

#текст из intro.txt запуск по Enter
ui_intro(lang)

#Главное меню
while True:

    ui_menu(lang)

    try:
        choice = int(input("➜ "))
    except ValueError:
        ui_error_number(lang)
        continue

    #Выход
    if choice == 0:
        os.system("clear")
        break

    save_file_system(lang, choice)
