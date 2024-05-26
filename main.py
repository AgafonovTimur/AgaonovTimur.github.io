# build for web : flet publish main.py
import flet




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
    def check_number(event):
        button_text.value = user_text_enter.value
        page.update()

    table_number = 7
    square_width = int(1000/table_number)
    square_height = int(1000/table_number)
    table_width = square_width*table_number
    table_height = square_height*table_number
    print(table_width, table_height, square_width, square_height)
    number_of_squares = table_number**2

    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                flet.Container(
                    content=flet.Text(value=str(i)),
                    alignment=flet.alignment.center,
                    width=square_width,
                    height=square_height,
                    bgcolor="#252525",
                    border=flet.border.all(1, "#505050"),

                )
            )
        return items

    page.add(
        flet.Column(
            [
                # flet.Text("4324"),
                flet.Container(
                    content=flet.Column(
                        items(number_of_squares),
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





