import flet as ft

def main(page: ft.Page):
    page.title = "Planta-Scan"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.bgcolor = ft.colors.LIGHT_GREEN_200
    
    # Logo and title
    logo = ft.Image(
        src="Planta-Scan/Planta-Scan/Imagen de WhatsApp 2024-10-02 a las 10.47.28_32377c65.jpg",  # Cambia a la ruta de tu logo
        width=150,
        height=150
    )

    title_text = ft.Text(
        "¡Identificar plantas y sus remedios!",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER
    )

    # Buttons for image upload and capture
    upload_button = ft.ElevatedButton(
        text="Subir Foto",
        icon=ft.icons.UPLOAD_FILE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.colors.GREEN_400,
            color=ft.colors.BLACK,
        )
    )

    capture_button = ft.ElevatedButton(
        text="Tomar Foto",
        icon=ft.icons.CAMERA_ALT,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.colors.GREEN_400,
            color=ft.colors.BLACK,
        )
    )

    # Buttons layout
    button_row = ft.Row(
        controls=[upload_button, capture_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Start button
    start_button = ft.ElevatedButton(
        text="Iniciar Sesión",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.colors.GREEN_600,
            color=ft.colors.WHITE,
        )
    )

    # Informative text
    bottom_text = ft.Text(
        "Inicie sesión para obtener más identificaciones y evaluaciones de salud",
        size=14,
        color=ft.colors.BLACK45,
        text_align=ft.TextAlign.CENTER
    )

    # Layout
    page.add(
        ft.Column(
            controls=[
                logo,
                title_text,
                ft.Text("Comenzar", size=22, weight=ft.FontWeight.BOLD),
                button_row,
                start_button,
                bottom_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)
