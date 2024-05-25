import flet as ft
from flet import (ElevatedButton, IconButton, TextButton, TextField, Checkbox, Page,
                  FilledButton, FloatingActionButton,ControlEvent,Text,
                  Row, KeyboardEvent)


def main(page: Page) -> None:
    page.add(ft.Text("SHULTE123"))
    page.title = "Shulte"
    page.scroll = ft.ScrollMode.HIDDEN
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.update()
    page.window_width = 500
    page.window_height = 500
    page.resizable = True
    #
    # text_username: TextField = TextField(label="Username", text_align=ft.TextAlign.RIGHT, width=100)
    # text_password: TextField = TextField(label="Password", text_align=ft.TextAlign.RIGHT, width=100, password=True)
    # checkbox_remember: Checkbox = Checkbox(label="Remember me", value=False)
    # button_submit: ElevatedButton = ElevatedButton("Submit", width=100, disabled=True)
    # elvButton: TextButton = TextButton("Submit", width=200, height=200, disabled=False)
    # button1: IconButton = IconButton(icon=ft.icons.HELP, tooltip="Help", icon_size=30)
    # button2: TextButton = TextButton("Submit", icon=ft.icons.HELP, icon_color=ft.colors.BLUE)
    # button3: FilledButton = FilledButton("Submit", icon=ft.icons.HELP)
    # button4: FloatingActionButton = FloatingActionButton(icon=ft.icons.ACCESSIBLE_FORWARD, tooltip="Help")
    text: Text = Text(value = "Hello \n app",
                      color = "red",
                      width = 200,
                      size = 50,
                      weight = ft.FontWeight.BOLD,
                      text_align = ft.TextAlign.CENTER,
                      italic = True)

    floating_action_button = ft.FloatingActionButton(width=200,
                                                     height=200,
                                                     bgcolor="#2b2b2b",
                                                     # icon=ft.icons.NUMBERS,
                                                     enable_feedback=False,
                                                     foreground_color="#919191",
                                                     text="Submit",

                                                     focus_color = "#777777",
                                                     # focus_color1.disabled= True,
                                                     # highlight_elevation=0,
                                                     )

# text view after button clicked
    key: Text = Text('key', size=20, color="red")
    shift : Text = Text('shift', size=20, color="orange")
    ctrl : Text = Text('ctrl', size=20, color="cyan")
    alt : Text = Text('alt', size=20, color="blue")
    page.add(key, shift, ctrl, alt)

    page.add(
        ft.Column(
            [
                # text_username,
                # text_password,
                # checkbox_remember,
                # button_submit,
                # elvButton,
                # button1,
                # button2,
                # button3,
                # button4,
                # floating_action_button,
                # text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


# if __name__ == "__main__":
#     ft.app(target=main)  # view=ft.WEB_BROWSER

    def click_button(e : ControlEvent)->None:
        print(e.control.text)
        page.clean()

    # click_button(e: ControlEvent)

# keyboard events
def on_keyboard(e: KeyboardEvent) -> None:
    key.value = e.key
    shift.visible = e.shift
    ctrl.visible = e.ctrl
    alt.visible = e.alt
    print(e.data)
    page.update()

# linking keyboard events to the page
    page.on_keyboard_event = on_keyboard
    page.add(
        Text('press any key'),
        Row(controls=[key, shift, ctrl, alt]),
        alignment=ft.MainAxisAlignment.CENTER
        )



ft.app(target=main)





















