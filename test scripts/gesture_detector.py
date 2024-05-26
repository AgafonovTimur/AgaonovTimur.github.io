import flet as ft

def main(page: ft.Page):

    def change_text(e):
        text.value = e
        text.update()

    page.add(
        ft.Container(
            height=50,
            width=50,
            content=ft.GestureDetector(
                on_tap=lambda e: change_text("On Release"),
            ),
            bgcolor="red",
            on_click=lambda e: change_text("On Click"),
            ink=True,
        ),
        text := ft.Text("Test text"),
    )


ft.app(target=main)