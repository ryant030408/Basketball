import pandas as pd
from nba_py import game, player, team
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import graph_gui_functions as gf
from pathlib import Path

# decides which functon to execute
def download_finder(stat):
    print('test')

# fills frame with data about files
def frame_filler(self, stat):

    # create filename
    file_name = "/" + stat + "/" + stat + "_for_" + self.yearVar.get()
    file = Path(file_name)

    # frame of widget
    frame = tk.Frame(self, borderwidth=1, relief="solid")
    label = tk.Label(frame, text=stat)
    label.grid(row=0, column=0)

    # check if stat is downloaded
    if file.is_file():
        # text if already downloaded
        downloaded = Label(frame, text="COMPLETE")
        downloaded.pack()
    else:
        # get button
        button = tk.Button(frame, text='GET', pady=25)
        button.grid(row=1, column=0)

    return frame


# gui
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # window specs
        self.minsize(900, 400)

        # title
        self.title('Downloader')

        #------------------------------------

        # frame for year
        self.year_frame = Frame(self)

        # year drop down
        self. yearVar = StringVar()
        self.year_combobox = ttk.Combobox(self.year_frame, values=gf.year_creator(), textvariable=self.yearVar)
        self.year_combobox.current(1)
        self.year_combobox.pack()

        # add year drop down to gui
        self.year_frame.grid(row=0, column=0)

        #------------------------------------

        frame_filler(self, 'play_by_play').grid(row=1, column=0)



app = App()
app.mainloop()