import flet
import main
import random
import time



table_number = 0
def use_data(n):
    table_number= n
    # received_data = main.main()
    print(f"from main matrix_amount : {n}")
    return table_number

def main(page: flet.Page) -> None:
    page.splash = None
    page.title = "Shulte"
    page.scroll = flet.ScrollMode.HIDDEN
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.update()


    table_number = use_data()
    print(f"table_number : {table_number}")
    square_width = int((page.height / table_number) - 10)
    square_height = square_width
    table_width = square_width * table_number
    table_height = square_height * table_number
    number_of_squares = table_number ** 2
    current_number = 1
    square_bgcolor = "#5e5e5e"
    text_color = "#909090"
    background_color = "#222222"

    # page.bgcolor = background_color
    # wrong_number_color = "#6d5555"
#
    def pass_variables(table_nums):
        table_number = table_nums
        print(table_number)
        square_width = int((page.height / table_number) - 10)
        square_height = square_width
        table_width = square_width * table_number
        table_height = square_height * table_number
        number_of_squares = table_number ** 2

    def items(shuffle=True):
        list_of_numbers = list(range(1, number_of_squares + 1))
        if shuffle:
            random.shuffle(list_of_numbers)
        return [
            flet.Container(
                content=flet.Text(value=str(num), size=square_height * 0.5, color=text_color, weight=flet.FontWeight.W_700),
                alignment=flet.alignment.center,
                width=square_width,
                height=square_height,
                bgcolor=square_bgcolor,
                border=flet.border.all(1.7, background_color),
                border_radius=17,
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
            container.bgcolor = wrong_number_color
            page.update()
            time.sleep(0.17)
            # asyncio.sleep(1)  # Delay to show the wrong selection
            container.bgcolor = square_bgcolor
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

    # page.add(flet.Container)
    page.add(flet.Column([
        flet.Container(
            content=flet.Column(items(), spacing=0, wrap=True, run_spacing=0),
            bgcolor=background_color,
            width=table_width,
            height=table_height,
        )
    ]))
