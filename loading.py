import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import time
import os
import subprocess
import table_data

i = 0

def loadingw():
    loading_w = tk.Tk()
    loading_w.title("Loading")
    loading_w.configure(bg="#fff")
    loading_w.resizable(False, False)

    width_of_window = 800
    height_of_window = 600
    screen_width = loading_w.winfo_screenwidth()
    screen_height = loading_w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    loading_w.geometry("%dx%d+%d+%d" %
                       (width_of_window, height_of_window, x_coordinate, y_coordinate))
    loading_w.overrideredirect(1)

    img = PhotoImage(
        file="bg2.png")
    Label(loading_w, image=img, bg="white").place(x=0, y=0)

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar",
                foreground='red', background='#2666FA')
    progress = Progressbar(loading_w, style="red.Horizontal.TProgressbar",
                           orient=HORIZONTAL, length=800, mode='determinate',)

    # Fungsi - fungsi
    def top():
        loading_w.withdraw()
        loading_w.destroy()
        table_data.tablew()

    def load():
        global i
        if i <= 100:
            progress['value'] = i
            loading_w.update_idletasks()
            time.sleep(0.03)
            i = i + 1
            loading_w.after(10, load)
        else:
            top()

    progress.place(x=0, y=583)

    load()
    loading_w.mainloop()


# loadingw()
