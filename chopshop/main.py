from flask import Flask, request, json
from pytube import YouTube
from pydub import AudioSegment
from dotenv import load_dotenv
from flask_cors import CORS
from datetime import datetime


load_dotenv()

from utils import checkPaths, complete_func, progress_func, uploadFile

today = str(datetime.today().date()).replace("-", "_")


checkPaths()

app = Flask(__name__)
CORS(app)


@app.route("/tune")
def tune():
    Y_URL = request.headers.get("URL")
    Y_ID = request.headers.get("ID")
    start = int(request.headers.get("START"))
    end = int(request.headers.get("END"))

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

    audio.download(filename="assets/down/" + today + "/" + Y_ID + audio_format)

    song = AudioSegment.from_file(
        "assets/down/" + today + "/" + Y_ID + audio_format, "mp4"
    )
    sliced_song = song[start:end]
    sliced_song.export("assets/export/" + today + "/" + Y_ID + ".m4r", format="ipod")
    return str(uploadFile(filename="assets/export/" + today + "/" + Y_ID + ".m4r"))


@app.route("/videoconfig")
def config():
    today = str(datetime.today().date()).replace("-", "_")
    checkPaths()
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


@app.route("/ytconfigs")
def ytconfig():
    today = str(datetime.today().date()).replace("-", "_")
    checkPaths()

    Y_URL = request.headers.get("URL")
    print("Hola")

    yt = YouTube(
        Y_URL,
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
    )

    try:
        available_formats = []
        for i in range(len(yt.streams.filter(only_audio=True))):
            # available_formats.append()
            # <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">
            available_formats.append(
                {
                    "itag": yt.streams[i].itag,
                    "mime_type": yt.streams[i].mime_type,
                    "abr": yt.streams[i].abr,
                    "itag": yt.streams[i].itag,
                    # "acodec": yt.streams[i].acodec,
                    # "progressive": yt.streams[i].progressive,
                    "type": yt.streams[i].type,
                    "approx_filesize": yt.streams[i].filesize_approx,
                }
            )

        return json.dumps(
            {"available_formats": available_formats, "length": str(yt.length)}
        )

    except Exception as err:
        print(err)
        return "0"


@app.route("/ytdown")
def ytdown():
    Y_URL = request.headers.get("URL")
    Y_ID = request.headers.get("ID")
    Y_TAG = request.headers.get("TAG")
    start = int(request.headers.get("START"))
    end = int(request.headers.get("END"))

    yt = YouTube(
        Y_URL,
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
    )
    stream = yt.streams.get_by_itag(Y_TAG)

    stream.download(filename="assets/down/" + today + "/" + Y_ID + stream.mime_type)

    # sliced_song = song[start:end]
    # sliced_song.export("assets/export/" + today + "/" + Y_ID + ".m4r", format="ipod")
    return str(uploadFile(filename="assets/export/" + today + "/" + Y_ID + ".m4r"))
