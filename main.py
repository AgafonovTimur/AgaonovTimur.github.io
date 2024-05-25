import flet
from flet import *



def main(page) -> None:
    page.add(flet.Text("SHULTE123"))
    page.title = "Shulte"
    page.theme_mode = 'dark'
    page.scroll = flet.ScrollMode.HIDDEN
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.update()
    # page.window_width = 500
    # page.window_height = 500
    # page.add(flet.Column())
    page.resizable = False

    page.add(
        # 1
        flet.Row(
            [
                flet.IconButton(flet.icons.HOME),
                flet.Icon(flet.icons.SETTINGS),
                # flet.FloatingActionButton(text="Add",
                #                           bgcolor=flet.colors.BROWN_900,
                #                           foreground_color=flet.colors.ORANGE),
                # flet.IconButton(flet.icons.HOME),
                # flet.Icon(flet.icons.SETTINGS),
                # flet.FloatingActionButton(text="Add",
                #                           bgcolor=flet.colors.BROWN_900,
                #                           foreground_color=flet.colors.ORANGE),
                flet.Text("SHULTE123")
            ],
            alignment=flet.MainAxisAlignment.CENTER,
    #     ),
    #     # 2
    # flet.Row(
    #     [
    #         flet.IconButton(flet.icons.HOME),
    #         flet.Icon(flet.icons.SETTINGS),
    #         flet.FloatingActionButton(text="Add",
    #                                   bgcolor=flet.colors.BROWN_900,
    #                                   foreground_color=flet.colors.ORANGE),
    #         flet.IconButton(flet.icons.HOME),
    #         flet.Icon(flet.icons.SETTINGS),
    #         flet.FloatingActionButton(text="Add",
    #                                   bgcolor=flet.colors.BROWN_900,
    #                                   foreground_color=flet.colors.ORANGE),
    #         flet.Text("SHULTE123")
    #     ],
    #     alignment=flet.MainAxisAlignment.CENTER,
    # ),
    #     # 3
    #     flet.Row(
    #         [
    #             flet.IconButton(flet.icons.HOME),
    #             flet.Icon(flet.icons.SETTINGS),
    #             flet.FloatingActionButton(text="Add",
    #                                       bgcolor=flet.colors.BROWN_900,
    #                                       foreground_color=flet.colors.ORANGE),
    #             flet.IconButton(flet.icons.HOME),
    #             flet.Icon(flet.icons.SETTINGS),
    #             flet.FloatingActionButton(text="Add",
    #                                       bgcolor=flet.colors.BROWN_900,
    #                                       foreground_color=flet.colors.ORANGE),
    #             flet.Text("SHULTE123")
    #         ],
    #         alignment=flet.MainAxisAlignment.CENTER,
    #     ),
    #     # 4
    #     flet.Row(
    #         [
    #             flet.IconButton(flet.icons.HOME),
    #             flet.Icon(flet.icons.SETTINGS),
    #             flet.FloatingActionButton(text="Add",
    #                                       bgcolor=flet.colors.BROWN_900,
    #                                       foreground_color=flet.colors.ORANGE),
    #             flet.IconButton(flet.icons.HOME),
    #             flet.Icon(flet.icons.SETTINGS),
    #             flet.FloatingActionButton(text="Add",
    #                                       bgcolor=flet.colors.BROWN_900,
    #                                       foreground_color=flet.colors.ORANGE),
    #             flet.Text("SHULTE123")
    #         ],
    #         alignment=flet.MainAxisAlignment.CENTER,
    #     ),
    #     # 5
    #     flet.Row(
    #         [
    #             flet.IconButton(flet.icons.HOME),
    #             flet.Icon(flet.icons.SETTINGS),
    #             flet.FloatingActionButton(text="Addd",
    #                                       bgcolor=flet.colors.BROWN_900,
    #                                       foreground_color=flet.colors.ORANGE),
    #             flet.IconButton(flet.icons.HOME),
    #             flet.Icon(flet.icons.SETTINGS),
    #             flet.FloatingActionButton(text="Add", height=150,
    #                                       bgcolor=flet.colors.BROWN_900,
    #                                       foreground_color=flet.colors.ORANGE),
    #             flet.Text("SHULTE123",text_align=flet.TextAlign.CENTER)
    #         ],
    #         alignment=flet.MainAxisAlignment.CENTER,
        )
    )


# if __name__ == "__main__":

# flet.app(target=main)

if __name__ == "__main__":
    flet.app(target=main, view=flet.AppView.WEB_BROWSER)

















