import flet as ft
import random

def main(page: ft.Page):
    # Create a list to hold text controls
    text_controls = []
    numbers = list(range(2, 12))  # Numbers from 2 to 11

    # Create text elements for numbers 2 to 11
    for num in numbers:
        text = ft.Text(value=str(num))  # Use TextField for display
        text_controls.append(text)
        page.add(text)
    print(text_controls)

    # Function to shuffle and update text on button click
    def shuffle_texts(e):
        random.shuffle(numbers)  # Shuffle the list of numbers
        for text, num in zip(text_controls, numbers):
            text.value = str(num)
        page.update()

    # Button to trigger text shuffling and updates
    shuffle_button = ft.ElevatedButton(text="Shuffle Numbers", on_click=shuffle_texts)
    page.add(shuffle_button)

    # Run the app
    page.update()

# Run the app with the main function
ft.app(target=main)