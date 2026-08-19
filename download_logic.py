import os
import time
import asyncio
import yt_dlp
import flet as ft

downloads_dir = os.path.expanduser("~/Downloads")

formats = {
    'mp4': {
        'outtmpl': f'{downloads_dir}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    },
    'mp3': {
        'outtmpl': f'{downloads_dir}/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],       
    }
}

def download(url: str, format: str, status_text: ft.Text):
    
    opts = formats[format.lower()] 
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])   
        status_text.value = "Downloaded Successfully"
        status_text.update()
    except Exception as e:
        status_text.value = f"Failed to download: {e}"
        status_text.update()