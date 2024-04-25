import os


def checkPaths():
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
