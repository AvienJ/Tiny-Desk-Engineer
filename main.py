# NAME: Tiny Desk Engineer)
# FILE: main.py(DIR: .\)

# DESCRIPTION: "A tiny desk engineer that dances on your desktop"
# CREDITS: Avien Jones(GITHUB: AvienJ)
# MISC\NOTES: 
# ____________________
import tkinter as tk
from tkinter import *

root = tk.Tk()

screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
mouse_x, mouse_y = root.winfo_pointerx(), root.winfo_pointery()
root.geometry("+" + str(int(screen_width / 1.2)) + "+" + str(int(screen_height / 1.37)))

frames = [tk.PhotoImage(file="engineer.gif",format = "gif -index %i" %(i)) for i in range(100)]

def update_frames(img_frame):
    try:
        global engie_frames
        engie_frames = frames[img_frame]
    except IndexError:
        img_frame = 1
    img_frame += 1
    engie_label.configure(image=engie_frames)
    root.after(30, update_frames, img_frame)

engie_label = tk.Label(root, bg="white")

root.overrideredirect(True)
root.lift()

root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")

engie_label.pack()

root.bind("tde", exit)

root.after(0, update_frames, 0)
root.mainloop()
