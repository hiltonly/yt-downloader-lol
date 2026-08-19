import flet as ft
from download_logic import download

def main(page: ft.Page):

    page.title = "YouTube Video Downloader"
    page.window.resizable = False
    page.window.full_screen = False
    page.window.title_bar_hidden = False
    page.window.width = 600
    page.window.height = 320
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER   
    page.bgcolor = "#0f0f0f"
    page.theme_mode = ft.ThemeMode.DARK 
    page.window.icon = '/icon.ico'
    page.window.maximizable = False

    label = ft.Text(
        value="YouTube Video Downloader", 
        height=40, 
        width=page.window.width-40, 
        size=30,
        margin=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER, 
        align=ft.Alignment.TOP_CENTER,
        color="#ffffff",
    )

    status_text = ft.Text(
        value=" ", 
        height=20, 
        width=page.window.width-40, 
        size=12,
        margin=2,
        text_align=ft.TextAlign.CENTER, 
        align=ft.Alignment.TOP_CENTER,
        color="#ffffff",
        animate_opacity=ft.Animation(duration=1000, curve=ft.AnimationCurve.EASE_OUT)
    )

    text_field = ft.TextField(
        hint_text="Paste your Youtube video link",
        width=page.window.width-170,
        height=50,
        bgcolor="#202020",
        border_color="#535353",
        border_radius=5,
        focused_border_color="#b1b1b1",
        focused_border_width=1,
        border_width=1,
        color="#b1b1b1"
    ) 

    def on_click(e):

        url = text_field.value
        format = dropdown.value

        # status_text.value = f'Downloading in Downloads with format {format}...'
        #status_text.opacity = 1
        #status_text.update()
        #

        download(url, format, status_text)
        
    download_button = ft.ElevatedButton(
        content="Download",
        width=page.window.width-40,
        height=40,
        bgcolor="#202020",
        color="#E2E2E2",   
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            overlay_color="#333333",
            bgcolor={
                ft.ControlState.HOVERED: "#222222"
            }
        ),
        on_click=on_click
    )

    dropdown = ft.Dropdown(
        label="Choose format",
        options=[ft.dropdown.Option("mp4"), ft.dropdown.Option("mp3")],
        value="mp4", 
        height=text_field.height,
        width=120,
        bgcolor="#202020",
        border_color="#535353",
        border_radius=5,
        focused_border_color="#b1b1b1",
        focused_border_width=1,
        border_width=1,
    )

    page.add(
        ft.Container(     
            expand=True, 
            alignment=ft.Alignment.TOP_CENTER,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                controls=[
                    label,
                    ft.Row(                     
                        controls=[text_field, dropdown],
                        spacing = 6,
                        tight = True,
                        alignment=ft.Alignment.TOP_CENTER
                    ),
                    download_button,
                    status_text
                ],
                spacing=15,
                alignment=ft.Alignment.TOP_CENTER
            ),
        )
    )