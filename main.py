import flet
import random
import time
import main_logic


def main(page: flet.Page) -> None:
    page.splash = None
    page.title = "Shulte"
    page.scroll = flet.ScrollMode.HIDDEN
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.update()

    # matrix - menu to choose table size
    matrix_amount = 3
    matrix_square_width = int((page.height * 0.7 // 3) - 10)
    matrix_square_height = matrix_square_width
    print(matrix_amount)
    # table_number = matrix_amount
    square_width = int((page.height / matrix_amount) - 10)
    square_height = square_width
    table_width = square_width * matrix_amount
    table_height = square_height * matrix_amount
    number_of_squares = matrix_amount ** 2
    current_number = 1
    square_bgcolor = "#5e5e5e"
    text_color = "#909090"
    background_color = "#222222"
    page.bgcolor = background_color

    # wrong_number_color = "#6d5555"
    # matrix_table_width = matrix_square_width * matrix_squares_amount
    # matrix_table_height = matrix_square_height * matrix_squares_amount
    # matrix_number_of_squares = matrix_squares_amount ** 2

    def matrix_squares():
        list_of_numbers = list(range(2, 11))
        return [
            flet.Container(
                content=flet.Text(value=str(num), size=matrix_square_width * 0.5, color=text_color,
                                  weight=flet.FontWeight.W_700),
                alignment=flet.alignment.center,
                width=matrix_square_width,
                height=matrix_square_height,
                bgcolor=square_bgcolor,
                border=flet.border.all(1.7, background_color),
                border_radius=17,
                data=num,
                on_click=lambda e, num=num: choose_matrix_on_click(e, num)
            )
            for num in list_of_numbers
        ]

    def choose_matrix_on_click(e: flet.TapEvent, num: int):
        table_number = num
        print(num, "matrix selected")
        page.update()
        main_logic.use_data(table_number)
        return table_number

    page.add(flet.Column([
        flet.Container(
            content=flet.Column(matrix_squares(), spacing=0, wrap=True, run_spacing=0),
            bgcolor=background_color,
            width=table_width,
            height=table_height,
        ),
    ]))

flet.app(target=main)
# flet.app(target=main, view=flet.AppView.WEB_BROWSER)
