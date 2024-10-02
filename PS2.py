import flet as ft

def main(page: ft.Page):
    page.title = "Planta-Scan"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.bgcolor = ft.colors.LIGHT_GREEN_200

    # Logo Planta-Scan
    logo = ft.Image(
        src="Planta-Scan/Planta-Scan/Planta-Scan.png",  # Cambia esta ruta por la de tu logo
        width=180,
        height=180
    )

    # Texto principal
    title_text = ft.Text(
        "¡Reconoce las plantas medicinales a través de imágenes!",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.LEFT
    )

    # Texto secundario
    subtitle_text = ft.Text(
        "Descubre sus beneficios, aprende recetas de remedios naturales y explora mucho más sobre el poder curativo de la naturaleza.",
        size=16,
        color=ft.colors.BLACK45,
        text_align=ft.TextAlign.LEFT
    )

    # Botón de identificar planta
    identify_button = ft.ElevatedButton(
        text="Identifica tu planta",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.colors.GREEN_400,
            color=ft.colors.BLACK,
        )
    )

    # Botón de iniciar sesión
    login_button = ft.ElevatedButton(
        text="Iniciar Sesión",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.colors.GREEN_400,
            color=ft.colors.BLACK,
        )
    )

    # Layout de los botones
    button_row = ft.Row(
        controls=[identify_button, login_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Layout principal
    page.add(
        ft.Column(
            controls=[
                logo,
                title_text,
                subtitle_text,
                button_row
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)
