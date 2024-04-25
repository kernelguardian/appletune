from pytube import YouTube
from pydub import AudioSegment
import os


if not os.path.exists("assets"):
    os.makedirs("assets")

if not os.path.exists("assets/export"):
    os.makedirs("assets/export")

if not os.path.exists("assets/down"):
    os.makedirs("assets/down")


def progress_func(stream, chunk, bytes_remaining):
    print("Progress: ", end="")
    print(bytes_remaining)


def complete_func(stream, file_handle):
    print("Download Completed")
    print(stream, file_handle)


Y_ID = "test"
start = 10 * 1000
end = 50 * 1000

yt = YouTube(
    "https://youtu.be/3f2gfIImoas?list=RDMM3f2gfIImoas",
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
