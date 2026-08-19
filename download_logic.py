import os
import time
import asyncio
import sys
import yt_dlp
import flet as ft

downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

formats = {
    'mp4': {
        'outtmpl': os.path.join(downloads_dir, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best / bestvideo/best / worst', 
        #'listformats': True,
        'merge_output_format': 'mp4',  
        'extractor_args': {'youtube': { 'player_client': ['android', 'tv', 'ios', 'web'], 'skip': ['webpage', 'configs']}},
        'retries': 20,
        'fragment_retries': 20,
        'retry_sleep': 3,
        'socket_timeout': 15,   
    },
    'mp3': {
        'outtmpl': os.path.join(downloads_dir, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best / bestvideo/best / worst',
        #'listformats': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],       
        'extractor_args': {'youtube': { 'player_client': ['android', 'tv', 'ios', 'web'], 'skip': ['webpage', 'configs']}},
        'retries': 20,
        'fragment_retries': 20,
        'retry_sleep': 3,
        'socket_timeout': 15,
    },
}

def get_loc():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def download(url: str, format: str, status_text: ft.Text): 

    qjs_path = os.path.join(get_loc(), 'qjs.exe')
    opts = formats[format.lower()] 
    opts['ffmpeg_location']=get_loc()
    opts['js_runtimes']={
        'quickjs': {
            'path': qjs_path
        }
    }
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])   
        status_text.value = "Downloaded Successfully"
        status_text.update()
    except Exception as e:
        status_text.value = f"Failed to download: {e}"
        status_text.update()