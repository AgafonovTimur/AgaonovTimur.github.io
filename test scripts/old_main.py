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

    # Store containers for updating later
    containers = []

    def items(shuffle=False):
        list_of_numbers = list(range(1, number_of_squares + 1))
        if shuffle:
            random.shuffle(list_of_numbers)
        if not containers:  # Create containers if they don't exist
            for num in list_of_numbers:
                container = flet.Container(
                    content=flet.Text(value=str(num), size=47, weight=flet.FontWeight.W_500),
                    alignment=flet.alignment.center,
                    width=square_width,
                    height=square_height,
                    bgcolor="#252525",
                    border=flet.border.all(1, "#505050"),
                )
                containers.append(container)
            return containers
        else:  # Update existing containers
            for container, num in zip(containers, list_of_numbers):
                container.content = flet.Text(value=str(num), size=47, weight=flet.FontWeight.W_500)
            return containers

    def on_keyboard(e: flet.KeyboardEvent):
        if e.key == "H":
            new_items = items(shuffle=True)
            page.update()

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

flet.app(main, view=flet.AppView.WEB_BROWSER)