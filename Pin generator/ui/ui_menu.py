#Library / Библиотеки
from rich.console import Console
from rich import print
from rich.panel import Panel
import pyfiglet
import os

#Тексты интерфейса на двух языках / UI texts in two languages
TEXTS = {
	"ru": {
		"welcome_title": "Добро пожаловать",
		"subtitle": "Интересние скрипты: t.me/unbowed_scripts",
		"intro_default": "Добро пожаловать!\nОтредактируйте файл intro.txt, чтобы изменить этот текст.",
		"press_enter": "\nНажми Enter чтобы продолжить: ",
		"lang_prompt_title": "Выберите язык / Select language",
		"lang_prompt_body": "[bold]1[/bold] — Русский\n[bold]2[/bold] — English",
		"lang_error": "[bold red]🚫 Введите 1 или 2[/bold red]",
		"menu": """
[bold green][1]Пароль | 16 символов[/bold green]
[bold yellow][2]Пароль | 32 символов[/bold yellow]
[bold red][3]Пароль | 64 символов[/bold red]

[bold purple][4]Своя длинна[/bold purple]

[bold bright_cyan][5]Мои пароли[/bold bright_cyan]

[bold bright_blue][0]Выход [/bold bright_blue]
	""",
		"error_number": "[bold red] 🚫 Error | Введите число [/bold red]",
		"error_save_password": "[bold red]🚫 Пока нет сохранённых паролей[/bold red]",
		"error_find": "[bold red] 🚫 Error | Такого пункта меню нет [/bold red]",
	},
	"en": {
		"welcome_title": "Welcome",
		"subtitle": "Cool scripts: t.me/unbowed_scripts",
		"intro_default": "Welcome!\nEdit the intro.txt file to change this text.",
		"press_enter": "\nPress Enter to continue: ",
		"lang_prompt_title": "Выберите язык / Select language",
		"lang_prompt_body": "[bold]1[/bold] — Русский\n[bold]2[/bold] — English",
		"lang_error": "[bold red]🚫 Enter 1 or 2[/bold red]",
		"menu": """
[bold green][1]Password | 16 characters[/bold green]
[bold yellow][2]Password | 32 characters[/bold yellow]
[bold red][3]Password | 64 characters[/bold red]

[bold purple][4]Custom length[/bold purple]

[bold bright_cyan][5]My passwords[/bold bright_cyan]

[bold bright_blue][0]Exit [/bold bright_blue]
	""",
		"error_number": "[bold red] 🚫 Error | Enter a number [/bold red]",
		"error_save_password": "[bold red]🚫 No saved passwords yet[/bold red]",
		"error_find": "[bold red] 🚫 Error | No such menu item [/bold red]",
	},
}


#Выбор языка при запуске / Language selection on startup
def ui_lang_select():
	os.system("cls" if os.name == "nt" else "clear")

	text = pyfiglet.figlet_format("PIN GENERATOR", font="slant")
	print(text)

	print(
		Panel(
			TEXTS["ru"]["lang_prompt_body"],
			title=f"[bold white]{TEXTS['ru']['lang_prompt_title']}[/bold white]",
			border_style="bright_cyan",
			padding=(1, 3),
		)
	)

	while True:
		choice = input("➜ ").strip().lower()

		if choice in ("1", "ru", "рус", "русский"):
			return "ru"
		elif choice in ("2", "en", "eng", "english"):
			return "en"

		print(TEXTS["ru"]["lang_error"])


#Достаёт нужную секцию (#Rusian / #English) из intro.txt / Extracts the matching section from intro.txt
def _extract_intro_section(raw_text, lang):
	marker = "#Rusian" if lang == "ru" else "#English"
	other_marker = "#English" if lang == "ru" else "#Rusian"

	if marker in raw_text:
		section = raw_text.split(marker, 1)[1]
		if other_marker in section:
			section = section.split(other_marker, 1)[0]
		return section.strip()

	return raw_text.strip()


#Экран приветствия / Intro screen — читает текст из intro.txt и ждёт Enter
def ui_intro(lang, intro_file="intro.txt"):
	os.system("cls" if os.name == "nt" else "clear")

	t = TEXTS[lang]
	text = pyfiglet.figlet_format("PIN GENERATOR", font="slant")
	print(text)

	if os.path.exists(intro_file):
		with open(intro_file, "r", encoding="utf-8") as file:
			raw = file.read()
		intro_text = _extract_intro_section(raw, lang)
	else:
		intro_text = t["intro_default"]

	print(
		Panel(
			intro_text,
			title=f"[bold white]{t['welcome_title']}[/bold white]",
			subtitle=t["subtitle"],
			border_style="bright_cyan",
			padding=(1, 3),
		)
	)

	input(t["press_enter"])
	os.system("cls" if os.name == "nt" else "clear")


#Ui main menu / Дизайн главного меню
def ui_menu(lang):
	t = TEXTS[lang]

	#Большой текст PIN GENERATOR / Стиль slant
	text = pyfiglet.figlet_format("PIN GENERATOR", font="slant")
	print(text)
	print(
		Panel(
			t["menu"],
			subtitle=t["subtitle"],
		)
	)


# Enter to continue / Нажмите Enter
def ui_press_enter(lang):
	input(TEXTS[lang]["press_enter"])


#Errors / ошибки
def ui_error_number(lang):
	print(TEXTS[lang]["error_number"])


def ui_error_save_password(lang):
	print(TEXTS[lang]["error_save_password"])


def ui_error_find(lang):
	print(TEXTS[lang]["error_find"])
