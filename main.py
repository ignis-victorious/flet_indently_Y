import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Sign-up"  # "Hello, Flet!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #  Mode can be 'light' or 'dark'
    page.theme_mode = ft.ThemeMode.LIGHT  # "dark"
    page.window.width = 400
    page.window.height = 400
    page.window.resizable = False
    print("First leg passed")

    # Fields setup
    text_username = TextField(
        label="Username",
        text_align=ft.TextAlign.START,
        width=200,
        # placeholder="Enter your username",
    )
    text_password = TextField(
        label="Password",
        text_align=ft.TextAlign.START,
        width=200,
        # placeholder="Enter your password",
        password=True,
    )
    checkbox_signup: Checkbox = Checkbox(
        label="I agree to the terms of the contract", value=False
    )
    button_submit: ElevatedButton = ElevatedButton(
        text="Sign up", width=200, height=50, disabled=True
    )
    print("Textes passed")

    #  Check that all fields are filled out before the submit button is enabled!
    def validate(event: ControlEvent) -> None:
        if all([text_username.value and text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

        page.update()

    def submit(event: ControlEvent) -> None:
        print(f"Username: {text_username.value}")
        print(f"Password: {text_password.value}")
        print(f"Sign-up: {checkbox_signup.value}")

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f"Welcome: {text_username.value}", size=20)],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    #  Render the Sing-up page
    page.add(
        Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                Column(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        text_username,
                        text_password,
                        checkbox_signup,
                        button_submit,
                    ],
                    spacing=20,
                )
            ],
        )
    )

    # print(page)


if __name__ == "__main__":
    # Run as a desktop app
    ft.app(target=main)

    # Run as a web app
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)

    # def check_fields():
    #     if text_username.text and text_password.text:
    #         button_submit.disabled = False
    #     else:
    #         button_submit.disabled = True
