import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Increment Counter"  # "Hello, Flet!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #  Mode can be 'light' or 'dark'
    page.theme_mode = "dark"

    text_number: TextField = TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width=100,
        label="Counter",
        enabled=False,
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
            children=[
                ft.IconButton(icons=ft.Icons.REMOVE, on_click=decrement_counter),
                text_number,
                ft.IconButton(icon=ft.Icons.ADD, on_click=increment_counter),
            ],
        )
    )


if __name__ == "__main__":
    ft.ruappn(main)


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
