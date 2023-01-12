from tkinter import *
from tkinter import filedialog
from moviepy import *
from pytube import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


# Functions
def select_path():
    # Allows user to select a path from file explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)  # Changes text of path to folder selected


def download_file():
    # Get user path
    get_link = link_field.get()
    # Get Selected Path
    user_path = path_label.cget("text")
    # Download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # Move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')


screen = Tk()
title = screen.title('YouTube Download')
canvas = Canvas(screen, width=750, height=750)
canvas.pack()

# Image Logo
logo_img = PhotoImage(file='yt.png')

# Resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 120, image=logo_img)

# Link Field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download URL In The Box Below: ", font=('Arial', 12))

# Select Path for Saving File
path_label = Label(screen, text='Select Folder to Download To: ', font=('Arial', 10))
select_btn = Button(screen, text='Select Folder', command=select_path)

canvas.create_window(250, 320, window=path_label)
canvas.create_window(250, 360, window=select_btn)

# Add Widgets
canvas.create_window(250, 260, window=link_label)
canvas.create_window(250, 290, window=link_field)

# Buttons
download_btn = Button(screen, text='Download Video', command=download_file)

# Add to Canvas
canvas.create_window(250, 420, window=download_btn)

screen.mainloop()
