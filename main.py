import flet



def main(page: flet.Page) -> None:
    # page.add(flet.Text("SHULTE123"))
    page.title = "Shulte"
    # flet.ThemeMode.DARK
    # page.scroll = flet.ScrollMode.HIDDEN
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    page.horizontal_alignment = 'center'
    page.update()
    # page.window_width = 500
    # page.window_height = 500
    # page.add(flet.Column())
    # page.resizable = False

    page.add(
        # 1
        flet.Row(
            [
                flet.IconButton(flet.icons.HOME),
                flet.Icon(flet.icons.SETTINGS),
                flet.FloatingActionButton(text="Add",
                                          bgcolor=flet.colors.BROWN_900,
                                          foreground_color=flet.colors.ORANGE),
                flet.IconButton(flet.icons.HOME),
                flet.Icon(flet.icons.SETTINGS),
                flet.FloatingActionButton(text="Add",
                                          bgcolor=flet.colors.BROWN_900,
                                          foreground_color=flet.colors.ORANGE),
                flet.Text("SHULTE123")
            ],
            alignment=flet.MainAxisAlignment.CENTER,
        ),
        # 2
    flet.Row(
        [
            flet.IconButton(flet.icons.HOME),
            flet.Icon(flet.icons.SETTINGS),
            flet.FloatingActionButton(text="Add",
                                      bgcolor=flet.colors.BROWN_900,
                                      foreground_color=flet.colors.ORANGE),
            flet.IconButton(flet.icons.HOME),
            flet.Icon(flet.icons.SETTINGS),
            flet.FloatingActionButton(text="Add",
                                      bgcolor=flet.colors.BROWN_900,
                                      foreground_color=flet.colors.ORANGE),
            flet.Text("SHULTE123")
        ],
        alignment=flet.MainAxisAlignment.CENTER,
    ),
        # 3
        flet.Row(
            [
                flet.IconButton(flet.icons.HOME),
                flet.Icon(flet.icons.SETTINGS),
                flet.FloatingActionButton(text="Add",
                                          bgcolor=flet.colors.BROWN_900,
                                          foreground_color=flet.colors.ORANGE),
                flet.IconButton(flet.icons.HOME),
                flet.Icon(flet.icons.SETTINGS),
                flet.FloatingActionButton(text="Add",
                                          bgcolor=flet.colors.BROWN_900,
                                          foreground_color=flet.colors.ORANGE),
                flet.Text("SHULTE123")
            ],
            alignment=flet.MainAxisAlignment.CENTER,
        ),
        # 4
        flet.Row(
            [
                flet.IconButton(flet.icons.HOME),
                flet.Icon(flet.icons.SETTINGS),
                flet.FloatingActionButton(text="Add",
                                          bgcolor=flet.colors.BROWN_900,
                                          foreground_color=flet.colors.ORANGE),
                flet.IconButton(flet.icons.HOME),
                flet.Icon(flet.icons.SETTINGS),
                flet.FloatingActionButton(text="Add",
                                          bgcolor=flet.colors.BROWN_900,
                                          foreground_color=flet.colors.ORANGE),
                flet.Text("SHULTE123")
            ],
            alignment=flet.MainAxisAlignment.CENTER,
        ),
        # 5
        flet.Row(
            [
                flet.IconButton(flet.icons.HOME),
                flet.Icon(flet.icons.SETTINGS),
                flet.FloatingActionButton(text="Addd",
                                          bgcolor=flet.colors.BROWN_900,
                                          foreground_color=flet.colors.ORANGE),
                flet.IconButton(flet.icons.HOME),
                flet.Icon(flet.icons.SETTINGS),
                flet.FloatingActionButton(text="Add", height=150,
                                          bgcolor=flet.colors.BROWN_900,
                                          foreground_color=flet.colors.ORANGE),
                flet.Text("SHULTE123",text_align=flet.TextAlign.CENTER)
            ],
            alignment=flet.MainAxisAlignment.CENTER,
        )
    )


flet.app(main, view=flet.AppView.WEB_BROWSER)


#
#
# import flet
#
#
# def main(page: flet.Page):
#     page.title = "Flet counter example"
#     page.theme_mode = flet.ThemeMode.DARK
#     page.vertical_alignment = flet.MainAxisAlignment.CENTER
#
#     txt_number = flet.TextField(value="0", text_align=flet.TextAlign.RIGHT, width=100)
#
#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()
#
#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()
#
#     page.add(
#         flet.Row(
#             [
#                 flet.IconButton(flet.icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 flet.FloatingActionButton(text="Add",
#                                             bgcolor=flet.colors.BROWN_900,
#                                             foreground_color=flet.colors.ORANGE),
#                 flet.IconButton(flet.icons.ADD, on_click=plus_click),
#             ],
#             alignment=flet.MainAxisAlignment.CENTER,
#         ),
#
#     flet.Text("SHULTE123"),
#     flet.Text
#     )
#
#
# flet.app(main, view=flet.AppView.WEB_BROWSER)
#
#
#
#
#
#
#
#




