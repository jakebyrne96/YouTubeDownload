from tkinter import *
from tkinter import filedialog

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
link_label = Label(screen, text="Enter Download URL In The Box Below: ", font=('Arial', 14))

# Select Path for Saving File
path_label = Label(screen, text='Select Folder to Download To0: ', font=('Arial', 12))
select_btn = Button(screen, text='Select Folder')

# Add Widgets11
canvas.create_window(250, 260, window=link_label)
canvas.create_window(250, 290, window=link_field)

# Buttons
download_btn = Button(screen, text='Download Video')


screen.mainloop()
