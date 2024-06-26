import os
from supabase import create_client, Client
from datetime import datetime

today = str(datetime.today().date()).replace("-", "_")

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

bucket_name: str = "appletune"


def uploadFile(filename):
    try:
        file = load_file(filename)
        data = supabase.storage.from_(bucket_name).upload(path=filename, file=file)

        res = supabase.storage.from_(bucket_name).get_public_url(filename)
        return res
    except Exception as err:
        return "Error"


def checkPaths():
    if not os.path.exists("assets"):
        os.makedirs("assets", exist_ok=True)

    if not os.path.exists("assets/export/" + today + "/"):
        os.makedirs("assets/export/" + today + "/", exist_ok=True)

    if not os.path.exists("assets/down" + today + "/"):
        os.makedirs("assets/down/" + today + "/", exist_ok=True)


def progress_func(stream, chunk, bytes_remaining):
    print("Progress: ", end="")
    print(bytes_remaining)


def complete_func(stream, file_handle):
    print("Download Completed")
    print(stream, file_handle)


def load_file(file_path):
    try:
        with open(file_path, "rb") as file:
            # Read the contents of the file
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print("File not found.")
        return None
