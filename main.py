import subprocess
import flet as ft
from ui import main

def update():
    try:        
        from yt_dlp import YoutubeDL
        from yt_dlp.update import Updater
        Updater(YoutubeDL).update()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    update()
    ft.run(main=main, assets_dir='assets')