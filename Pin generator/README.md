# RUSSIAN
# Pin Generator

Консольная программа на Python для генерации и хранения надёжных паролей.

## Возможности

- Генерация пароля длиной 16, 32 или 64 символа
- Генерация пароля произвольной длины (от 8 символов)
- Сохранение всех сгенерированных паролей в `save_password.txt`
- Просмотр ранее сохранённых паролей
- Приветственный экран при запуске с текстом из файла `intro.txt`
- Выбор языка интерфейса при запуске: русский / английский (ru / en)

## Структура проекта

```
Pin generator/
├── Main.py                     # Точка входа
├── intro.txt                   # Текст приветственного экрана (редактируется вручную)
├── save_password.txt           # Файл с сохранёнными паролями (создаётся автоматически)
├── Core/
│   ├── generator_process.py    # Логика генерации паролей
│   └── core_main_save.py       # Обработка выбора в меню, сохранение паролей
└── ui/
    ├── ui_menu.py               # Главное меню и приветственный экран
    └── ui_save_passwords.py     # Оформление вывода сгенерированного пароля
```

## Установка

Требуется Python 3.8+.

```bash
pip install rich pyfiglet
```

## Запуск

```bash
python Main.py
```

### Как это работает

1. При запуске сначала предлагается выбрать язык интерфейса:
   `1` — русский, `2` — English.
2. Затем показывается приветственный экран — его текст берётся из файла
   `intro.txt` (секции `#Rusian` / `#English` внутри него подставляются
   автоматически в зависимости от выбранного языка). Отредактируйте этот
   файл своим текстом, он будет отображаться при каждом запуске.
3. Нажмите **Enter**, чтобы продолжить — откроется главное меню генератора.
4. В главном меню выберите пункт (0–5) и нажмите Enter для подтверждения.

Весь остальной интерфейс (меню, сообщения об ошибках, подписи к
сгенерированным паролям) тоже переключается на выбранный язык.

## Меню

| Пункт | Действие                       |
|-------|---------------------------------|
| 1     | Сгенерировать пароль на 16 символов |
| 2     | Сгенерировать пароль на 32 символа  |
| 3     | Сгенерировать пароль на 64 символа  |
| 4     | Сгенерировать пароль произвольной длины (от 8 символов) |
| 5     | Показать ранее сохранённые пароли |
| 0     | Выход из программы |


# English 
# Pin Generator
A console application in Python for generating and storing secure passwords.
## Features
- Generate a password of 16, 32, or 64 characters
- Generate a password of arbitrary length (8 characters or more)
- Save all generated passwords to `save_password.txt`
- View previously saved passwords
- Welcome screen on startup with text from the `intro.txt` file
- Choice of interface language at startup: Russian / English (ru / en)
## Project Structure
```
Pin generator/
├── Main.py                     # Entry point
├── intro.txt                   # Welcome screen text (edited manually)
├── save_password.txt           # File with saved passwords (created automatically)
├── Core/
│   ├── generator_process.py    # Password generation logic
│   └── core_main_save.py       # Menu selection handling, password saving
└── ui/
├── ui_menu.py               # Main menu and welcome screen
└── ui_save_passwords.py     # Formatting for the generated password output
```
## Installation
Requires Python 3.8+.
```bash
pip install rich pyfiglet
```
## Running
```bash
python Main.py
```
### How it works
1. On startup, you're first asked to choose the interface language:
`1` — Russian, `2` — English.
2. Then a welcome screen is shown — its text is taken from the
`intro.txt` file (the `#Rusian` / `#English` sections inside it are
substituted automatically depending on the chosen language). Edit this
file with your own text; it will be displayed on every run.
3. Press **Enter** to continue — the generator's main menu will open.
4. In the main menu, choose an option (0–5) and press Enter to confirm.
The rest of the interface (menu, error messages, labels for
generated passwords) also switches to the chosen language.
## Menu
| Option | Action                       |
|-------|---------------------------------|
| 1     | Generate a 16-character password |
| 2     | Generate a 32-character password  |
| 3     | Generate a 64-character password  |
| 4     | Generate a password of arbitrary length (8 characters or more) |
| 5     | Show previously saved passwords |
| 0     | Exit the program |
