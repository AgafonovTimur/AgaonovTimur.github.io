import flet
import random

def main(page: flet.Page) -> None:
    page.splash = None
    page.title = "Shulte"
    page.scroll = flet.ScrollMode.HIDDEN
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.update()

    table_number = 5
    square_width = int((page.height / table_number) - 10)
    square_height = square_width
    table_width = square_width * table_number
    table_height = square_height * table_number
    number_of_squares = table_number ** 2
    current_number = 1

    def items(shuffle=True):
        list_of_numbers = list(range(1, number_of_squares + 1))
        if shuffle:
            random.shuffle(list_of_numbers)
        return [
            flet.Container(
                content=flet.Text(value=str(num), size=47, weight=flet.FontWeight.W_500),
                alignment=flet.alignment.center,
                width=square_width,
                height=square_height,
                bgcolor="#252525",
                border=flet.border.all(1, "#505050"),
                data=num,
                on_click=lambda e, num=num: on_square_click(e, num)
            )
            for num in list_of_numbers
        ]

    def on_square_click(e: flet.TapEvent, num: int):
        nonlocal current_number
        container = e.control
        if num == current_number:
            container.content = None
            page.update()
            current_number += 1
            if current_number > number_of_squares:
                reset_game()
        else:
            container.bgcolor = "#450a0a"
            page.update()
            # asyncio.sleep(0.5)  # Delay to show the wrong selection
            container.bgcolor = "#252525"
            page.update()

    def reset_game():
        nonlocal current_number
        current_number = 1
        new_items = items(shuffle=True)
        page.clean()
        page.add(flet.Column([
            flet.Container(
                content=flet.Column(new_items, spacing=0, wrap=True, run_spacing=0),
                bgcolor="#989898",
                width=table_width,
                height=table_height,
            ),
        ]))
        page.update()

    def on_keyboard(e: flet.KeyboardEvent):
        if e.key == "H":
            nonlocal current_number
            current_number = 1  # Reset the current number
            reset_game()  # Call reset_game to shuffle and update UI

    page.on_keyboard_event = on_keyboard

    # Initial display
    initial_items = items()
    page.add(flet.Column([
        flet.Container(
            content=flet.Column(initial_items, spacing=0, wrap=True, run_spacing=0),
            bgcolor="#989898",
            width=table_width,
            height=table_height,
        ),
    ]))

# flet.app(target=main)
flet.app(target=main, view=flet.AppView.WEB_BROWSER)