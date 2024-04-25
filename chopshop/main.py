from flask import Flask, request
from pytube import YouTube
from pydub import AudioSegment
import os
from dotenv import load_dotenv

load_dotenv()

from utils import checkPaths, complete_func, progress_func, uploadFile


checkPaths()

app = Flask(__name__)


@app.route("/tune")
def tune():
    Y_URL = request.headers.get("URL")
    Y_ID = request.headers.get("ID")
    start = request.headers.get("START")
    end = request.headers.get("END")

    yt = YouTube(
        Y_URL,
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
    )
    available_formats = yt.streams.filter(only_audio=True)
    for i in range(len(available_formats)):
        if available_formats[i].mime_type == "audio/mp4":
            audio = yt.streams.filter(only_audio=True)[i]
            audio_format = ".mp4"
            break
        if available_formats[i].mime_type == "audio/webm":
            audio = yt.streams.filter(only_audio=True)[i]
            audio_format = ".webm"
            break

    audio.download(filename="assets/down/" + Y_ID + audio_format)

    song = AudioSegment.from_file("assets/down/" + Y_ID + audio_format, "mp4")
    sliced_song = song[start:end]
    sliced_song.export("assets/export/" + Y_ID + ".m4r", format="ipod")
    return uploadFile(filename="assets/export/" + Y_ID + ".m4r")


@app.route("/videoconfig")
def config():
    Y_URL = request.headers.get("URL")

    yt = YouTube(
        Y_URL,
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
    )
    try:
        length = yt.length
        return str(yt.length)
    except Exception as err:
        print(err)
        return "0"
