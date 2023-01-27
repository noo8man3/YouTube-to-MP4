from tkinter import *
from tkinter import ttk
from pytube import YouTube

def download(*args):
    yt = YouTube(url.get())
    yd = yt.streams.get_audio_only()
    yd.download(directory.get())

root = Tk()
root.geometry("300x150")
root.title("YouTube-to-MP4")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

url = StringVar()
directory = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="")

link_title = ttk.Label(root, text="Link", width=16, font=("Courier New", 16)).grid(column=0, row=1)
link_field = ttk.Entry(root, width=16, font=("Courier New", 16), textvariable=url).grid(column=0, row=2)

dir_title = ttk.Label(root, text="Directory", width=16, font=("Courier New", 16)).grid(column=0, row=3)
dir_field = ttk.Entry(root, width=16, font=("Courier New", 16), textvariable=directory).grid(column=0, row=4)

download_btn = ttk.Button(root, width=10, text="Download", command=download).grid(column=0, row=5)

root.mainloop()