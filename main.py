# build for web : flet publish main.py
import flet
import random



def main(page: flet.Page) -> None:
    # page.add(flet.Text("SHULTE123"))
    page.title = "Shulte"
    # flet.ThemeMode.DARK
    page.scroll = flet.ScrollMode.HIDDEN
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    # page.bgcolor = "#272727"

    page.horizontal_alignment = 'center'
    page.update()
    # page.window_width = 500
    # page.window_height = 500
    # page.add(flet.Column())
    # page.resizable = False

    button_text = flet.Text("Add")
    user_text_enter = flet.TextField( value="0", width=150, text_align=flet.TextAlign.CENTER)
    # def check_number(event):
    #     button_text.value = user_text_enter.value
    #     page.update()

    table_number = 5
    square_width = int((page.height/table_number) - 10)
    square_height = int((page.height/table_number) - 10)
    table_width = square_width*table_number
    table_height = square_height*table_number
    print(table_width, table_height, square_width, square_height)
    number_of_squares = table_number**2

    def items():
        list_of_numbers = []
        for i in range(number_of_squares):
            list_of_numbers.append(int(i) + 1)
        shuffling =  random.shuffle(list_of_numbers)
        print(list_of_numbers,len(list_of_numbers))

        items = []
        for i in range(0, len(list_of_numbers)):
            items.append(
                flet.Container(
                    content=flet.Text(value=str(list_of_numbers[i]),
                                      size=47,
                                      weight=flet.FontWeight.W_500),
                    alignment=flet.alignment.center,
                    width=square_width,
                    height=square_height,
                    bgcolor="#252525",
                    border=flet.border.all(1, "#505050"),

                )
            )
        return items

    def on_keyboard(e: flet.KeyboardEvent):
        if e.key == "H":
            # items()
            page.clean()
            page.add(
                flet.Column(
                    [
                        # flet.Text("4324"),
                        flet.Container(
                            content=flet.Column(
                                items(),
                                spacing=0,
                                wrap=True,
                                run_spacing=0,
                            ),
                            bgcolor="#989898",
                            width=table_width,
                            height=table_height,
                        ),
                    ],
                ),
            )
            page.update()
        else:
            print(e.key)


    page.on_keyboard_event = on_keyboard


    # def change_text_in_squares():
    #     pass
    # ! after resize page
    # def page_resize(e):
    #     print("New page size:", page.window_width, page.window_height)
    # page.on_resize = page_resize

    page.add(
        flet.Column(
            [
                # flet.Text("4324"),
                flet.Container(
                    content=flet.Column(
                        items(),
                        spacing=0,
                        wrap=True,
                        run_spacing=0,
                    ),
                    bgcolor="#989898",
                    width=table_width,
                    height=table_height,
                ),
            ],
        ),
    )

# flet.app(target=main)
flet.app(main, view=flet.AppView.WEB_BROWSER)





