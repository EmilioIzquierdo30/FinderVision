import flet as ft

def main(page: ft.Page):

    page.title = "Planta-Scan"
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Top bar
    top_bar = ft.Row(
        controls=[
            ft.IconButton(ft.icons.ARROW_BACK, icon_size=30),
            ft.ElevatedButton("Recetario"),
            ft.ElevatedButton("Iniciar Sesión"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Logo section
    logo = ft.Image(
        src="Planta-Scan/Planta-Scan/Imagen de WhatsApp 2024-10-02 a las 10.47.28_32377c65.jpg",  # Cambia por la ruta del logotipo
        width=100,
        height=100
    )

    # Plant image box
    plant_image_box = ft.Container(
        width=200,
        height=200,
        bgcolor=ft.colors.BLACK26,
        border_radius=10
    )

    # Bottom section (camera and search buttons)
    camera_button = ft.IconButton(ft.icons.CAMERA_ALT, icon_size=30)
    search_button = ft.ElevatedButton("Buscar Planta")

    # Layout
    page.add(
        top_bar,
        logo,
        plant_image_box,
        ft.Text("Nombre de la planta", size=18),
        camera_button,
        search_button
    )

ft.app(target=main)
