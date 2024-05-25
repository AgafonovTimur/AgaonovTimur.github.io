# https://www.youtube.com/watch?v=KFZ_fO_HCMA&list=PL4KX3oEgJcfdiE-S3qLqATrsMg2Nddosx&index=4
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

    text: Text = Text(value = "Hello \n app",
                      color = "red",
                      width = 200,
                      size = 50,
                      weight = ft.FontWeight.BOLD,
                      text_align = ft.TextAlign.CENTER,
                      italic = True)



# text view after button clicked
    key: Text = Text('key', size=20, color="red")
    shift : Text = Text('shift', size=20, color="orange")
    ctrl : Text = Text('ctrl', size=20, color="cyan")
    alt : Text = Text('alt', size=20, color="green")
    page.add(key, shift, ctrl, alt)




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
            # alignment=ft.MainAxisAlignment.CENTER
        )



# ft.app(target=main)
#




















