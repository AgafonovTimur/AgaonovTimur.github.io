import flet
from flet_core import View, RouteChangeEvent, Text, AppBar, ElevatedButton, MainAxisAlignment, CrossAxisAlignment, \
    ViewPopEvent
# ! взять настройки из закоментированного кода снизу

import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


# ft.app(target=main, view=ft.AppView.WEB_BROWSER)


#
# def main(page: flet.Page) -> None:
#     page.title = "page 1"
#     my_param = "xDD"
#
#     def route_change(route):
#         page.views.clear()
#
#         page.views.append(
#             View(
#                 route='/',
#                 controls=[
#                     AppBar(title=Text(value='Home', size=30), bgcolor='orange'),
#                     Text(page.route),
#                     ElevatedButton('store', on_click=lambda _: page.go(f'/store/{my_param}'))
#                 ],
#                 vertical_alignment=MainAxisAlignment.CENTER,
#                 horizontal_alignment=CrossAxisAlignment.CENTER,
#                 spacing=27
#             )
#         )
#
#         # store
#         if page.route == f'/store/{my_param}':
#             page.views.append(
#                 View(
#                     route='/store',
#                     controls=[
#                         AppBar(title=Text('store'), bgcolor='orange'),
#                         Text(page.route),
#                         ElevatedButton(text='go home', on_click=lambda _: page.go('go home'))
#                     ],
#                     vertical_alignment=MainAxisAlignment.CENTER,
#                     horizontal_alignment=CrossAxisAlignment.CENTER,
#                     spacing=27
#                 )
#             )
#
#         def view_pop(e: ViewPopEvent) -> None:
#             page.views.pop()
#             top_view = page.views[-1]
#             page.go(top_view.route)
#
#         page.on_route_change = route_change
#         page.on_view_pop = view_pop
#         page.go(page.route)
#
#
# flet.app(main, view=flet.AppView.WEB_BROWSER)
