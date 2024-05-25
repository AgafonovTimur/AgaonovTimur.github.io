# https://www.youtube.com/watch?v=ku_HZdgaOF8&list=PL4KX3oEgJcfdiE-S3qLqATrsMg2Nddosx&index=5
import flet as ft
from flet import (UserControl, Text, Row, Page, ControlEvent, MainAxisAlignment, ElevatedButton, KeyboardEvent)


class IncremetCounter(UserControl):

    def __init__(self, text: str, start_number: int = 0) -> None:
        super().__init__()
        self.text = text
        self.counter = start_number
        self.text_number: Text = Text(value=str(start_number), size=20, color="red")

    def increment(self, e: ControlEvent) -> None:
        self.counter += 1
        self.text_number.value = str(self.counter)
        self.update()

    def build(self) -> Row:
        return Row(controls=[ElevatedButton(text=self.text, on_click=self.increment), self.text_number],
                   alignment=MainAxisAlignment.SPACE_BETWEEN,
                   width=300)

def main(page: Page) -> None:
    page.add(ft.Text("SHULTE123"))
    page.title = "Shulte"
    page.scroll = ft.ScrollMode.HIDDEN
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_width = 500
    page.window_height = 500

    page.add(IncremetCounter("Increment"))





# ft.app(target=main)





















