from pytube import YouTube
from pydub import AudioSegment
from datetime import datetime
from dotenv import load_dotenv

from utils import checkPaths, progress_func, complete_func

load_dotenv()


today = str(datetime.today().date()).replace("-", "_")

from utils import uploadFile

checkPaths()


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


audio.download(filename="assets/down/" + today + "/" + Y_ID + audio_format)

song = AudioSegment.from_file("assets/down/" + today + "/" + Y_ID + audio_format, "mp4")
sliced_song = song[start:end]
sliced_song.export("assets/export/" + today + "/" + Y_ID + ".m4r", format="ipod")


uploadFile(filename="assets/export/" + today + "/" + "test" + ".m4r")
