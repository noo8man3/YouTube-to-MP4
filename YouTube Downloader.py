from tkinter import *
from tkinter import ttk
from pytube import YouTube

def download(*args):
    yt = YouTube(url.get())
    yd = yt.streams.get_audio_only()
    yd.download('C:/Users/brend/Music/MP4 Staging')

root = Tk()
root.geometry("280x90")
root.title("YouTube MP3 Downloader")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

url = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="")
link_title = ttk.Label(root, text="Link", width=16, font=("Courier New", 16)).grid(column=0, row=1)
link_field = ttk.Entry(root, width=16, font=("Courier New", 16), textvariable=url).grid(column=0, row=2)
download_btn = ttk.Button(root, width=10, text="Download", command=download).grid(column=0, row=3)

root.mainloop()