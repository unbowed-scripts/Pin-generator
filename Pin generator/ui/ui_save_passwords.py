from rich import print
from rich.panel import Panel

TEXTS = {
	"ru": {
		"label": "Пароль",
		"success": "Успешно сохранен",
		"title": "Пароль сгенерирован✅",
		"subtitle": "Сохранён в save_password.txt",
	},
	"en": {
		"label": "Password",
		"success": "Successfully saved",
		"title": "Password generated✅",
		"subtitle": "Saved to save_password.txt",
	},
}

_BORDER_STYLES = {16: "green", 32: "yellow", 64: "red", "user": "purple"}


def _show_password_panel(lang, password, border_style):
	t = TEXTS[lang]
	print(
		Panel(
			f"[bold]{t['label']}:[/bold] [bold underline yellow]{password}[/bold underline yellow] [green]{t['success']}[/green]",
			title=f"[bold white] {t['title']}[/bold white]",
			subtitle=f"[bold white]{t['subtitle']}[/bold white]",
			border_style=border_style,
			padding=(1, 3),
		)
	)


def ui_save_password_16(lang, password_16):
	_show_password_panel(lang, password_16, _BORDER_STYLES[16])


def ui_save_password_32(lang, password_32):
	_show_password_panel(lang, password_32, _BORDER_STYLES[32])


def ui_save_password_64(lang, password_64):
	_show_password_panel(lang, password_64, _BORDER_STYLES[64])


def ui_save_password_user(lang, password_user):
	_show_password_panel(lang, password_user, _BORDER_STYLES["user"])
