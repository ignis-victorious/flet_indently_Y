import flet as ft
from flet import TextField
from flet import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Increment Counter"  # "Hello, Flet!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #  Mode can be 'light' or 'dark'
    page.theme_mode = "dark"

    text_number: TextField = TextField(
        value="0",
        text_align=ft.TextAlign.CENTER,  # .RIGHT,
        width=80,  # =100,
        label="Counter",
        # enabled=False,
    )

    def decrement_counter(event: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def increment_counter(event: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=decrement_counter),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=increment_counter),
            ],
        )
    )
    print(page)


if __name__ == "__main__":
    # Run as a desktop app
    # ft.app(target=main)
    # Run as a web app
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)


# # ft.IconButton(icon="remove", on_pressed=decrement_counter),
#                 ft.IconButton(icon:ft.icons.REMOVE, on_click=decrement_counter),
#                 text_number,
#                 # ft.IconButton(icon="add", on_pressed=increment_counter),
#                 ft.IconButton(icon:ft.icons.ADD, on_click=increment_counter),
# ft.Button(
#                     label="-",
#                     on_click=decrement_counter,
#                     width=50,
#                     height=50,
#                     margin=ft.EdgeInsets.only(right=10),
#                 ),
#                 text_number,
#                 ft.Button(
#                     label="+",
#                     on_click=increment_counter,
#                     width=50,
#                     height=50,
#                     margin=ft.EdgeInsets.only(left=10),
#                 ),
